import requests
from selenium import webdriver
#from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from time import sleep
import json
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://esaj.tjsp.jus.br/cpopg/open.do'
options = Options()
#options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
driver.get(url)
sleep(2)

driver.find_element(By.NAME, 'cbPesquisa').click()
select_element = driver.find_element(By.NAME, 'cbPesquisa')
select = Select(select_element)
option_list = select.options
select.select_by_value('DOCPARTE')
sleep(2)

print(option_list)
#driver.find_element(By.ID, 'numeroDigitoAnoUnificado').send_keys("12345678910" + Keys.ENTER)

doc_input = input('Qual é seu documento? ')
driver.find_element(By.ID, 'campo_DOCPARTE').send_keys(doc_input + Keys.ENTER)
#input_doc.send_keys("bitcoin dolar" + Keys.ENTER)

sleep(2)


site = BeautifulSoup(driver.page_source, "html.parser")
print(site.prettify())

numero_processo = site.find('span', attrs = {'id':'numeroProcesso'})
classe = site.find('span', attrs={'id':'classeProcesso'})
assunto = site.find('span', attrs={'id':'assuntoProcesso'})
foro = site.find('span', attrs={'id':'foroProcesso'})
vara = site.find('span', attrs={'id':'varaProcesso'})
juiz = site.find('span', attrs={'id':'juizProcesso'})
requerente = site.find('td', attrs={'class':'nomeParteEAdvogado'})
requerido = site.find('td', attrs={'class':'nomeParteEAdvogado'})

lista_processo = []
lista_processo.append([numero_processo.text,classe.text,assunto.text,foro.text,vara.text,juiz.text,requerente.text,requerido.text ])
print(lista_processo)

arquivo = pd.DataFrame(lista_processo, columns= ['Numero Processo', 'Classe', 'Assunto', 'Foro', 'Vara', 'Juiz', 'Requerente', 'Requerido'])
#arquivo.to_excel(doc_input+'-TJ-SP.xlsx', index=False)

