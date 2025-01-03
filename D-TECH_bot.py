import logging
import speedtest
import time
import os

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# Function to get the Telegram bot API token
def get_api_token():
    token_file = "telegram_token.txt"
    
    # Check if the token is already saved
    if not os.path.exists(token_file):
        print("🚨 Please enter your Telegram bot API token:")
        api_token = input("API Token: ").strip()
        
        # Save the token to a file for future use
        with open(token_file, "w") as f:
            f.write(api_token)
    else:
        # Read the token from the file if it already exists
        with open(token_file, "r") as f:
            api_token = f.read().strip()
    
    return api_token

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Get Telegram API token
API_TOKEN = get_api_token()

# Inline Buttons for the Welcome Message
def create_buttons():
    return [
        [InlineKeyboardButton("🌹 Admin 🌹", url="https://t.me/PREASX24")],
        [InlineKeyboardButton("🔥 YouTube Channel 🔥", url="https://youtube.com/@d-tech_services?si=iBJd3458kYtgVFsJ")],
        [InlineKeyboardButton("💌 Telegram Channel 💌", url="https://t.me/DTECHXPORT")],
        [InlineKeyboardButton("🌟 TikTok Channel 🌟", url="https://vm.tiktok.com/ZMhPpSEV4/")]
    ]

# Welcome Message with Inline Buttons
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    start_text = """
🌹 **Welcome to D-TECH Speed Tester!** 🌹

🔥 We're here to optimize your connection and give you instant feedback on:

📥 **Download Speed**  
📤 **Upload Speed**  
⏱️ **Ping Latency**

💌 Use `/speedtest` now to test your internet speed and stay ahead!

🌟 **Powered by D-TECH Services** 🌟  
Stay fast. Stay connected.
"""
    buttons = create_buttons()
    reply_markup = InlineKeyboardMarkup(buttons)
    await update.message.reply_text(start_text, reply_markup=reply_markup)

# Speed Test Function
async def speed_test(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Send initial loading message
    loading_message = await update.message.reply_text("🌟 Initializing the speed test... Please wait!")

    # Progress bar steps
    progress_steps = [
        "[▱▱▱▱▱▱▱▱▱▱] 0% - Starting...",
        "[▰▱▱▱▱▱▱▱▱▱] 10% - Connecting to the server...",
        "[▰▰▱▱▱▱▱▱▱▱] 30% - Testing download speed...",
        "[▰▰▰▰▱▱▱▱▱▱] 50% - Testing upload speed...",
        "[▰▰▰▰▰▰▱▱▱▱] 70% - Calculating ping...",
        "[▰▰▰▰▰▰▰▱▱▱] 90% - Finalizing results...",
        "[▰▰▰▰▰▰▰▰▰▰] 100% - Done!"
    ]

    # Perform the speed test in a separate thread to monitor its progress
    test_completed = False

    def perform_test():
        nonlocal test_completed
        st.get_best_server()
        st.download()
        st.upload()
        test_completed = True

    st = speedtest.Speedtest()
    import threading
    thread = threading.Thread(target=perform_test)
    thread.start()

    # Simulate the progress bar taking 30 seconds, or completing early if the test finishes
    for step in progress_steps:
        if test_completed:
            break
        await loading_message.edit_text(f"🌟 {step}")
        time.sleep(30 / len(progress_steps))  # Spread updates across 30 seconds

    # Wait for the thread to finish if it hasn't already
    thread.join()

    # Retrieve the results
    download_speed = st.results.download / 1_000_000  # Convert to Mbps
    upload_speed = st.results.upload / 1_000_000      # Convert to Mbps
    ping = st.results.ping

    # Calculate estimated download time for a 1GB file
    download_time_seconds = (8_000 / download_speed)  # 1GB = 8,000 megabits
    if download_time_seconds > 3600:
        download_time = f"{download_time_seconds / 3600:.2f} hours"
    elif download_time_seconds > 60:
        download_time = f"{download_time_seconds / 60:.2f} minutes"
    else:
        download_time = f"{download_time_seconds:.2f} seconds"
    
    # Ping stability (using thresholds for stability description)
    if ping <= 50:
        ping_status = "✅ Stable Ping"
    elif ping <= 100:
        ping_status = "⚠️ Moderate Ping"
    else:
        ping_status = "🚨 High Latency"

    # Message Reaction (based on speeds)
    if download_speed > 50:
        speed_reaction = "🌟 **Your internet speed is excellent!** 🌟"
    else:
        speed_reaction = "⚠️ **Your internet speed is below average.** ⚠️"
    
    # Result Text
    test_time = time.strftime('%Y-%m-%d at %H:%M')  # Current time
    result_text = f"""
🔥🔥🔥 **D-TECH Speed Test Results** 🔥🔥🔥
==============================

📥 **Download Speed:** {download_speed:.2f} Mbps  
📤 **Upload Speed:** {upload_speed:.2f} Mbps  
⏱️ **Ping:** {ping:.2f} ms  
🌐 **Ping Stability:** {ping_status}

📅 **Test Performed On:** {test_time}  
==============================

🕒 **Estimated Time to Download 1GB:** {download_time}  
==============================

{speed_reaction}  
Tested using **🌹 D-TECH Speed Tester 🌹**  
🔥 Stay connected, stay fast! 🔥
"""
    await loading_message.edit_text(result_text)

# Main Function to handle commands
def main():
    # Create an Application object and pass it your bot's token
    application = Application.builder().token(API_TOKEN).build()

    # Command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("speedtest", speed_test))

    # Start the bot
    application.run_polling()

if __name__ == '__main__':
    main()
