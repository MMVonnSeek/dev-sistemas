from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class LivroCreate(BaseModel):
    titulo: str = Field(..., min_length=2, max_length=200)
    autor: str = Field(..., min_length=2, max_length=150)
    ano_publicacao: Optional[int] = None

class LivroPatch(BaseModel):
    titulo: Optional[str] = Field(None, min_length=2, max_length=200)
    autor: Optional[str] = Field(None, min_length=2, max_length=150)
    ano_publicacao: Optional[int] = None
    disponivel: Optional[bool] = None

class LivroResponse(BaseModel):
    id: int
    titulo: str
    autor: str
    ano_publicacao: Optional[int]
    disponivel: bool
    criado_em: datetime
    class Config:
        from_attributes = True