import requests
import urllib3
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import time


def search_new_links(current_page):
    try:
        response = requests.get(current_page, verify=False, timeout=1)  # Faz a requisição da página
        if not response.ok:  # Verifica o status da requisição. Caso não seja 200 é considerado um link problemático
            brokenLinks.append({"url": current_page, "status": response.status_code})
    except:
        return

    content_type = response.headers.get('content-type')

    if 'text/html' in content_type:  # Verifica se é uma página html
        page = BeautifulSoup(response.text, "html.parser")
        links_from_page = page.find_all("a", href=True)  # Coleta da página todas as tags "a" com href

        for link in range(len(links_from_page)):
            href = links_from_page[link].get("href")
            valid_link = urlparse(href)
            if all([valid_link.scheme, valid_link.netloc]):  # Verifica se é um link válido
                link_hostname = urlparse(href).hostname
                if link_hostname == hostname:  # Verifica se é o hostname da unirio
                    link_path = urlparse(href).path
                    if link_path.count("/") < 2:  # Limita a profundidade do diretório
                        if link_path != "/":  # Evita links com variações da página inicial
                            if href not in siteMap:
                                siteMap.append(href)
                else:
                    if href not in otherLinks:
                        otherLinks.append(href)
    return


def check_other_links():
    for j in range(len(otherLinks)):
        link = otherLinks[j]
        print("Processando link", j, ":", link)
        try:
            response = requests.get(link, verify=False, timeout=5)
            if not response.ok:
                brokenLinks.append({"url": link, "status": response.status_code})
        except:
            pass
    return


start_time = time.time()
urllib3.disable_warnings()  # Desativa aviso de links com https sem certificado

mainURL = "http://www.unirio.br"
siteMap = [mainURL]
otherLinks = []
brokenLinks = []

hostname = urlparse(mainURL).hostname
i = 0

print("Procurando links...")
while i < len(siteMap):
    search_new_links(siteMap[i])  # Procura novos links do domínio na página corrente
    print("Processando link", i, ":", siteMap[i])
    # Limitar a busca
    #if i == 25:
    #    break
    i += 1

print("Avaliando outros links...")
check_other_links()  # Verifica se os demais links coletados(que não são do domínio) tem algum problema

print("Links unirio:", len(siteMap))
print(siteMap)
print("Outros links:", len(otherLinks))
print(otherLinks)
print("Links problemáticos:", len(brokenLinks))
print(brokenLinks)

print("Tempo de execução:", (time.time() - start_time), "segundos")
