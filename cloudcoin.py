import random
import string
import ctypes

def generate_random_string():
    hex_chars = string.hexdigits[:-6] # exclude letters 'a' to 'f'
    return ''.join(random.choice(hex_chars) for _ in range(32))

class CloudCoinFile:
    coincount = ctypes.c_uint16(0)
    flags = ctypes.c_uint8(0)
    formatType = ctypes.c_uint8(10)
    cloudId = ctypes.c_uint8(2)
    coinID1 = ctypes.c_uint16(10)
    coinID2 = ctypes.c_uint8(10)
    reserved = ctypes.c_uint8(0)
    encryptionType = ctypes.c_uint8(0)
    
    hash = ctypes.create_string_buffer(7)
    def __init__(self):
        self.sn = None
        self.ans = [0] * 25
        self.pans = [0] * 25
        self.statuses = []
        self.pownString = ""
        self.formatType = 10
        self.cloudId = 1
        self.coinID1 = 10
        self.coinID2 = 10
        self.reserved = 0
        self.coincount = 0
        self.hash = b'\x00\x00\x00\x00\x00\x00\x00\x00'
        self.coins = [CloudCoin] * 1

        self.splitNumber = None
        self.flags = 0
        self.encryptionType = 0
        self.receiptId = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        self.passwordHash = ""
    def generatePANS(self):
        self.ans[0] = generate_random_string()
        for i in range(len(self.ans)):
            self.ans[i] = generate_random_string()

class CloudCoin:
    dn = None
    reserved = b'\x00\x00\x00'
    sn = ctypes.c_uint32(0)
    def __init__(self):
        self.sn = ctypes.c_uint32(0)
        self.ans = [0] * 25
        self.pans = [0] * 25
        self.statuses = []
        self.pownString = ""
        self.seed = None
        self.reserved = b'\x00\x00\x00'

