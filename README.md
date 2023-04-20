<h1>Exemplo de FastAPI com Git</h1>

<p>Este é um exemplo simples de um aplicativo FastAPI que serve um arquivo HTML no endpoint raiz ("/"). O aplicativo utiliza o FastAPI, um framework moderno e rápido para construir APIs com Python.</p>

<h2>Dependências</h2>

<p>Este projeto requer as seguintes dependências:</p>

<ul>
  <li>FastAPI</li>
  <li>Jinja2</li>
  <li>uvicorn</li>
</ul>

<h2>Instalação</h2>

<p>Para configurar e executar o aplicativo localmente, siga os passos abaixo:</p>

<ol>
  <li>Clone o repositório para sua máquina local.</li>
  <li>Instale as dependências usando <code>pip</code> ou <code>conda</code>:</li>
</ol>

<pre>
<code>pip install fastapi jinja2 uvicorn</code>
</pre>

<ol start="3">
  <li>Execute o aplicativo usando <code>uvicorn</code>:</li>
</ol>

<pre>
<code>uvicorn main:app --reload</code>
</pre>

<p>Isso iniciará um servidor de desenvolvimento que recarrega automaticamente o aplicativo quando houver alterações.</p>

<h2>Estrutura de Arquivos</h2>

<ul>
  <li><code>app/static</code>: Diretório contendo arquivos estáticos, como CSS e imagens.</li>
  <li><code>app/templates/item.html</code>: Arquivo HTML que é servido no endpoint raiz ("/").</li>
  <li><code>main.py</code>: Script Python que define o aplicativo FastAPI e suas rotas.</li>
</ul>

<h2>Uso</h2>

<p>Depois que o aplicativo estiver em execução, você pode acessá-lo em seu navegador em <code>http://localhost:8000</code> (ou em uma porta diferente, se especificado). O aplicativo responderá com o conteúdo HTML do arquivo <code>item.html</code>, que é servido como resposta com um código de status 200 (OK).</p>

<h2>Contribuições</h2>

<p>Sinta-se à vontade para contribuir para este projeto enviando pull requests ou relatando problemas. Suas contribuições são muito apreciadas!</p>

<h2>Licença</h2>

<p>Este projeto está licenciado sob a Licença MIT. Consulte o arquivo <code>LICENSE</code> para obter mais informações.</p>
