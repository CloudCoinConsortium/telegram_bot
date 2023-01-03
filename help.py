def help(update, context):
    depositContent = DepositHelp()
    withdrawContent = WithdrawHelp()
    mainContent = MainHelp()
    moveContent = moveHelp()
    payContent = payHelp()
    balanceContent = balanceHelp()
    statementContent = statementHelp()
    deletewalletContent  = deletewalletHelp()

    update.message.reply_text(mainContent + depositContent + withdrawContent + moveContent + payContent + balanceContent + statementContent + deletewalletContent)


def MainHelp():
    return '**✳️ WELCOME TO CLOUDCOIN VAULT ✳️**\nThis bot allows you to deposit, withdraw, transfer, and pay out CloudCoins. This software is provided free of charge with all bugs, defects and vulnerabilities. \n\n**BASIC COMMANDS**'

def MainNFTHelp():
    return '**✳️ WELCOME TO CLOUDCOIN NFT VAULT ✳️**\nThis bot allows you to create, list and withdraw NFTs powered by CloudCoin. This software is provided free of charge with all bugs, defects and vulnerabilities included free from the CloudCoin Consoritum. \n\n**BASIC COMMANDS ➡️**'

def statementHelp():
    return '\n\n**🧾 STATEMENT**\n`/bank statement <page>` Returns records of transactions as a set of 10 records.\ne.g. /bank statement 1 returns first page of statement'

def balanceHelp():
    return '\n\n**🔎 BALANCE**\n`/bank balance` Returns the number of coins in  your Coin Bank.\nNo extra information is required.'

def deletewalletHelp():
    return '\n\n**🔎 DELETE COIN BANK **\n`/bank deletebank` Deletes your Coin Bank if it\'s empty.\nPlease withdraw all your coins before issuing this command.'

def payHelp():
    return "\n\n**❤️ PAY**\n`/bank pay` Places money from your Coin Bank into the bot's Coin Bank and tells the bot about the payment.\nRequires the number of coins to give the bot: `/bank pay 50` where 50 is the number of coins to give the bot. "
    
def moveHelp():
    return '\n\n**↔️ TRANSFER**\n`/bank transfer` Transfers coins from your Coin Bank to the Coin Bank of another person.\nRequires the number of coins to transfer and the name of the user that will receive them: `/bank transfer 10 larryG#3345` where 10 is the number of coins to transfer and larryG#3345 is the Discord user to receive the coins. They must have a Coin Bank on this bot to receive coins. '

def WithdrawHelp():
    return '\n\n**📤 WITHDRAW**\n`/bank withdraw` Removes coins from your Coin Bank.\nRequires the amount of coins to be removed: `/bank withdraw 33` where 33 is the number of coins to be removed.\nClick image. Open original and save the file.'

def DeleteWalletHelp():
    return '\n\n** 🚫 DELETE COIN BANK **\nDeletes the users Coin Bank.\n\tRequest:\n /deletebank\nReturns:\n\tWallet Deleted\nor\n\tYour Wallet Must Be Empty to be Deleted. Withdraw your Coins first.'

def ShowCoinsHelp():
    return '\n\n** 👀 SHOWCOINS **\nShows all the coins that are in the users wallet. This number includes coins in the Bank folder and in the Fracked folder.\n\tRequest:\n `/showcoins`\nReturns an integer something like:\n\t33'

def DepositHelp():
    return '\n\n** 📥 DEPOSIT**\n`/bank deposit` Creates a Coin Bank if one does not exist. Uploads a coin file into your Coin Bank.\n Files must have a .bin or .png file extension.  To upload coins to your Coin Bank, first type /bank deposit. Before you submit this command, click the “+” icon to the left of the text box and select a coin file to upload. Once your file is uploaded, submit the command.'

def NFTCreateHelp():
    return '\n\n** 🎨 CREATE**\n`/nft create title description\nThis bot allows you to create NFTs from your cloudcoins in CloudBank. You must have a non zero balance in your wallet to create an NFT. This will create a new NFT wallet for you on the server.\n\n '
    
def NFTsHOWHelp():
    return '\n\n**👀 SHOW**\n`/nft show Lists all the NFTs created by you in tabular format\n\n '
    
def NFTWithdrawHelp():
    return '\n\n**📤 WITHDRAW**\n`/nft withdraw withdraws an NFT and sends back the PNG by discord bot\n\n '
