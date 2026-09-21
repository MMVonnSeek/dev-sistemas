class Curso(Base):
    __tablename__ = ''
    id      = Column(Integer, primary_key=True, =True)
    nome    = Column(String(), nullable=)
    duracao = Column(, nullable=False)
    ativo   = Column(Boolean, default=)
    def __repr__(self): 
        return f'<Curso id={self.} nome={self.nome}>'

class Aluno(Base):
    __tablename__ = ''
    id        = Column(Integer, primary_key=True, autoincrement=True)
    nome      = Column(String(150), nullable=)
    email     = Column(String(100), nullable=False, =True)
    matricula = Column(String(),  nullable=False, unique=True)
    ativo     = Column(, default=True)
    def __repr__(self): 
        return f'<Aluno id={self.id} nome={self.}>'
