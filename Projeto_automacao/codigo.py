""" 
Passo 1: Entrar no sistema da empresa
    Link: https://dlp.hashtagtreinamentos.com/python/intensivao/login
Passo 2: Fazer o login
Passo 3: Pegar/Importar dados
Passo 4: Cadastrar produto
Passo 5: Repetir processo
"""

# pip install pyautogui (no prompt de comando para instalar pela primeira vez o pacote)
import pyautogui # utilizar este pacote de código (para automação de atividades do mouse, teclado e monitor)
import time # tempo de espera
# https://pyautogui.readthedocs.io/en/latest/ (documentação)

""" 
pyautogui.click #clicar
pyautogui.write #escrever
pyautogui.press #apertar uma tecla 
pyautogui.hotkey #combinação de teclas (ex: ctrl + c)
pyautogui.scroll #rolar a tela
"""

# Passo 1: Entrar no sistema da empresa
# abrir navegador -> entrar no link 

# Passo 1: Entrar no sistema da empresa

pyautogui.PAUSE = 1.0 #configurando tempo de intervalo no código para cada comando

pyautogui.press("win") #apertar uma tecla 
pyautogui.write("chrome") #escrever
pyautogui.press("enter") #apertar uma tecla 
time.sleep(5) # vai esperar um pouco nesse trecho
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login") #escrever
pyautogui.press("enter") #apertar uma tecla 

time.sleep(3) # vai esperar um pouco nesse trecho

# Passo 2: Fazer o login

pyautogui.click(x=652, y=377) #clicar
pyautogui.hotkey("ctrl", "a") #combinação de teclas
pyautogui.write("julia@gmail.com") #escrever
pyautogui.click(x=650, y=477) #clicar
pyautogui.hotkey("ctrl", "a") #combinação de teclas
pyautogui.write("123") #escrever
pyautogui.press("enter") #apertar uma tecla



