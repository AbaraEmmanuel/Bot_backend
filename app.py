from flask import Flask, request
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

app = Flask(__name__)

TOKEN = "YOUR_BOT_TOKEN"
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Define start command handler
def start(update: Update, context: CallbackContext):
    user = update.message.from_user
    username = user.username or "Username"
    user_id = user.id

    # Initialize user data
    # Save user data to database or in-memory storage

    update.message.reply_text(f"Hello, {username}! Welcome to the bot.")

# Register handlers
dispatcher.add_handler(CommandHandler("start", start))

# Define webhook route
@app.route('/webhook', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(), updater.bot)
    dispatcher.process_update(update)
    return 'ok'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
