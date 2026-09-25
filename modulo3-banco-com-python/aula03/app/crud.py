from sqlalchemy.orm import Session
from app.models import Funcionario

def criar_funcionario(db: Session, nome: str, email: str, salario: float):
    # 1 Verificar se o email já existe
    existe = db.query(Funcionario).filter(
        Funcionario.email == email
    ).first()

    if existe:
        raise ValueError(f'E-mail {email} já cadastrado')

    # 2 Criar o objeto
    novo = Funcionario(nome=nome, email=email, salario=salario)

    # 3 Salvar no banco
    db.add(novo)
    db.commit()
    db.refresh(novo)  # busca o id pelo banco
    return novo

