"""
DOCUMENTAÇÃO DOS IMPORTS E SEQUÊNCIAS DOS MESMOS:
https://selenium-python.readthedocs.io/getting-started.html

#Configurações padrões para rodar a automação Selenium

#Com busca e implementação de atualizações da versão do chrome automáticas para que, na hora do funcionamento da automação não haja erros de versão.
"""

import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico, options=chrome_options)
import pyautogui


#DECLARAÇÃO DE LIST PARA USO POSTERIOR

trechos_e_frases = []


#PASSO 1 -- ENTRANDO NO NAVEGADOR > PÁGINA INICIAL.
url = 'https://www.mairovergara.com/category/phrasal-verbs/page/1/'
navegador.get(url)

#PASSO 2 -- SELECIONAR UM QUADRADO ONDE SERÁ COLETADO A FRASE.

navegador.find_element('xpath','//*[@id="td-outer-wrap"]/div/div[3]/div/div[2]/div[1]/div/div[3]/div[1]').click()
time.sleep(5)

#LOCALIZANDO XPATH DO TEXTO A SER COPIADO...

texto = navegador.find_element('xpath','//*[@id="post-76183"]/div[3]/p[7]')
time.sleep(5)

#COPIANDO
texto_copiado = texto.text
time.sleep(3)
print(texto_copiado)

""""
#PROXIMO TEXTO

#texto2 = navegador.find_element('xpath','//*[@id="post-76183"]/div[3]/p[8]')

clipboard.set_text(texto)
frases_palavras.append(texto)

navegador.find_element('//*[@id="post-73629"]/div[3]/p[5]')

texto2 = navegador.text

frases_palavras.append(texto2)
clipboard.set_text(texto2)
"""

#IMPORTAÇÃO E INICIO DE AUTOMAÇÃO PARA PROCESSOS NO WINDOWS COM WINOUT
""""
from pywinauto import clipboard
from pywinauto import mouse
from pywinauto.application import Application
from pywinauto import keyboard

pagina_inicial = r'C:\Program Files\Anki\anki.exe'
app = Application(backend='uia').start(pagina_inicial)

"""

# Pressione a combinação de teclas para abrir o aplicativo (por exemplo, no Windows, pode ser Win + R para executar e digitar o caminho do aplicativo)
pyautogui.hotkey('ctrl','alt','k')
time.sleep(10)
pyautogui.press('a')