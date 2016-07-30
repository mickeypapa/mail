# -*- coding:utf-8 -*-
# Created on 07/27/2016
# By Peter Chen
# coding=utf-8

import json
import requests
import sys


class wechat_alarm():
    def __init__(self):
        variable = {}
        variable['corpid'] = 'wxa352d7a82071cac7'
        variable['corpsecret'] = 'v7KbSF_ODfwBXTDpFUPRbtXNgoYHVlzK0PAzZPr0cHxumi87DplSb8upXBuixP1c'
        r = requests.get('https://qyapi.weixin.qq.com/cgi-bin/gettoken?', params=variable)
        print('Accessing %s ' % r.url)
        js = r.json()

        if 'errcode' not in js:
            print('Access token %s ' % js)
            self.access_token = js.get('access_token')
            self.expires_in = js.get('expires_in')
        else:
            print('Can not get the access token')
            print(json)
            sys.exit(2)

    def get_access_token(self):
        variable = {}
        variable['corpid'] = 'wxa352d7a82071cac7'
        variable['corpsecret'] = 'v7KbSF_ODfwBXTDpFUPRbtXNgoYHVlzK0PAzZPr0cHxumi87DplSb8upXBuixP1c'
        r = requests.get('https://qyapi.weixin.qq.com/cgi-bin/gettoken?', params=variable)
        print('Accessing %s ' % r.url)
        return r.json()

    def init_text(self, content):
        content = content
        print(content)
        send_content ={
            "touser": "@all",
            "toparty": "",
            "totag": "",
            "msgtype": "text",
            "agentid": "2",
            "text": {
                "content": content
            },
            "safe": "0"
            }
        return send_content

    def send_alarm_wechat(self, msg):
        text = self.init_text(msg)
        headers = {'Content-Type': 'application/json', "encoding": "utf-8"}
        print(text)
        r = requests.post('https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=%s' % self.access_token,
                          data=json.dumps(text, ensure_ascii=False).encode('utf-8'), headers=headers)
        result = r.json()
        print(result)


