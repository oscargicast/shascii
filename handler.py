import json

filepath = "message.json"

with open(filepath, 'r') as filename:
    msg = json.loads(filename.read())
    print msg['asci-art']
    print msg['welcome-message']
