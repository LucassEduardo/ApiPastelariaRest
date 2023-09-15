from fastapi import FastAPI
from settings import HOST, PORT, RELOAD

# import das classes com as rotas/endpoints
from mod_funcionario import funcionarioDAO
from mod_cliente import clienteDAO
from mod_produto import produtoDAO

app = FastAPI()

# mapeamento das rotas/endpoints
app.include_router(funcionarioDAO.router)
app.include_router(clienteDAO.router)
app.include_router(produtoDAO.router)

import db
db.criaTabelas()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run('apiPastelaria:app', host=HOST, port=int(PORT), reload=RELOAD)

# rota padrão
@app.get("/")
def root():
    return {"detail":"API Pastelaria", "Swagger UI": "http://127.0.0.1:8000/docs", "ReDoc": "http://127.0.0.1:8000/redoc" }