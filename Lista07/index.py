import re
import requests

url = input('Informe a URL:')
#http://www.unirio.br/

print('Aguarde um momento...')

request = requests.get(url)
page = request.text

pattern = '<img.*width={1}.*height={1}.*>|<img.*height={1}.*width={1}.*>'

findImg = re.findall(pattern, page)

print('Imagens com altura e largura especificadas:')
print(findImg)
