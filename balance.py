from utils import getwalletname
import requests
from constants import baseUrl

def balance(update):
    wallet = getwalletname(update)
    checkWalletUrl = baseUrl + 'wallets/' + wallet
    try:
        response = requests.get(checkWalletUrl)
        responsejson = response.json()
    # in case of success show the balance else display 0
        if(responsejson['status'] == 'success'):
            return ( str(responsejson['payload']['balance']))
        else:
            return (str(0))
    except Exception:
        return "Server unavailable. Please retry sometimes later"

