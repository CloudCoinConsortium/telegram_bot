from utils import getwalletname
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
    else:
        print('can not proceed')

