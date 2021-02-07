import requests
from bs4 import BeautifulSoup as bs

from ojworkings.ojUtils import formToPayload


def uriLogin(cliente):
    """Login to uri with provided cliente"""
    # Basic OJ into
    url = "https://www.urionlinejudge.com.br/judge/en/login"
    userid = 'email'
    passid = 'password'
    formIdName = 'method'
    formIdValue = 'post'
    # Take username and password as input
    username = ""
    password = ""
    if(username == "" and password == ""):
        username = "jocelyn69@freadingsq.com"
        password = "bitelane"

    #prepares payload for login
    rrs = cliente.get(url)
    payload = formToPayload(rrs,formIdName,formIdValue)
    payload[userid] = username
    payload[passid] = password

    # Logging in
    rrs = cliente.post(url,data=payload)

    if rrs.url == "https://www.urionlinejudge.com.br/judge/en/":
        print("Loggin to uri successful")
    else:
        print("Failed to login to uri")

    return rrs


def uriSubmit(cliente,problemId,langId,solutionCode):
    """Submits the solution to uva"""
    url = "https://www.urionlinejudge.com.br/judge/en/runs/add"
    formIdName = 'action'
    formIdValue = '/judge/en/runs/add'

    rrs = cliente.get(url)
    payload = formToPayload(rrs,formIdName,formIdValue)

    payload['problem_id'] = problemId
    payload['language_id'] = langId
    payload['source_code'] = solutionCode

    submitUrl = 'https://www.urionlinejudge.com.br/judge/en/runs/add'
    rrs = cliente.post(submitUrl, data=payload)
    return rrs


def testSubmit():
    """test submit function"""
    cliente =  requests.session()
    uriLogin(cliente)
    code = '''#include<bits/stdc++.h>
using namespace std;

int main(){
    cout<<"Hello World!"<<endl;
    return 0;
}
'''
    uriSubmit(cliente,'1000','16',code)


def problistSerializer(pageCode):
    """Serialize problemlist page"""
    problist = []
    soup = bs(pageCode,'html.parser')
    tbody = soup.body.table.tbody
    for tr in tbody.children:
        if type(tr)==type(tbody):
            problist.append({
                'prob-id' : tr.contents[1].get_text().strip(),
                'prob-title' : tr.contents[5].get_text().strip(),
                'oj' : 'URI'
            })
    return problist


def testProblistSerializer():
    """tests problistSerializer"""
    with open('Problems - URI Online Judge.html') as fp:
        problist = problistSerializer(fp)
    for prob in problist:
        print(prob)


def getProblist(cliente,pageNo):
    """Fetch problist from uri website"""
    url = "https://www.urionlinejudge.com.br/judge/en/problems/all?page="+str(pageNo)
    rrs = cliente.get(url)
    problist = problistSerializer(rrs.content)
    return problist


def testgetProblist():
    """tests getProblist method"""
    cliente = requests.session()
    uriLogin(cliente)
    problist = getProblist(cliente,5)
    for prob in problist:
        print(prob)


def main():
    """main workings of the file"""



# main()
