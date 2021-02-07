import requests
from bs4 import BeautifulSoup as bs


def formToPayload(rrs,formIdName,formIdValue):
    """Returns form with formId of rrs response as payload dict"""
    # Requires requests and BeautifulSoup

    html = bs(rrs.content,features="html.parser")
    forms = html.body.findChildren('form')
    payload = {}
    for form in forms :
        if formIdName in form.attrs and form[formIdName]==formIdValue:
            if 'action' in form.attrs:
                actionUrl = form['action']
            for input in form.findAll('input'):
                name = " "
                value = " "
                if 'name' in input.attrs:
                    name = input['name']
                if 'value' in input.attrs:
                    value = input['value']
                payload[name] = value
            return payload


def login(client,url,userid,passid,formIdName,formIdValue,username,password):
    """Login with specified settings"""
    rrs = client.get(url)

    # creates payload
    payload = formToPayload(rrs,formIdName,formIdValue)

    payload[userid] = username
    payload[passid] = password

    #logging in
    rrs = client.post(url,data=payload)
    return rrs


def showDict(data):
    for (k,v) in data.items():
        print(k,'<--->',v)
