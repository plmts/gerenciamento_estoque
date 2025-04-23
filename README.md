<h1>Sistema de Gerenciamento de Produtos</h1>
<p>O código demonstra um sistema de gerenciamento de produtos, ideal para uso em lojas, mercados ou qualquer outro estabelecimento que possua um estoque e deseja uma plataforma para gerenciar os produtos que entram e saem.</p>

<h2>🚀 Começando</h2>
<p>Essas instruções permitirão que você obtenha uma cópia do projeto em operação na sua máquina local para fins de desenvolvimento e teste. A clonagem de um repositório baixa uma cópia completa de todos os dados dele que o GitHub.com tem no momento, incluindo todas as versões de cada arquivo e pasta do projeto.</p>

<h3>Clonar um respositório</h3>

<lu>
<li> Em GitHub, acesse a página principal do repositório.</li>
<li> Acima da lista de arquivos, clique em  Código.</li>
<li> Copie a URL do repositório (Você pode realizar a clonagem tanto copiando o HTTPS, a chave SSH ou o GitHub CLI).</li>
<li> Abra Git Bash.</li>
<li> Altere o diretório de trabalho atual para o local em que deseja ter o diretório clonado.</li>
<li> Digite git clone e cole a URL já copiada.</li>
<li> Pressione ENTER para criar seu clone local.</li>
</lu>

<h2>📋 Pré-requisitos</h2>
<p>Para poder utilizar o código, se faz necessário ter instalado em sua máquina:</p>
<lu>
<li> Python V3.13.0</li>
<li> Visual Studio Code (ou qualquer outro editor de textos de sua preferência com suporte à linguagem Python)</li>
<li> Flask</li>
<li> SQLAlchemy</li>
<li> Postman (ou qualquer outra plataforma de gerenciamento de APIs de sua preferencia)</li>
</lu>

<h2>🔧 Instalação</h2>
<p>Após instalados todos os itens necessários, abra o editor de texto de no terminal e digite <b>pip install -r requirements.txt</b>. Isso fará com que todas as bibliotecas das quais a aplicação depende sejam instaladas em sua máquina. </p>

<h2>⚙️ Executando os testes</h2>
<p>Depois de feitas as intalações, basta executar o código dentro do arquivo <u>main.py</u>. Estando tudo de acordo, basta prosseguir para o Postman - ou sua plataforma escolhida - e iniciar os testes.

Por exemplo, vamos adicionar um produto. No caso do Postman, após criado o workspace, vá até a seção denominada <b>POST</b> e digite a seguinte url no campo em destaque: <b>http://127.0.0.1:5000/produtos/</b>.
Logo após vá para a seção <b>body</b> e no campo em destaque, digite o seguinte dicionário: 

{
	"nome": "Caneca I Love You",
    "valor": 10.50,
    "marca": "Wolff",
    "descricao": "Caneca Preta com detalhes em formato de coração com frase 'I Love You' escrita.",
    "quantidade": 5
}

Depois disso, basta apenas clicar em <b>SEND</b> que as informações contidas nesse dicionário serão salvas no banco de dados.
Fique à vontade para realizar mais testes, explorando todas as formas de requisição.
</p>

<h1>🛠️ Construído com</h1>
<lu>
  <li>Python - Lingaguem de programação utilizada</li>
  <li>Flask - Framework utilizada para criação da API</li>
  <li>SQLAlchemy - Framework utilizado para criação e gerenciamento do banco de dados</li>
</lu>

<h1>🖇️ Colaborando</h1>
<p>Não está aceitando colaborações</p>



<h1>✒️ Autores</h1>
Mencione todos aqueles que ajudaram a levantar o projeto desde o seu início

Paulo Matos - @plmts
