import bitcoin
import os
import time

address_to_find = input("Which keyword do you want to find ? ")
start=time.time()#记录程序运行的时间
i = 0

while True:

    wallet = bitcoin.Wallet()

    i += 1
    print("[{}] {}".format(i, wallet.get_address_uncompressed()))
    str = wallet.get_address_uncompressed()
    result = address_to_find in str
    if result :
        print("   => Eureka !!! Private key : {}".format(wallet.get_wif_uncompressed()))
        break

    i += 1
    print("[{}] {}".format(i, wallet.get_address_compressed()))
    str = wallet.get_address_compressed()
    result2 = address_to_find in str
    if result2 :
        print("   => Eureka !!! Private key : {}".format(wallet.get_wif_compressed()))
        break
end=time.time()
print('Running time: %s Seconds'%(end-start))
os.system("pause")
