"""
This module implements GPB chain processing in python
It is fully interoperable with C++
"""

import struct
import zlib
import logging

from chain_exceptions import *
from gpb_message_factory import *

class ChainItem(object):
    '''
    Handles single chain item
    source: http://p4-web.it.qwilt.com/@rev1=head@//main/dev/doc/modules/infra/gpb/gpb-chain-overview.pptx
    Format of the chain link is:
       |32-bit Chain header|64 bit Descriptor-Name-Hash(Little Endian)|Message|CRC32|
       | Chain-Header      | ------------------------ Data -------------------------|

    Format of the header is:
       31 30  28  26 25       22           0
      | MAJ|MIN| HL| L|Reserved|    Length |
    '''

    CHAIN_HEADER_SIZE=4
    CRC32_SIZE=4
    CRC32_FINAL_XOR = 0xFFFFFFFF

    def __init__(self):
        '''Initialize Chain Item'''
        self.totalLength = 0        # Total length of chain item
        self.reserved = 0
        self.isLast = False         # last message in the chain
        self.gpbHeaderLength = 12   # this is value in current protocol version
        self.minorVersion = 0       # minor version no
        self.majorVersion = 0       # major version no
        self.descriptorNameHash = 0 # descriptor name hash number
        self._message = ""          # serialized GPB message
        self.crc32 = 0
        self.packedChainHeader = "" # binary string representation of 32 bit chain header
        self.packedGPBHeader = ""   # binary string representation of GPB header - chain header (in current version it is actually DNH)

    def parseChainHeader(self, packedChainHeader):
        '''parse 32bit Chain header'''
        self.packedChainHeader = packedChainHeader
        (headerVal,) = struct.unpack("I", packedChainHeader)
        self.totalLength =  headerVal & (0x3FFFFF)
        self.reserved =     (headerVal>>22)&0x7
        self.isLast =       ((headerVal>>25)&0x1) != 0
        # header lengthId determines size of chainitem header (chain header + gpb header)
        headerLengthId =    (headerVal>>26)&0x3
        if headerLengthId == 0:
            self.gpbHeaderLength = 12
        elif headerLengthId == 1:
            self.gpbHeaderLength = 16
        elif headerLengthId == 2:
            self.gpbHeaderLength = 24
        elif headerLengthId == 3:
            self.gpbHeaderLength = 48
        self.minorVersion = (headerVal>>28)&0x3
        self.majorVersion = (headerVal>>30)&0x3

    def calculateChainHeaderValue(self):
        '''Calculates chain header value from ChainItem attributes'''
        ch = self.totalLength
        if self.isLast:
            ch = ch | (1<<25)
        # In current version: gpbHeaderLength == 12 so headerLengthId = 0
        ch = ch | (self.minorVersion << 28)
        ch = ch | (self.majorVersion << 30)
        return ch

    def getDataLength(self):
        '''Returns serialized length of chain item excluding its header'''
        return self.totalLength - ChainItem.CHAIN_HEADER_SIZE

    def readData(self, data):
        '''Reads chain item data after the header was already read'''
        if len(data) != self.getDataLength():
            raise NotCompleteMessageException(self.getDataLength())
        leftGPBHeaderLength = self.gpbHeaderLength - ChainItem.CHAIN_HEADER_SIZE 
        self.packedGPBHeader = data[:leftGPBHeaderLength]
        (self.descriptorNameHash,) = struct.unpack("Q", self.packedGPBHeader)
        self._message = data[leftGPBHeaderLength:- ChainItem.CRC32_SIZE]
        crc32Bin = data[-ChainItem.CRC32_SIZE:]
        (self.crc32,) = struct.unpack("I", crc32Bin)
        logging.debug("readData: totalLen: %d DNH=0x%x CRC32=0x%x msg-len=%d" % (self.totalLength, self.descriptorNameHash, self.crc32, len(self._message)))
        self.validateMessageCRC()

    def validateMessageCRC(self):
        '''Validates CRC of the message'''
        actualCRC = self.calcCRC32(self.packedChainHeader + self.packedGPBHeader + self._message)
        if self.crc32 != actualCRC:
            raise InvalidCRCException(self.crc32, actualCRC)

    def getMessageLength(self):
        '''Returns real message length'''
        return self.totalLength - self.gpbHeaderLength - ChainItem.CRC32_SIZE

    def getPackedMessage(self):
        '''Pack chain item to single message ready to send'''
        fullHeader = struct.pack("=IQ", self.calculateChainHeaderValue(), self.descriptorNameHash)
        crc32 = self.calcCRC32(fullHeader + self._message)
        packedCRC = struct.pack("I", crc32)
        return fullHeader + self._message + packedCRC

    def getMessage(self):
        '''Accessor to actual serialized GPB message'''
        return self._message

    def setMessage(self, msg):
        '''Setter of GPB message'''
        self._message = msg
        # update total length
        self.totalLength = 12 + len(msg) + ChainItem.CRC32_SIZE
        self.crc32 = -1

    def calcCRC32(self, data):
        # make crc32 unsigned int
        val = (zlib.crc32(data,0) & 0xFFFFFFFF)
        logging.debug("Calculated CRC is 0x%x" % val)
        return val


class iGPBChain:
    '''
    Input GPB chain base class
    This class doesn't deal with actual IO so  child classes should implement function
        def readRaw(self, size):

    Use model:
        ichain = ifGPBChain(file)
        # Teach the chain about all possible GPB messages that may be found in it
        ichain.addFactoryMessage(MyMessage1())
        ichain.addFactoryMessage(MyMessage2())

        # Now we can start iterating over all messages
        for message in ichain:
            print message
    '''
    def __init__(self, factory=None):
        '''Constructor, allows to provide already populated factory'''
        self.factory = factory
        self._isLastMessageInChain = False

    def addFactoryMessage(self, message):
        '''Registers message class in factory'''
        if self.factory == None:
            self.factory = GPBMessageFactory()
        self.factory.addMessage(message)

    def next(self):
        '''Reads single message from stream, if no more messages are available StopIterationException is thrown'''
        try:
            packedChainHeader = self.readRaw(ChainItem.CHAIN_HEADER_SIZE)
        except EOFError:
            raise StopIteration
        chainItem = ChainItem()
        chainItem.parseChainHeader(packedChainHeader)
        dataLength = chainItem.getDataLength()
        logging.debug("DataLength %d" % dataLength)
        try:
            data = self.readRaw(dataLength)
        except EOFError:
            logging.debug("Wanted %d" % dataLength)
            raise NotCompleteMessageException(dataLength)
        chainItem.readData(data)
        self._isLastMessageInChain = chainItem.isLast
        return self.factory.createMessageByDNH(chainItem.descriptorNameHash, chainItem.getMessage())
    
    def isLastMessageInChain(self):
        '''Returns True if the last returned message was marked as last'''
        return self._isLastMessageInChain

    def __iter__(self):
        '''Makes iGPBChain an iterator object of itself'''
        return self

    def readRaw(self, size):
        '''Abstract function that reads raw data from stream, if it fails to read the exact amout of data it should raise EOFError'''
        raise NotImplementedError

class oGPBChain:
    '''
    Output GPB chain base class
    This class doesn't deal with actual IO so child classes should implement functions
        def writeRaw(self, size):
        def close(self):
    Use model:
        ochain = ofGPBChain(file)
        ochain.append(message1);
        ochain.append(message2, isLast=True)
        ochain.close()
    '''
    def __init__(self):
        '''Contstructor'''
        self.factory = GPBMessageFactory()

    def append(self, message, isLast=False):
        '''Appends message -> serialize it to stream'''
        chainItem = ChainItem()
        chainItem.isLast = isLast
        chainItem.setMessage(message.SerializeToString())
        chainItem.descriptorNameHash = self.factory.getMessageDNH(message)
        logging.debug("oChain: GPB totalLen: %d DNH=0x%x CRC32=0x%x msg-len=%d" % (chainItem.totalLength, chainItem.descriptorNameHash, chainItem.crc32, len(chainItem.getMessage())))
        self.writeRaw(chainItem.getPackedMessage())

    def writeRaw(self, size):
        '''Abstract function that writes raw data to stream'''
        raise NotImplementedError

class ifGPBChain(iGPBChain):
    '''iGPBChain implementation to the file'''
    def __init__(self, file, factory=None):
        iGPBChain.__init__(self, factory)
        self.file = file

    def readRaw(self, size):
        data = self.file.read(size)
        if len(data) != size:
            raise EOFError
        return data

class ofGPBChain(oGPBChain):
    '''oGPBChain implementation to the file'''
    def __init__(self, file):
        oGPBChain.__init__(self)
        self.file = file

    def writeRaw(self, data):
        self.file.write(data)

class oGenericGPBChain(oGPBChain):
    '''oGPBChain implementation to the an object that implements the function "write(item)"'''
    def __init__(self, writer):
        oGPBChain.__init__(self)
        self._writer = writer

    def writeRaw(self, data):
        self._writer.write(data)


