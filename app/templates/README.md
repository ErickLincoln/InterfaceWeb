<!DOCTYPE html>
<html>

<head>
    <title>Exemplo de Uso de Templates com FastAPI</title>
</head>

<body>
    <h1>Exemplo de Uso de Templates com FastAPI</h1>
    <p>Este é um exemplo simples de como usar templates em conjunto com o FastAPI, um framework moderno e rápido para construir APIs com Python.</p>

    <h2>Dependências</h2>
    <p>Este projeto requer as seguintes dependências:</p>
    <ul>
        <li>FastAPI</li>
        <li>uvicorn</li>
        <li>Jinja2</li>
    </ul>

    <h2>Instalação</h2>
    <p>Para configurar e executar o projeto com templates localmente, siga os passos abaixo:</p>
    <ol>
        <li>Clone o repositório para sua máquina local.</li>
        <li>Instale as dependências usando <code>pip</code> ou <code>conda</code>:</li>
    </ol>
    <pre><code>pip install fastapi uvicorn jinja2</code></pre>
    <ol start="3">
        <li>Crie um diretório chamado <code>/templates</code> na raiz do projeto e coloque seus arquivos de template dentro dele.</li>
        <li>Execute o aplicativo usando <code>uvicorn</code>:</li>
    </ol>
    <pre><code>uvicorn main:app --reload</code></pre>
    <p>Isso iniciará o servidor de desenvolvimento do FastAPI, que usará os templates para renderizar páginas HTML dinamicamente.</p>

    <h2>Estrutura de Arquivos</h2>
    <ul>
        <li><code>/templates</code>: Diretório que contém os arquivos de template, geralmente em formato HTML, que serão renderizados dinamicamente pelo FastAPI.</li>
        <li><code>main.py</code>: Script Python que define o aplicativo FastAPI e configura a integração com os templates.</li>
    </ul>

    <h2>Uso</h2>
    <p>Depois de iniciar o servidor, você pode acessar as páginas HTML renderizadas pelos templates em seu navegador, usando as rotas definidas no aplicativo FastAPI.</p>

    <h2>Contribuições</h2>
    <p>Sinta-se à vontade para contribuir para este projeto enviando pull requests ou relatando problemas. Suas contribuições são muito apreciadas!</p>

    <h2>Licença</h2>
    <p>Este projeto está licenciado sob a Licença MIT. Consulte o arquivo <code>LICENSE</code> para obter mais informações.</p>
</body>

</html>
