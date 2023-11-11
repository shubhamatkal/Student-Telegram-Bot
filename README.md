# IITM-BS Live Session Tracker

Welcome to the IIT Madras - Biological Sciences Live Session Tracker! This repository contains two folders: one for a WhatsApp bot and another for a Telegram bot. These bots are designed to provide details about today's live sessions and schedules specifically tailored for students in the Biological Sciences program at IIT Madras.

## Features

- **WhatsApp Bot:**
  - Retrieves today's live session details.
  - Provides the schedule for the day.
  - User-friendly interaction through WhatsApp.

- **Telegram Bot:**
  - Fetches information on live sessions happening today.
  - Displays the daily schedule.
  - Seamless interaction within the Telegram platform.

## Getting Started

To use these bots, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/iitm-bs-live-session-tracker.git
   cd iitm-bs-live-session-tracker
   ```

2. **Set Up Bot Credentials:**
   - For the WhatsApp bot, provide your Twilio credentials.
   - For the Telegram bot, obtain your Telegram Bot Token.

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Bots:**
   - Start the WhatsApp bot:
     ```bash
     cd WhatsApp\ bot
     python main.py
     ```
   - Start the Telegram bot:
     ```bash
     cd Telegram\ bot
     python main.py
     ```

## Configuration

### WhatsApp Bot
1. Open `WhatsApp bot/config.py`.
2. Enter your Twilio Account SID, Auth Token, and WhatsApp Sandbox number.

### Telegram Bot
1. Open `Telegram bot/config.py`.
2. Replace `"YOUR_TELEGRAM_BOT_TOKEN"` with your actual Telegram Bot Token.

## Usage

- **WhatsApp Bot:**
  - Send a message to the Twilio WhatsApp Sandbox number with the keyword "sessions" or "schedule."

- **Telegram Bot:**
  - Start a chat with the Telegram bot and use the commands `/sessions` or `/schedule`.

## Contributing

We welcome contributions! If you have any suggestions, improvements, or bug fixes, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to customize this README according to the specific details and intricacies of your project. Good luck with your live session tracker for IITM BS students!