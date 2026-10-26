import bcrypt
from jose import JWTError, jwt
from datetime import datetime, timedelta, timezone
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

SECRET_KEY = 'poder-ser-qualquer-mensgem'
ALGORITHM = 'HS256'
EXPIRA_MIN = 60

# Criar função criar_hash


# Criar função verificar_senha


# Criar função criar_token


# Criar função usuario_logado
