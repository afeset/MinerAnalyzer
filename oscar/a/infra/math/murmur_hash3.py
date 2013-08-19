#
# Copyright Qwilt, 2010
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Integrated from ext/murmur_hash/MurmurHash3.cpp
# 
# Author: Original code by Austin Appleby, adapted by orens
# 
# Only the 64-bit versions of the code were kept. 128-bit hash not externalized.
#
# Adapted to python from C++ version by michaelg
#


#
# NOTE python has unlimited integer arithmetics
# This means:
# Unsinged 64 bit integers should be long pyhon numbers because python use signed integers
# each time we do + or * we have to perform (& MASK_64)
#

# To treat string as numbers
import struct

MASK_64 =     0xffffffffffffffffL
VALUE_2_64 = 0x10000000000000000L

def _rotl64(num,amount):
    '''Left rotate by given amount of bits'''
    return ((num << amount) | (num >> (64 - amount))) & MASK_64

def getblock( str, i ):
    '''Get integer as 8 byte block from string'''
    (res,) = struct.unpack("Q", str[8*i:8*(i+1)])
    #print "getblock(%d)=0x%x\n" % (i, res);
    return res

#----------
# 

def bmix64 ( h1, h2, k1, k2, c1, c2 ):
    '''
    Block mix - combine the key bits with the hash bits and scramble everything
    Returns tuple of the modified input variables in the same order
    '''
    k1 = (k1*c1) & MASK_64
    k1 = _rotl64(k1,23)
    k1 = (k1*c2) & MASK_64
    h1 = h1 ^ k1
    h1 = (h1 + h2) & MASK_64

    h2 = _rotl64(h2,41)

    k2 = (k2 * c2) & MASK_64
    k2 = _rotl64(k2,23)
    k2 = (k2 * c1) & MASK_64
    h2 = h2 ^ k2
    h2 = h2 + h1

    h1 = (((h1*3)&MASK_64) + 0x52dce729) & MASK_64
    h2 = (((h2*3)&MASK_64) + 0x38495ab5) & MASK_64

    c1 = (((c1*5)&MASK_64) + 0x7b7d159c) & MASK_64
    c2 = (((c2*5)&MASK_64) + 0x6bce6396) & MASK_64
    return (h1, h2, k1, k2, c1, c2)

def fmix64 ( k ):
    '''Finalization mix - avalanches all bits to within 0.05% bias'''
    k = k ^ (k >> 33)
    k = (k * 0xff51afd7ed558ccd) & MASK_64
    k = k ^ (k >> 33)
    k = (k * 0xc4ceb9fe1a85ec53) & MASK_64
    k = k ^ (k >> 33)

    return k;

#----------

def MurmurHash3_x64_128 ( data, seed ):
    '''Main routine, returns output as 2-64 bit numbers'''
    nblocks = len(data) / 16

    h1 = 0x9368e53c2f6af274 ^ seed
    h2 = 0x586dcd208f7cd3fd ^ seed

    c1 = 0x87c37b91114253d5
    c2 = 0x4cf5ad432745937f

    #----------
    # body

    for i in range(nblocks):
        k1 = getblock(data,i*2+0)
        k2 = getblock(data,i*2+1)

        (h1,h2,k1,k2,c1,c2) = bmix64(h1,h2,k1,k2,c1,c2)
        #print "for(i=%d) h1=0x%x h2=0x%x" % (i, h1, h2)

    #----------
    # tail

    tail_string = data[nblocks*16:]
    l = len(tail_string)
    if l >= 1:
        tail = struct.unpack(str(l)+'B', tail_string)
    k1 = 0;
    k2 = 0;

    if l >= 15: k2 = k2 ^ (tail[14] << 48)
    if l >= 14: k2 = k2 ^ (tail[13] << 40)
    if l >= 13: k2 = k2 ^ (tail[12] << 32)
    if l >= 12: k2 = k2 ^ (tail[11] << 24)
    if l >= 11: k2 = k2 ^ (tail[10] << 16)
    if l >= 10: k2 = k2 ^ (tail[ 9] << 8)
    if l >=  9: k2 = k2 ^ (tail[ 8] << 0)

    if l >=  8: k1 = k1 ^ (tail[ 7] << 56)
    if l >=  7: k1 = k1 ^ (tail[ 6] << 48)
    if l >=  6: k1 = k1 ^ (tail[ 5] << 40)
    if l >=  5: k1 = k1 ^ (tail[ 4] << 32)
    if l >=  4: k1 = k1 ^ (tail[ 3] << 24)
    if l >=  3: k1 = k1 ^ (tail[ 2] << 16)
    if l >=  2: k1 = k1 ^ (tail[ 1] << 8)
    if l >=  1:
        k1 = k1 ^ (tail[ 0] << 0)
        (h1,h2,k1,k2,c1,c2) = bmix64(h1,h2,k1,k2,c1,c2)

    #----------
    # finalization

    h2 = h2 ^ len(data)

    h1 = (h1 + h2) & MASK_64
    h2 = (h2 + h1) & MASK_64

    h1 = fmix64(h1)
    h2 = fmix64(h2)

    h1 = (h1 + h2) & MASK_64
    h2 = (h2 + h1) & MASK_64

    return (h1, h2)



#-----------------------------------------------------------------------------
# If we need a smaller hash value, it's faster to just use a portion of the 
# 128-bit hash

def murmurHash3_32(data, seed=0):
    '''Get lowest 32 bit'''

    temp = MurmurHash3_x64_128(data,seed)

    return temp[0] & 0xffffffff


def murmurHash3_64(data, seed=0):
    '''Get lowest 64 bit'''

    temp = MurmurHash3_x64_128(data, seed)

    return temp[0]

