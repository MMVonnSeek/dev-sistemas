from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from database import get_db
from models import Usuario

# Configuração
SECRET_KEY = "almoxarifado-chave-secreta-2026"
ALGORITHM = "HS256"
EXPIRE_MIN = 60   # token válido por 60 minutos

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Instrui o Swagger a exibir o cadeado nas rotas protegidas
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


# Funções de senha
# Transforma a senha em hash bcrypt para salvar no banco
def hash_senha(senha: str)-> str:
    return pwd_context.hash(senha)

# Compara a senha digitada com o hash do banco
def verificar_senha(senha: str, hash_salvo: str) -> bool:
    return pwd_context.verify(senha, hash_salvo)


# Funções do token
# Gera o JWT com o login do usuário e data de expiração
def criar_token(dados: dict)-> str:
    payload = dados.copy()
    expira = datetime.utcnow() + timedelta(minutes=EXPIRE_MIN)
    payload.update({"exp": expira})
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


# Dependência: usuário logado
# Vamos injetar essa função nos endpoints protegidos com Depends()
# Dependência: extrai e valida o token, retorna o usuário
def usuario_logado(
        token: str = Depends(oauth2_scheme),
        db: Session = Depends(get_db)
) -> Usuario:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        login = payload.get("sub")
        if not login:
            raise HTTPException(status_code=401, detail="Token inválido")
    
    except JWTError:
        raise HTTPException(status_code=401, detail="Token expirado ou inválido")
    
    usuario = db.query(Usuario).filter(Usuario.login == login).first()
    if not usuario:
        raise HTTPException(status_code=401, detail="Usuário não encontrado")
    return usuario