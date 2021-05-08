from fastapi import FastAPI, Form
from db import query_email, is_token_valid, generate_token, invalidate_token  # Not provided
from sender import send_otp  # Not provided


app = FastAPI(docs_url=None, redoc_url=None)


@app.get('/sendtoken/{email}')
async def send_OTP(email: str):
    if query_email(email):
        if not send_otp(generate_token(email), email):
            return { 'status': False }
    return { 'status': True }


@app.get('/verify/{token}')
async def verify_OTP(token: str):
    if not is_token_valid(token):
        return { 'status': False }
    invalidate_token(token)
    return { 'status': True }
