from chain_exceptions import *

from a.infra.math.murmur_hash3 import murmurHash3_64

import logging

class GPBMessageFactory:
    '''Generates and serializes GPB messages according to to Descriptor Name Hash'''

    DNH_SEED = 0x372c3a8e # Seed value of hash taken from include/a/infra/gpb/utils.h

    def __init__(self):
        self.dictionary = {}
    def getMessageDNH(self, message):
        return murmurHash3_64(message.DESCRIPTOR.full_name, GPBMessageFactory.DNH_SEED)
    def addMessage(self, message):
        descriptorNameHash = self.getMessageDNH(message)
        logging.debug("addMessage(%s, 0x%x)" %(message.DESCRIPTOR.full_name, descriptorNameHash))
        self.dictionary[descriptorNameHash] = message
    def getByDNH(self, descriptorNameHash):
        if not descriptorNameHash in self.dictionary:
            raise UnknownGPBMessageException(descriptorNameHash)
        return self.dictionary[descriptorNameHash]
    def createMessageByDNH(self, descriptorNameHash, messageData):
        message = self.getByDNH(descriptorNameHash)
        newMessage = type(message)() # Create new object of the same class as message (implies that message has empty constructor)
        newMessage.ParseFromString(messageData)
        return newMessage


