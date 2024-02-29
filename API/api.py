from fastapi import FastAPI
from datetime import datetime
import uvicorn
import fastapi

app = FastAPI()

# Rota para obter a data e hora atuais
@app.get("/data-hora")
def obter_data_hora():
    data_hora_atual = datetime.now()
    return {"data_hora_atual": data_hora_atual}

# Rota para obter informações sobre o servidor
@app.get("/info-servidor")
def obter_info_servidor():
    return {"mensagem": "API em execução", "versao_fastapi": fastapi.__version__}

# Rota para saudar o usuário
@app.get("/saudacao/{nome}")
def saudacao(nome: str):
    return {"mensagem": f"Olá, {nome}! Bem-vindo à API."}

# Rota para realizar uma operação matemática simples
@app.get("/calcular/{operacao}")
def calcular(operacao: str, num1: int, num2: int):
    resultado = 0
    if operacao == "soma":
        resultado = num1 + num2
    elif operacao == "subtracao":
        resultado = num1 - num2
    elif operacao == "multiplicacao":
        resultado = num1 * num2
    elif operacao == "divisao":
        resultado = num1 / num2
    else:
        return {"erro": "Operação não suportada"}
    
    return {"resultado": resultado}

# Rota padrão para verificar se o servidor está em execução
@app.get("/")
def verificar_status():
    return {"status": "Servidor em execução"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
