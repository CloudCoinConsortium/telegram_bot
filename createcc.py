import sys
from cloudcoin import CloudCoinFile, CloudCoin
import struct
import random
import secrets

coincount = int(sys.argv[1])
dens = [-8, -7, -6, -5, -4, -3, -2, -1]
print('Creating ' , coincount, ' Coins..')
filename = "coins.bin"
cc = CloudCoinFile()
cc.coincount = int(coincount)
cc.coins = [CloudCoin] * int(coincount)
#print(cc.coins)

with open(filename, "wb") as f:
    binary_data = struct.pack("bbbbbbb8sb16s", cc.formatType, cc.cloudId, cc.coinID1, cc.coinID2,cc.reserved,cc.encryptionType, cc.coincount, cc.hash, cc.flags, cc.receiptId)
    f.write(binary_data)
    for i in range(coincount):
        cc.coins[i].dn = (random.choice(dens))
        rand_int = random.getrandbits(32)
        #cc.coins[i].sn = hex(rand_int)[2:].zfill(8)
        cc.coins[i].sn = secrets.token_hex(4)
        cc.coins[i].seed = secrets.token_hex(11)
        #coinbdata = struct.pack('bb11s3s', cc.coins[i].dn, cc.coins[i].sn, cc.coins[i].seed, cc.coins[i].reserved)
        coinbdata = struct.pack('1sb4s11s3s', bytes.fromhex('00'), cc.coins[i].dn, bytes.fromhex(cc.coins[i].sn), bytes.fromhex(cc.coins[i].seed), (cc.coins[i].reserved))
        f.write(coinbdata)

print('Coins written to ' , filename)

with open(filename, 'rb') as rf:
    bdata = rf.read()
    format_string = "bbbbbbb8sb16s"
    count = bdata[6]
    header = struct.unpack(format_string, bdata[:32])
    for i in range(count):
        coinformat = "1sb4s11s3s"
        coindata = struct.unpack_from('1sb4s11s3s', bdata, int(32 + i *20))
        print('Coin ', i + 1 , ': ' , coindata)
    bytecount = int(32 + count * 20)
    unpacked_data = struct.unpack(format_string, bdata[:32])

#print(unpacked_data)
print(header)
#print(count)








