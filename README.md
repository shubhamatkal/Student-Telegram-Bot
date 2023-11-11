# IITM-BS Bots for staying up to date with all the events and deadlines

Welcome to the IIT Madras-BS Uodates Bot repository ! This repository contains two folders: one for a WhatsApp bot and another for a Telegram bot. These bots are designed to provide details about today's live sessions and schedules specifically tailored for students

google docs for getting information about ongoing updates in this repo
https://docs.google.com/document/d/1yjr_NXChKjF3HIbJfOVPO2BQ8AqG9RMoNGmtE4Ih1C0/edit?usp=sharing
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
