from __future__ import annotations

import uuid
from datetime import datetime, timedelta, timezone

from jose import jwt, JWTError, ExpiredSignatureError
from passlib.context import CryptContext

from app.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password:str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password:str, password:str) -> bool :
    return pwd_context.verify(plain_password, password)


# -----------------------------
# Token exceptions
# -----------------------------

class TokenError(Exception):
    """Base Token Exception"""

class InvalidTokenError(TokenError):
    pass

class ExpiredTokenError(TokenError):
    pass

# -----------------------------
# JWT helpers
# -----------------------------

def _utcnow():
    return datetime.now(timezone.utc)


def create_access(sub:str, expires_delta:timedelta|None = None):
    now = _utcnow()

    expire = now + (expires_delta or timedelta(minutes=settings.ACCESS_TOKEN_EXPIRES_MINUTES))
    payload = {
        "sub":str(sub),
        "iat":int(now.timestamp()),
        "exp":int(expire.timestamp()),
        "iss":settings.TOKEN_ISSUER,
        "aud":settings.TOKEN_AUDIENCE,
        "type":"access",
        "jti":str(uuid.uuid4()),
    }

    return jwt.encode(payload, settings.SECRET_KEY, algorithm=settings.ALGORITHM)


def decode_access_token(token:str) -> dict:

    """
    Decode and validate JWT access token.
    """

    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM],
            audience=settings.TOKEN_AUDIENCE,
            issuer=settings.TOKEN_ISSUER,
            options={
                "require_exp": True,
                "require_iat": True,
                "require_sub": True,
            },
        )
    except ExpiredSignatureError as e:
        raise ExpiredTokenError("Token Expired") from e

    except JWTError as e:
        raise InvalidTokenError("Invalid Token") from e


    if payload.get("type") != "access":
        raise InvalidTokenError("Wrong Token Type")

    if "jti" not in payload:
        raise InvalidTokenError("Missing Token id")


def get_user_id_from_token(token:str):
    """
    Extract user_id from token
    """

    payload = decode_access_token(token)
    try:
        return int(payload["sub"])
    except (KeyError, ValueError) as e:
        raise InvalidTokenError("Invalid subject in token") from e
    

