import requests

from fastapi import FastAPI, Form
from os import getenv

OTP_SERVER = getenv('OTP_SERVER', default='localhost')
FLAG = getenv('FLAG', default='Cyberthon{PLACEHOLDER_FLAG}')

app = FastAPI(docs_url=None, redoc_url=None)


@app.post('/request')
async def request_OTP(email: str = Form(...)):
    r = requests.get(f'http://{OTP_SERVER}/sendtoken/{email}')
    result = r.json()['status']

    if result:
        return {
            'status': True,
            'message': 'Request success! OTP will be sent if provided email is present in our database.'
        }

    return {
        'status': False,
        'message': 'Failed to request OTP!'
    }


@app.post('/verify')
async def authenticate(token: str = Form(...)):
    r = requests.get(f'http://{OTP_SERVER}/verify/{token}')
    result = r.json()['status']

    if result:
        return {
            'status': True,
            'message': FLAG
        }

    return {
        'status': False,
        'message': 'Invalid Token!'
    }
