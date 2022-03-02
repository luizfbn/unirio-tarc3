import requests
from bs4 import BeautifulSoup

url = 'https://valor.globo.com/'

request = requests.get(url)
page = BeautifulSoup(request.text, 'html.parser')

# a) O número de parágrafos, o menor e o maior parágrafo;
paragraph = page.select('p')
print('Número de parágrafos:', str(len(paragraph)))

largestParagraph = smallestParagraph = paragraph[0]

for p in paragraph:
    if len(str(p)) > len(str(largestParagraph)):
        largestParagraph = p
    elif len(str(p)) < len(str(smallestParagraph)):
        smallestParagraph = p

print('O menor parágrafo é:', smallestParagraph.getText())
print('O maior parágrafo é:', largestParagraph.getText())

# b) O número de imagens;
image = page.select('img')
print('Número de imagens:', str(len(image)))

# c) O número de links;
link = page.find_all('a', href=True)
print('Número de links:', str(len(link)))

# d) O número de vezes que a palavra “saúde” e a palavra “esporte” aparecem.
saude = page.find_all(text='saúde')
esporte = page.find_all(text='esporte')
print('Quantidade de vezes que a palavra "saúde" aparece:', str(len(saude)))
print('Quantidade de vezes que a palavra "esporte" aparece:', str(len(esporte)))

