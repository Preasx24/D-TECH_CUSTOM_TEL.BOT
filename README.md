Ah, I see what you're referring to now! You're talking about code blocks in markdown, which is often used in GitHub README files to make it easy to copy text. You can wrap text with triple backticks (```) to create these code blocks, which makes it easy to copy the commands.

Here’s the updated version with the correct formatting for easy copying on GitHub:


---

D-TECH CUSTOM TELEGRAM BOT

This repository contains the D-TECH Speed Test Bot for Telegram, allowing users to test their internet speed directly via Telegram commands. The bot tests the user's download speed, upload speed, and ping, and displays the results along with an estimated time to download a 1GB file.

Features:

🚀 Perform Speed Tests (Download, Upload, Ping)

📊 Display Detailed Results and recommendations based on speed



---

Installation

1. Clone the Repository

First, clone the repository using Git:

''' git clone https://github.com/Preasx24/D-TECH_CUSTOM_TEL.BOT.git
cd D-TECH_CUSTOM_TEL.BOT '''

2. Install Dependencies


' ' 'pip install python-telegram-bot speedtest-cli ' ' '

3. Get a Telegram Bot API Token

To use the bot, you'll need a Telegram bot API token. Follow these steps to get one:

1. Open Telegram and search for BotFather: https://t.me/BotFather.


2. Type /newbot and follow the instructions to create a new bot.


3. Copy the API token provided by BotFather.



The bot will save this token in a file called telegram_token.txt. If this file doesn't exist, you will be prompted to enter the token when you first run the bot.

4. Run the Script

After everything is set up, you can run the bot with the following command:

'''python D-TECH_bot.py'''

The bot will now be running and ready to respond to commands! 🎉


---

Commands

/start

Displays a welcome message.

/speedtest

Initiates the internet speed test and measures:

📥 Download Speed

📤 Upload Speed

⏱️ Ping Latency


Once the test is complete, the bot displays:

Test Results

Recommendations based on speed



---

Now, when users view this on GitHub, they will be able to easily copy commands and code because of the proper code block formatting.

