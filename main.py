import pywhatkit as kit
import random

messages = ["Hello", "Hi", "Heyy", "whatsup"]
timeHrs = random.randint(8,12)
timeMins = random.randint(0,59)

message = random.choice(messages)
print(message)

kit.sendwhatmsg("+14632748077", message, timeHrs, timeMins)