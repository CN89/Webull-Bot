import requests
import json

#Retrieve discord messages
def retrieve_messages(channelid):
    headers = {
        'authorization': 'MTE2ODYyMDg1NTk3OTQyMTcyNg.GpqiPA.5K_89LLkybPSVwB4muCWxLNaXyIoqt7q84_6uo'
    }
    r = requests.get(f'https://discord.com/api/v9/channels/{channelid}/messages', headers=headers)
    jsonn = json.loads(r.text)
    for value in jsonn:

        lines = []

        text = str(value['content'])
        
        index = "spy"
        trim = "TP"
        out = "out"
        
        if index in text:
            lines.append(text)
        if trim in text:
            lines.append(text)
        if out in text:
            lines.append(text)

    return lines



