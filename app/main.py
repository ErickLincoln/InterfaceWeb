from fastapi import FastAPI, Request               # Importa o módulo FastAPI e a classe Request
from fastapi.responses import HTMLResponse         # Importa a classe HTMLResponse do módulo fastapi.responses
from fastapi.staticfiles import StaticFiles        # Importa a classe StaticFiles do módulo fastapi.staticfiles
from fastapi.templating import Jinja2Templates     # Importa a classe Jinja2Templates do módulo fastapi.templating
import os                                       # Importa o módulo os para manipulação de caminhos de arquivo

app = FastAPI()                                  # Cria uma instância da classe FastAPI chamada "app"

# Monta o diretório de arquivos estáticos
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Define uma rota para a raiz ("/") que responde com um objeto HTMLResponse
# e recebe um objeto Request como parâmetro
@app.get("/", response_class=HTMLResponse)
async def get_index(request: Request):
    file_path = os.path.join("app", "templates", "item.html")   # Monta o caminho completo para o arquivo HTML
    with open(file_path, "r") as file:                         # Abre o arquivo em modo de leitura
        html_content = file.read()                             # Lê o conteúdo do arquivo

    return HTMLResponse(content=html_content, status_code=200)  # Retorna o conteúdo HTML como uma resposta HTTP com status 200 (OK)

# Comentário para executar o servidor de desenvolvimento com o comando uvicorn
# uvicorn main:app --reload
