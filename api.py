import requests
TOKEN='tnFn41GZs8Fd'
METHOD='search/physical'
def search_phisycal(region,firstname,lastname,birthdate):
    METHOD='search/physical'
    url='https://api-ip.fssp.gov.ru/api/v1.0/{}'.format(METHOD)

    data={'region':region,'firstname':firstname, 'lastname':lastname, 'birthdate':birthdate}

    data['token']=TOKEN
    print (url)
    r=requests.get(url,data)
    print (r.json())
    #data['token']=TOKEN
    return r.json()['response']['task']
#

def get_status(task):
    METHOD='status'
    url='https://api-ip.fssp.gov.ru/api/v1.0/{}'.format(METHOD)

    data={'task':task}

    data['token']=TOKEN
    print (url)
    r=requests.get(url,data)
    print (r.json())
    return r.json()['response']['status']
#task=search_phisycal(region='9',firstname='Сергей', lastname='Шило', birthdate='15.06.1984')
def get_result(task):
    METHOD='result'
    url='https://api-ip.fssp.gov.ru/api/v1.0/{}'.format(METHOD)

    data={'task':task}

    data['token']=TOKEN
    print (url)
    r=requests.get(url,data)
    print (r.json())
    #sreturn r.json()['response']['status']
task=search_phisycal(region='16',firstname='Тимур', lastname='Галанин', birthdate='17.10.1998')
print (task)

status=get_status(task)
while get_status(task)>0:
    pass
get_result(task)

    #data['token']=TOKEN
    #return r.json()['response']['task']


# url='https://api-ip.fssp.gov.ru/api/v1.0/{}'.format(METHOD)
# data={'region':'9','firstname':'Шило', 'lastname':'Сергей', 'birthdate':'15.06.1984'}
# data['token']=TOKEN
# r=requests.get(url,data)
# print (r.json())
# task=r.json()['response']['task']
# print (task)
# task='ea22b38b-fd15-41ad-8233-9b0f24aa0fa3'
# METHOD='status'
# url='https://api-ip.fssp.gov.ru/api/v1.0/{}'.format(METHOD)
# data={'task':task}
# data['token']=TOKEN
# r=requests.get(url,data)
# print (r.json())

# task='ea22b38b-fd15-41ad-8233-9b0f24aa0fa3'
# METHOD='result'
# url='https://api-ip.fssp.gov.ru/api/v1.0/{}'.format(METHOD)
# data={'task':task}
# data['token']=TOKEN
# r=requests.get(url,data)
# print (r.json())
