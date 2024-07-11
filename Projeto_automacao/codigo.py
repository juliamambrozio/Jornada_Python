""" 
Passo 1: Entrar no sistema da empresa
    Link: https://dlp.hashtagtreinamentos.com/python/intensivao/login
Passo 2: Fazer o login
Passo 3: Pegar/Importar dados
Passo 4: Cadastrar produto
Passo 5: Repetir processo
"""

# pip install pyautogui (no prompt de comando para instalar pela primeira vez o pacote)
# pip install pandas openpyxl numpy (no prompt de comando para instalar pela primeira vez o pacote)

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

time.sleep(5) # vai esperar um pouco nesse trecho

# Passo 2: Fazer o login

pyautogui.click(x=652, y=377) #clicar
pyautogui.hotkey("ctrl", "a") #combinação de teclas
pyautogui.write("julia@gmail.com") #escrever
pyautogui.click(x=650, y=477) #clicar
pyautogui.hotkey("ctrl", "a") #combinação de teclas
pyautogui.write("123") #escrever
pyautogui.press("enter") #apertar uma tecla

time.sleep(3) # vai esperar um pouco nesse trecho

# Passo 3: Pegar/Importar dados

import pandas # trabalhar com vários tipos de dados

tabela = pandas.read_csv("produtos.csv") # armazenando dados na var

print(tabela)

# Passo 4: Cadastrar produto

# Looping

for linha in tabela.index: # phyton chama cada linha de index
    # para cada linha em tabela.index
    pyautogui.click(x=554, y=256) # clicar
    codigo = str(tabela.loc[linha, "codigo"]) # localizar ítem e passar para string
    #localizando a linha de qual coluna
    pyautogui.write(codigo) # escrever
    
    
    pyautogui.press("tab") #clicar
    marca = str(taCAHA000   bela.loc[linha, "marca"]) # localizar ítem e passar para string
    pyautogui.write(marca) # escrever

    
    pyautogui.press("tab")
    tipo = str(tabela.loc[linha, "tipo"]) # localizar ítem e passar para string
    pyautogui.write(tipo) # escrever

    
    pyautogui.press("tab")
    categoria = str(tabela.loc[linha, "categoria"]) # localizar ítem e passar para string
    pyautogui.write(categoria) # escrever

    
    pyautogui.press("tab")
    preco_unitario = str(tabela.loc[linha, "preco_unitario"]) # localizar ítem e passar para string
    pyautogui.write(preco_unitario) # escrever

    
    pyautogui.press("tab")
    custo = str(tabela.loc[linha, "custo"]) # localizar ítem e passar para string
    pyautogui.write(custo) # escrever

    
    pyautogui.press("tab")
    obs = str(tabela.loc[linha, "obs"]) # localizar ítem e passar para string
    if obs != "nan": # se for diferente de nan ele cadastra, se não ele não cadastra
        pyautogui.write(obs) # escrever

    pyautogui.press("tab") # apertar uma tecla
    pyautogui.press("enter") # apertar uma tecla
    pyautogui.scroll(1000) # rolar a tela





