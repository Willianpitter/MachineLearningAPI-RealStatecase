from fastapi.security.api_key import APIKeyHeader, APIKey
from fastapi import Security, Depends
from fastapi import FastAPI, HTTPException


def get_api_key(api_key_header: str = Security(api_key_header)):
    if api_key_header == API_KEY:
        return api_key_header
    else:
        raise HTTPException(status_code=403, detail="Could not validate credentials")
