# Passo 1: Acessar o site da empresa
#    Link: https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Passo 2: Fazer Login
# Passo 3: Pegar/importar a base de dados
# Passo 4: Cadastrar o primeiro produto
# Passo 5: Repetir o passo 4 até cadastrar todos os produtos

import pyautogui # pip install pyautogui (automatiza mouse/teclado/tela)
import pandas # pip install pandas (importar o BD)
import time
import os

pyautogui.PAUSE = 0.5 # a cada comando do pyautogui faz uma pausa de meio segundo

pyautogui.press("win")
pyautogui.write("Crome")
pyautogui.press("enter")

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(1.5)

pyautogui.click(x=-720, y=369) # Click no input do email (deve ser alterado a posicao conforme a tela)
pyautogui.hotkey("ctrl", "a")
pyautogui.write("pythonimpressionador@gmail.com")

pyautogui.hotkey("tab")
pyautogui.write("minha senha")

pyautogui.click(x=-698, y=536) # click no botao de login

produtos = os.path.join(os.path.dirname(__file__),"produtos.csv") # encontra o arquivo
dados_produto = pandas.read_csv(produtos)

for linha in dados_produto.index:
    pyautogui.click(x=-966, y=265) # click no input do codigo 

    codigo = str(dados_produto.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.hotkey("tab")

    marca = str(dados_produto.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.hotkey("tab")

    tipo = str(dados_produto.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.hotkey("tab")

    categoria = str(dados_produto.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.hotkey("tab")

    preco_unitario = str(dados_produto.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.hotkey("tab")

    custo = str(dados_produto.loc[linha, "custo"])
    pyautogui.write(custo)

    pyautogui.hotkey("tab")

    obs = str(dados_produto.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)

    pyautogui.hotkey("tab") # botao de enviar

    pyautogui.hotkey("enter")
    pyautogui.scroll(1000) # voltar ao inicio da tela