# importação de pacotes utilizados no projeto

import requests
import csv
import pandas as pd
import matplotlib.pyplot as plt
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup

conteudo_git = None
URL2 = 'https://github.com/trending'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# Checagem de erros ao acessar o site

try:
    resposta = requests.get(URL2, headers=headers)
    resposta.raise_for_status()
    conteudo_git = resposta.text
except HTTPError as exc:
    print(exc)
except Exception as err:
    print(err)

# Uso do BeautifulSoup para extrair os dados de interesse

pagina_git = BeautifulSoup(conteudo_git, 'html.parser')

# Criação de uma lista organizada para gerar o csv

conteudo_extraido_git = []
ranking = 1

for linha in pagina_git.find_all('article'):
    if ranking > 10:
        break

    textos_coluna = list()

    for coluna in linha.find_all('a'):
        texto_coluna = coluna.get_text().strip().split('\n')
        if texto_coluna != ['Sponsor'] and texto_coluna != ['https://cloud.qdrant.io/']:
            textos_coluna += texto_coluna

    for coluna in linha.find_all('span'):
        texto_coluna = coluna.get_text().strip().split('\n')
        textos_coluna += texto_coluna

    linha = [str(ranking)]
    linha.append(textos_coluna[3].strip())

    for i in range(4, 6):
        linha.append(textos_coluna[i].replace(',', '.'))  # Substituindo vírgula por ponto nos números

    linha.insert(-2, (textos_coluna[-1].split(sep=' ')[0]))

    if textos_coluna[-3] == textos_coluna[1]:
        linha.insert(2, '')
    else:
        linha.insert(2, textos_coluna[-3])

    conteudo_extraido_git.append(linha)
    ranking += 1

cabecalho_git = ['ranking', 'project', 'language', 'stars_today', 'stars', 'forks']

with open(file='./github.csv', mode='w', encoding='utf8', newline='') as fp:
    escritor_csv = csv.writer(fp, delimiter=';')
    escritor_csv.writerow(cabecalho_git)
    escritor_csv.writerows(conteudo_extraido_git)

# Criação do dataframe e do gráfico em pizza

df = pd.read_csv('./github.csv', sep=';')
sizes = df['language'].value_counts()
grafico = plt.pie(sizes, labels=sizes.index, autopct='%1.1f%%')
plt.title('Porcentagem de repositórios por linguagem de programação')
plt.savefig('github.png')
df.head(10)