from fastapi import FastAPI

app = FastAPI(
    title="LogFarma API",
    description="API para gerenciamento de uma distribuidora farmacêutica.",
    version="1.0.0",
    docs_url="/docs", 
    redoc_url="/redoc",  
    contact={
        "name": "Equipe LogFarma",
        "email": "contato@logfarma.com",
    },
    license_info={
        "name": "MIT",
    },
)

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API LogFarma!"}
