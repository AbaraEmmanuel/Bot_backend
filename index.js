const express = require('express');
const { TelegramBot } = require('telegram-bot-api');
require('dotenv').config();

const app = express();
const port = process.env.PORT || 3000;

// Initialize the Telegram bot
const bot = new TelegramBot({
  token: process.env.TELEGRAM_BOT_TOKEN,
  updates: {
    enabled: true
  }
});

// Define a basic route
app.get('/', (req, res) => {
  res.send('Telegram Bot Backend is running!');
});

// Start the Express server
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});

// Handle Telegram updates
bot.on('message', (message) => {
  console.log('Received message:', message);
  // Your message handling logic here
});
