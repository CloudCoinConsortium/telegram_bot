from utils import getwalletname
from deposit import deposit
from balance import balance

def bank(update, context):
    message = update.message.text
    
    # Split the message into words
    phrases = message.split()
    phrases.pop(0)
    phrasehandler(phrases, update=update, context=context)
    user = update.message.from_user
    print(message)
    print(phrases)

def phrasehandler(phrases, update, context):
    if bool(len(phrases)):
        print('handling ' , phrases[0])
        phrase = phrases[0]
        if phrase == "whatsmywallet":
            update.message.reply_text("Your wallet name is " + getwalletname(update=update))
        elif(phrase == "deposit"):
            deposit(phrases,update=update, context=context)
        elif(phrase == "balance"):
            wbalance = balance(update=update)
            update.message.reply_text("Your wallet balance is " + str(wbalance))
    else:
        print('can not proceed')

