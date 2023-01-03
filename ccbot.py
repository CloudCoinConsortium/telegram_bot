import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from help import help
from dotenv import load_dotenv
import os

load_dotenv()

def command(update, context):
    # Get the user's message
    message = update.message.text
    
    # Split the message into words
    print(update.message)
    words = ['echo']
    
    # Get the first word (the command)
    command = words[0]
    
    # Get the rest of the words (the arguments)
    args = words[1:]
    
    # Check if the message has an image attachment
    if update.message.photo:
        # Get the largest image in the list of images
        image = update.message.photo[-1]
        file_id = image.file_id
        file_size = image.file_size
        
        # Download the image
        file = context.bot.get_file(file_id)
        file.download("image.jpg")
        
        # Send a message with the image's file size
        update.message.reply_text("Received image with size {}".format(file_size))
    
    # Send a message with the command and arguments
    update.message.reply_text("You used the {} command with the following arguments: {}".format(command, args))

def main():
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(os.environ['BOT_TOKEN'], use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add a command handler to handle the /echo command
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("echo", command))

    # Add a message handler to handle messages with image attachments
    dp.add_handler(MessageHandler(Filters.photo, command))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()
