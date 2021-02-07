import requests
from bs4 import BeautifulSoup as bs
from ojworkings.ojUtils import formToPayload


def uvaLogin(cliente):
    """Login to uva with provided cliente"""
    # Basic OJ info
    url = "https://onlinejudge.org/index.php?option=com_comprofiler&task=login"
    userid = 'username'
    passid = 'passwd'
    formIdName = 'id'
    formIdValue = 'mod_loginform'
    # Take username and password as input
    username = ""
    password = ""
    if(username == "" and password == ""):
        username = "sagor32"
        password = "bolajabe9"

    #prepares payload for login
    rrs = cliente.get(url)
    payload = formToPayload(rrs,formIdName,formIdValue)
    payload[userid] = username
    payload[passid] = password

    # Logging in
    rrs = cliente.post(url,data=payload)

    if rrs.url == "https://onlinejudge.org/":
        print("Loggin to uva online judge successful")
    else:
        print("Failed to login to uva online judge")

    return rrs


def uvaSubmit(cliente,problemId,langId,solutionCode):
    """Submits the solution to uva"""
    url = "https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=25"
    formIdName = 'action'
    formIdValue = 'index.php?option=com_onlinejudge&Itemid=25&page=save_submission'

    rrs = cliente.get(url)
    payload = formToPayload(rrs,formIdName,formIdValue)

    payload['localid'] = problemId
    payload['language'] = langId
    payload['code'] = solutionCode

    submitUrl = 'https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=25&page=save_submission'
    rrs = cliente.post(submitUrl, data=payload)
    return rrs


def problistSerializer(pageCode):
    """Serialize problemlist page"""
    problist = []
    soup = bs(pageCode,'html.parser')
    tr1 = soup.find_all(name='tr',attrs={'class':'sectiontableentry1'})
    tr2 = soup.find_all(name='tr',attrs={'class':'sectiontableentry2'})
    for tr in tr1:
        tr = tr.contents[5].get_text().split('\xa0')
        problist.append({
            'prob-id' : tr[0],
            'prob-title' : tr[2],
            'oj' : 'UVA'
        })
    for tr in tr2:
        tr = tr.contents[5].get_text().split('\xa0')
        problist.append({
            'prob-id' : tr[0],
            'prob-title' : tr[2],
            'oj' : 'UVA'
        })
    return problist


def getProblist(cliente,pageNo):
    """Fetch problist from uri website"""
    url = "https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category="+str(pageNo)
    rrs = cliente.get(url)
    problist = problistSerializer(rrs.content)
    return problist


def main():
    """Main workings of the file"""
    cliente = requests.session()
    uvaLogin(cliente)
    code = '''#include<stdio.h>
int main()
{
    int v,t,s;
    while(scanf("%d %d",&v,&t)!=EOF)
    {
        s=(v*t*2);
        printf("%d\\n",s);
    }
    return 0;
}
'''
    uvaSubmit(cliente,'10071','1',code)


# main()
