<!DOCTYPE html>
<html>

<head>
    <title>Exemplo de Servidor de Arquivos Estáticos com FastAPI</title>
</head>

<body>
    <h1>Exemplo de Servidor de Arquivos Estáticos com FastAPI</h1>
    <p>Este é um exemplo simples de como servir arquivos estáticos usando o FastAPI, um framework moderno e rápido para construir APIs com Python.</p>

    <h2>Dependências</h2>
    <p>Este projeto requer as seguintes dependências:</p>
    <ul>
        <li>FastAPI</li>
        <li>uvicorn</li>
    </ul>

    <h2>Instalação</h2>
    <p>Para configurar e executar o servidor de arquivos estáticos localmente, siga os passos abaixo:</p>
    <ol>
        <li>Clone o repositório para sua máquina local.</li>
        <li>Instale as dependências usando <code>pip</code> ou <code>conda</code>:</li>
    </ol>
    <pre><code>pip install fastapi uvicorn</code></pre>
    <ol start="3">
        <li>Coloque seus arquivos estáticos no diretório <code>/static</code> na raiz do projeto.</li>
        <li>Execute o aplicativo usando <code>uvicorn</code>:</li>
    </ol>
    <pre><code>uvicorn main:app --reload</code></pre>
    <p>Isso iniciará o servidor de desenvolvimento do FastAPI, que servirá os arquivos estáticos localmente e recarregará automaticamente o aplicativo quando houver alterações.</p>

    <h2>Estrutura de Arquivos</h2>
    <ul>
        <li><code>/static</code>: Diretório que contém os arquivos estáticos, como CSS, imagens, JavaScript, etc.</li>
        <li><code>main.py</code>: Script Python que define o aplicativo FastAPI e configura a rota para servir os arquivos estáticos.</li>
    </ul>

    <h2>Uso</h2>
    <p>Depois de iniciar o servidor, você pode acessar os arquivos estáticos em seu navegador, usando o seguinte padrão de URL:</p>
    <pre><code>http://localhost:8000/static/&lt;nome_do_arquivo&gt;</code></pre>
    <p>Substitua &lt;nome_do_arquivo&gt; pelo nome real do arquivo estático que você deseja acessar.</p>

    <h2>Contribuições</h2>
    <p>Sinta-se à vontade para contribuir para este projeto enviando pull requests ou relatando problemas. Suas contribuições são muito apreciadas!</p>

    <h2>Licença</h2>
    <p>Este projeto está licenciado sob a Licença MIT. Consulte o arquivo <code>LICENSE</code> para obter mais informações.</p>
</body>

</html>
