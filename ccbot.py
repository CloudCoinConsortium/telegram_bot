import telegram
from telegram.ext import Updater, CommandHandler, Filters

def command(update, context):
    # Check if the message has an attachment
    if update.message.document:
        # Get the attachment
        attachment = update.message.document
        file_id = attachment.file_id
        file_name = attachment.file_name
        file_size = attachment.file_size
        
        # Do something with the attachment
        # For example, you could download the file and save it to disk
        file = context.bot.get_file(file_id)
        file.download("/path/to/save/file/{}".format(file_name))
        
        update.message.reply_text("Received attachment with file name {} and size {}".format(file_name, file_size))
    else:
        update.message.reply_text("No attachment received")

def main():
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("TOKEN", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add a handler to handle the command
    dp.add_handler(CommandHandler("command", command))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()
