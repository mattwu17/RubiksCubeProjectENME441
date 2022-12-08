import requests
import json
import sys
def get_message(ch_id):
    headers = {
        "authorization" : 'MjM1OTc5MjEwMDA5NzM5MjY0.G1ysAJ.RiSKyvpXNPt7Dm3kR7o_oXS6Hz7N0nWrEg8BpU'
    }
    # esp32 ch_id = 1050175218246762546
    r = requests.get(f'https://discord.com/api/v9/channels/{ch_id}/messages', headers= headers)

    parse_json = json.loads(r.text)
    if len(parse_json) == 2:
        print(f"Error!!! Exited with KeyError:{parse_json['code']}")
        sys.exit()
    print(parse_json[0]['content'])


get_message('1050175218246762546')