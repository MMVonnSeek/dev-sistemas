from pydantic import BaseModel, Field, EmailStr, field_validator
from typing import Optional
from datetime import datetime


# 1. Contém senha pois o usuário precisa enviar para se cadastrar.
# NÃO contém id nem criado_em / o banco gera automaticamente.
class UsuarioCreate(BaseModel):
    nome:  str = Field(
        ...,
        min_length=2,
        max_length=100,
        description='Nome completo do usuário'
    )
    email: EmailStr = Field(
        ...,
        description='E-mail válido — será usado no login'
    )
    senha: str = Field(
        ...,
        min_length=8,
        description='Mínimo 8 caracteres'
    )

    # @field_validator valida o campo 'nome' antes de salvar
    # Se a validação falhar: raise ValueError com a mensagem de erro
    # Se passar: return v (o valor validado)
    @field_validator('nome')
    @classmethod
    def nome_sem_numeros(cls, valor: str) -> str:
        if any(char.isdigit() for char in valor):
            raise ValueError('Nome não pode conter números')
        if not valor.strip():
            raise ValueError('Nome não pode ser só espaços')
        return valor.strip()  # remove espaços extras das bordas

    @field_validator('senha')
    @classmethod
    def senha_deve_ter_letra_e_numero(cls, valor: str) -> str:
        tem_letra  = any(c.isalpha()  for c in valor)
        tem_numero = any(c.isdigit()  for c in valor)
        if not tem_letra or not tem_numero:
            raise ValueError('Senha deve conter letras e números')
        return valor


# 2. Schema de ATUALIZAÇÃO PARCIAL (PATCH)
# Todos os campos são opcionais — o usuário envia só o que mudou.
# Não inclui senha — troca de senha seria um endpoint separado.
class UsuarioPatch(BaseModel):
    nome:  Optional[str] = Field(None, min_length=2, max_length=100)
    email: Optional[EmailStr] = None

    @field_validator('nome')
    @classmethod
    def nome_sem_numeros(cls, valor):
        if valor and any(char.isdigit() for char in valor):
            raise ValueError('Nome não pode conter números')
        return valor.strip() if valor else valor


# 3. UsuarioResponse - RESPOSTA (o que a API retorna)
class UsuarioResponse(BaseModel):
    id: int
    nome: str
    email: str
    ativo: bool
    criado_em: datetime

    class Config:
        from_attributes = True

class ErroResponse(BaseModel):
    erro: str
    detalhe: Optional[str] = None