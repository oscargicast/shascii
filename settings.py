import json
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_FILE = os.path.join(BASE_DIR, "message.json")


with open(CONFIG_FILE, 'r') as filename:
    content = json.loads(filename.read())

    ASCII_FILE = os.path.join(
        os.path.join(BASE_DIR, "ascii"), content.get("asci-art")
    )
    WELCOME_MESSAGE = content.get("welcome-message")
    RANDOM_MESSAGES = content.get("random-messages")
