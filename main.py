# import pywhatkit as kit
import random
# import requests

messages = ["Hello", "Hi", "Heyy", "whatsup"]
timeHrs = random.randint(8,12)
timeMins = random.randint(0,59)

phone_number = "number"

message = random.choice(messages)
print(message)

# Send message with whatsapp
# kit.sendwhatmsg(phone_number, message, timeHrs, timeMins)

# Send SMS
# resp = requests.post('https://textbelt.com/text', {
#     'phone': phone_number,
#     'message': message,
#     'key': 'textbelt',
# })

# print(resp.json())