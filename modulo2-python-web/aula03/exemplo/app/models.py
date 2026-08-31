from pydantic import BaseModel, field_validator
from typing import Optional
from enum import Enum

# Enum: Define os valores aceitos para o campo cargo
# Aparece como dropdown no swagger automaticamente
class CargoEnum(str, Enum):
    dev = 'Dev'
    design = 'Designer'
    qa = 'QA'
    product_manager = 'Product Manager'

# Schema de entrada: o que o cliente envia (SEM id)
class UsuarioEntrada (BaseModel):
    nome: str
    email: str
    cargo: str
    ativo: bool = True
    salario: Optional[float] = None

    @field_validator('nome')
    @classmethod
    def validar_nome(cls, valor: str) -> str:
        valor = valor.strip()
        if len(valor) < 3:
            raise ValueError('Mínimo 3 caracteres')
        return valor.title()

# Schema de saída: o que o servidor retorna (COM id)
class UsuarioSaida(BaseModel):
    id: int
    nome: str
    email: str
    cargo: CargoEnum
    ativo: bool
    salario: Optional [float] = None

