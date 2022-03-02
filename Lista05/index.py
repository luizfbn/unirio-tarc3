from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

# Pesquisa de algum assunto #

url ='https://odia.ig.com.br/'
search = 'Flamengo'

firefoxDriver = webdriver.Firefox()
firefoxDriver.get(url)
print('URL antes da busca:', firefoxDriver.current_url)

searchBox = firefoxDriver.find_element(By.NAME, 'q').send_keys(search + Keys.ENTER)

# O driver espera até a url mudar
WebDriverWait(firefoxDriver, timeout=3).until(expected_conditions.url_changes(url))

print('URL depois da busca:', firefoxDriver.current_url)
