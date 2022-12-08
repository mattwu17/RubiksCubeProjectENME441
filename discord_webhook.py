# Use HTTP POST to create a webhook to send a message
# to a Discord channel

# Here we just want to send a simple POST request to a
# fixed target IP, without managing the entire HTTP 
# communication process as with sockets.  To do this we
# can use the Python requests module

from machine import Pin
from time import sleep
import time
import urequests as requests
import ujson

p_in = Pin(25, Pin.IN) 

# On Discord, do the following:
# 1. create a channel
# 2. create a webhook for the channel (select channel -> gear icon
#     -> Integrations -> Webhooks)
# 3. get the URL for the webhook, it should look something like this:
url = 'https://discord.com/api/webhooks/1050207959877173259/Hp0566Gnidx8v1-9dSXn4xsRgxqKBlreVBodWSqE_PDK1j7djOQ_c4fl6egrvbKgQfoq'

while True:
    # For Discord webhook formatting see:
    # https://discord.com/developers/docs/resources/webhook
    # (scroll down to "Execute Webhook" section). At a minimum
    # a "content" field is required. We can also override the
    # default webhook user by adding a "username" field:
#     data = {'name': 'TempName',
#         'content' : '5'}
#     data_json = ujson.dump(data)
#     print(data_json)
    t = time.localtime()
    #(year, month, mday, hour, minute, second, weekday, yearday)
    month_mapping = {1:"jan", 2:"feb", 3:"mar", 4:"apr", 5:"may", 6:"jun", 7:"jul", 8:"aug", 9:"spet", 10:"oct", 11:'nov', 12:"dec"}

    def append(day):
        if day == 1:
            return 'st'
        elif day == 2:
            return 'nd'
        elif day == 3:
            return 'rd'
        else:
            return 'th'
    pretty_str = f"current time: {t[3]}:{t[4]}:{t[5]} {month_mapping[t[1]]} {t[2]}{append(t[2])} {t[0]}"
    data = ujson.dumps(
        {'content' : pretty_str,
         'username': "ENME441 bot"})
    result = requests.post(url, headers = {'Content-type': 'application/json'}, data=data)  # send the POST request
    print(result.text)                      # and print the response
    sleep(10)




