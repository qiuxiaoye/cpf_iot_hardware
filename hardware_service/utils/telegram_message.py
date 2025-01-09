import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Telegram_Message:
    BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
    CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

    def send_ip_to_telegram(self, host_name, ip_address):
        """Send the IP address to a Telegram chat."""
        try:
            url = f"https://api.telegram.org/bot{self.BOT_TOKEN}/sendMessage"
            payload = {"chat_id": self.CHAT_ID, "text": f"Received Hardware Info - Hostname: {host_name}, IP Address: {ip_address}"}
            response = requests.post(url, json=payload)
            response.raise_for_status()
            print("IP address sent to Telegram successfully.")
        except requests.exceptions.RequestException as e:
            print(f"Failed to send IP to Telegram. Error: {e}")