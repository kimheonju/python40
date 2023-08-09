import requests
import json

slack_webhook_url = 'https://hooks.slack.com/services/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'

def sendSlackWebhook(strText):
    headers= {
        "Content-type": "application/json"
    }
    
    data = {
        "text": strText
    }
    
    res = requests.post(slack_webhook_url, headers=headers, data=json.dumps(data))
    
    if res.status_code == 200:
        if res.status_code == 200:
            return "ok"
        else:
            return "error"
        
print(sendSlackWebhook("안녕하세요 파이썬에서 보내는 메시지 입니다."))