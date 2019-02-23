import requests
from bs4 import BeautifulSoup 
import os

PWD = os.environ['PWD']

def lersite():
    headers = {
    
        'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36'

    }
    login_data = {
        'username': 'admin',
        'password': PWD,
    }

    url = 'http://127.0.0.1:8000/admin/login/?next=/admin/'

    session_requests = requests.Session()

    result = session_requests.get(url)
    soup = BeautifulSoup(result.content, 'html5lib')
    csr = soup.find('input', attrs={'name':'csrfmiddlewaretoken'})['value']
    login_data['csrfmiddlewaretoken'] = csr
    result = session_requests.post(
        url, 
        data=login_data, 
        headers=headers
    )
    print(BeautifulSoup(result.content, 'html5lib'))

lersite()