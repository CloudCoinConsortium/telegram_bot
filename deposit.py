from ast import While
from urllib import response
import requests
from constants import baseUrl
import os
import json
import time
from utils import getwalletname
from balance import balance

def deposit(args, update, context):
    wallet = getwalletname(update)
    user = update.message.from_user.username

    nftWalletName =  "NFTs." + wallet
    # encode # as special character to be used in url
    walletget = wallet.replace("#","%23")
    # check if wallet exists
    checkWalletUrl = baseUrl + 'wallets/' + walletget + '?contents=false'
    response = requests.get(checkWalletUrl)
    responsejson = response.json()
    fullpath = os.path.join(os.getcwd(), 'import', str(user))
    isExist = os.path.exists(fullpath)
    if not isExist:
        os.makedirs(fullpath)
        print("The new directory is created!")
    # create a new one is wallet does not exists
    if(responsejson['status'] != 'success'):
        print('Wallet does not exist.Creating new one')
        createWalletUrl = baseUrl + 'wallets'
        walletJson = { 'name': wallet}
        nftwalletJson = {'name': nftWalletName}
        print(walletJson, nftwalletJson)
        createresponse = requests.post(createWalletUrl, json= walletJson)
        createresponsejson = createresponse.json()
        nftcreateresponse = requests.post(createWalletUrl, json= nftwalletJson)
        nftcreateresponsejson = nftcreateresponse.json()
        
        if(createresponsejson['status'] == 'success'):
            print('Wallet Created successfully')
            update.message.reply_text("New Wallet created for you. your wallet name is:" + wallet)
    update.message.reply_text('Depositing file...')
    if update.message.photo:
        # Get the largest image in the list of images
        image = update.message.photo[-1]
        file_id = image.file_id
        file_size = image.file_size
        file = context.bot.get_file(file_id)
        filename = file_id + ".png"
        file.download("import/" + user + '/' + filename)
        fullfilename = os.path.join(fullpath, filename)
        print(fullfilename)
        depositUrl = baseUrl + 'import'
        depositJson = {"name": wallet, "items":[{"type":"file", "data":fullfilename}]}
        print(depositJson)
        json_string = json.dumps(depositJson) 
        depositresponse = requests.post(depositUrl, json_string)
        depositresponsejson = depositresponse.json()
        print(depositresponsejson)
        depositstatus = depositresponsejson['payload']['status']
        TASK_URL = baseUrl + 'tasks/' + depositresponsejson['payload']['id']
                # poll for task status till status is changed to completed

        while depositstatus == 'running':
            taskresponse = requests.get(TASK_URL)
            taskresponsejson = taskresponse.json()
            depositstatus = taskresponsejson['payload']['status']
            time.sleep(2)
            print(taskresponsejson)
            if(depositstatus == 'completed'):
                    # calculate stats if deposit api call is successful and send a response to user
                authentic = taskresponsejson['payload']['data']['pown_results']['authentic']
                counterfeit = taskresponsejson['payload']['data']['pown_results']['counterfeit']
                total = taskresponsejson['payload']['data']['pown_results']['total']
                unknown = taskresponsejson['payload']['data']['pown_results']['unknown']
                fracked = taskresponsejson['payload']['data']['pown_results']['fracked']
                update.message.reply_text('Coins imported..\nTotal: ' + str(total) + '\nAuthentic: '+ str(authentic + fracked) +  '\nCounterfeit:' + str(counterfeit) + '\nUnknown: ' + str(unknown))
            else:
                update.message.reply_text('Unable to import coin')   
        update.message.reply_text('Balance: '+ balance(update))
            
                



