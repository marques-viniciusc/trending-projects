📊 GitHub Trending Scraper
Este projeto realiza web scraping do site GitHub Trending, extrai informações sobre os projetos mais populares e cria uma visualização gráfica em formato de gráfico de pizza mostrando a distribuição das linguagens de programação dos projetos extraídos.

🚀 Funcionalidades
Faz uma requisição à página de projetos populares no GitHub.
Usa a biblioteca BeautifulSoup para extrair dados como nome do projeto, linguagem de programação, número de estrelas e número de forks.
Salva os dados extraídos em um arquivo CSV.
Exibe um gráfico de pizza representando a distribuição das linguagens dos 10 primeiros projetos.

📂 Estrutura do Projeto
github.csv: Arquivo CSV gerado com as informações dos projetos extraídos.
trending_scraper.py: Script Python responsável pelo web scraping e geração do gráfico.

🛠️ Tecnologias Utilizadas
Python: Linguagem de programação usada no projeto.
Bibliotecas:
requests: Para fazer requisições HTTP.
BeautifulSoup (da biblioteca bs4): Para realizar o parsing do HTML e extrair informações.
csv: Para salvar os dados extraídos em formato CSV.
pandas: Para manipulação dos dados.
matplotlib: Para criação do gráfico de pizza.

📊 Como o Projeto Funciona
Faz uma requisição à página do GitHub Trending e obtém o conteúdo HTML.
Utiliza o BeautifulSoup para extrair o nome dos projetos, linguagem de programação, número de estrelas e forks.
Os dados são armazenados em um arquivo CSV com as colunas: ranking, project, language, stars_today, stars, forks.
Cria um gráfico de pizza com a distribuição das linguagens dos projetos extraídos.

🔧 Como Rodar o Projeto
Clone o repositório:

```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
```
Instale as dependências necessárias:
```bash
pip install requests beautifulsoup4 pandas matplotlib
```
Execute o script Python:
```bash
python trending_scraper.py
```
O gráfico de pizza com a distribuição de linguagens será exibido e o arquivo github.csv será gerado no diretório.

🎯 Resultado
Após a execução do script, o gráfico de pizza será gerado com a porcentagem de cada linguagem de programação nos 10 projetos mais populares.
Exemplo de visualização:

⚠️ Considerações
O arquivo robots.txt do GitHub permite que a página /trending seja acessada e indexada por web crawlers, portanto, este projeto está em conformidade com as políticas do site.

📄 Licença
Este projeto é de uso livre para fins educativos e de estudo. Sinta-se à vontade para usar e modificar conforme necessário.