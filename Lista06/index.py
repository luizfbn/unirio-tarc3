import requests
from bs4 import BeautifulSoup

url = 'https://www.goal.com/br/mineiro-i/tabela-de-classifica%C3%A7%C3%A3o/craznzmzk01hn9gjbj3g3mjah'

request = requests.get(url)
page = BeautifulSoup(request.content, 'html.parser')

# Coleta todas as linhas da tabela do campeonato mineiro
mineiroTable = page.find_all('tr', 'p0c-competition-tables__row')

print("{:<20} {:<8} {:<8} {:<8}".format('Time', 'Pontos', 'Jogos', 'Saldo de gols'))

# Em cada linha contém as informações de determinado time em que o nome das colunas são separadas por classes
for time in range(len(mineiroTable)):
    print("{:<20} {:<8} {:<8} {:<8}".format(
        mineiroTable[time].select('.p0c-competition-tables__team')[0].text.strip(),
        mineiroTable[time].select('.p0c-competition-tables__pts')[0].text.strip(),
        mineiroTable[time].select('.p0c-competition-tables__matches-played')[0].text.strip(),
        mineiroTable[time].select('.p0c-competition-tables__goals-diff')[0].text.strip()))
