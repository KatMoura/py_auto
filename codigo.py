import pyautogui
import time

#Pausa de 0.5 segundos entre cada comando
pyautogui.PAUSE = 0.5

#Abrir o navegador
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

#Tempo de descanso para abrir o Chrome
time.sleep(3)

#Digitar o link
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

time.sleep(3)

#Clicar no espaço de email e fazer login
pyautogui.click(x=913, y=465)
pyautogui.write('onedirection@gmail.com')
pyautogui.press('tab')
pyautogui.write('123654789')
pyautogui.press('enter')

time.sleep(3)

#Importar base de produtos para cadastrar
import pandas as pd

tabela = pd.read_csv('../Power Up/produtos.csv')

print(tabela)

#Cadastrar um produto
for linha in tabela.index:
    pyautogui.click(x=656, y=320)
    #Pegar o valor para preencher da tabela
    codigo = str(tabela.loc[linha, "codigo"])
    #Preencher o campo
    pyautogui.write(str(codigo))
    #Ir para o próximo campo
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press('tab')
    
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press('tab')

    #Se a coluna de OBS estiver com valor NaN, ignorar
    obs = tabela.loc[linha, 'obs']
    if not pd.isna(obs): #Detecta se a coluna possui valores nulos
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press('tab')
    pyautogui.press('enter')

    #Voltar para o topo da página
    pyautogui.scroll(5000)
    