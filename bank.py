from utils import getwalletname
from deposit import deposit
from balance import balance

def bank(update, context):
    if(getwalletname(update=update) == None):
        update.message.reply_text('You dont have a user name.')
        return
    message = update.message
    # Split the message into words
    if(update.message.photo):
        photos = update.message.photo
        #print('Photo:', photos)
        #print('No of photos:', len(photos))
        print('caption', message.caption)
        caption = ''
        if(message.caption):
            caption = message.caption
        elif(message.caption_html):
            caption = message.caption_html
        else:
            caption = '/bank deposit'
        phrases = caption.split()
    else:
        print('Message:',message.text)
        phrases = message.text.split()

    phrases.pop(0)
    phrasehandler(phrases, update=update, context=context)
    user = update.message.from_user
    #print(message)
    #print(phrases)

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

