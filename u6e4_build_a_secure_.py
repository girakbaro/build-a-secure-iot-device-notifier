Python
import random
import string
import json
import requests
import hashlib
import hmac
import time
from typing import Dict

# Configuration
DEVICE_ID = "U6E4_DEVICE_001"
API_KEY = "YOUR_API_KEY"
API_SECRET = "YOUR_API_SECRET"
NOTIFICATION_URL = "https://api.example.com/notifications"

# IoT Device Notifier class
class IoTDeviceNotifier:
    def __init__(self, device_id: str, api_key: str, api_secret: str):
        self.device_id = device_id
        self.api_key = api_key
        self.api_secret = api_secret

    def generate_signature(self, message: str) -> str:
        signature = hmac.new(self.api_secret.encode(), message.encode(), hashlib.sha256).hexdigest()
        return signature

    def send_notification(self, message: str) -> bool:
        signature = self.generate_signature(message)
        headers = {
            "X-API-KEY": self.api_key,
            "X-SIGNATURE": signature,
            "Content-Type": "application/json"
        }
        data = {"device_id": self.device_id, "message": message}
        response = requests.post(NOTIFICATION_URL, headers=headers, json=data)
        return response.status_code == 200

# Test case
def test_iot_device_notifier():
    device_notifier = IoTDeviceNotifier(DEVICE_ID, API_KEY, API_SECRET)
    message = f"Hello from {DEVICE_ID} at {int(time.time())}!"
    print(f"Sending notification: {message}")
    if device_notifier.send_notification(message):
        print("Notification sent successfully!")
    else:
        print("Failed to send notification!")

if __name__ == "__main__":
    test_iot_device_notifier()