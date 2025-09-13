from openpyxl import load_workbook
from selenium import webdriver as opcoes
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

caminho_arquivo = 'DadosFormulario.xlsx'

planilha_aberta = load_workbook(filename=caminho_arquivo)

sheet_selecionada = planilha_aberta['Dados']

for linha in range(2, len(sheet_selecionada['A']) + 1):

    nome = sheet_selecionada[f'A{linha}'].value
    email = sheet_selecionada[f'B{linha}'].value
    telefone = sheet_selecionada[f'C{linha}'].value
    sexo = sheet_selecionada[f'D{linha}'].value
    sobre = sheet_selecionada[f'E{linha}'].value

    driver = opcoes.Chrome()
    driver.get('https://pt.surveymonkey.com/r/TVDJSL9')

    espera = WebDriverWait(driver, 10)

    campo_nome = espera.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/div[2]/div[2]/main/form/div[1]/div/div/div/div/div/fieldset/input')))
    campo_nome.send_keys(nome)
   
    #-----------------------------------

    campo_email = espera.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/div[2]/div[2]/main/form/div[2]/div/div/div/div/div/fieldset/input')))
    campo_email.send_keys(email)

    #---------------------------------------------

    campo_telefone = espera.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/div[2]/div[2]/main/form/div[3]/div/div/div/div/div/fieldset/input')))
    campo_telefone.send_keys(telefone)

    #--------------------------------------------

    if sexo == 'Masculino':
        botao_masculino = espera.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[2]/div[2]/div[2]/main/form/div[4]/div/div/div/div/fieldset/div/div/div/div[2]/label')))
        botao_masculino.click()
    else:
        botao_feminino = espera.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[2]/div[2]/div[2]/main/form/div[4]/div/div/div/div/fieldset/div/div/div/div[1]/label')))
        botao_feminino.click()

    #-----------------------------------------------

    campo_sobre = espera.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/div[2]/div[2]/main/form/div[5]/div/div/div/div/div/fieldset/input')))
    campo_sobre.send_keys(sobre)

    #-----------------------------------------------------------
    botao_enviar = espera.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[2]/div[2]/div[2]/main/footer/div/div/button')))
    botao_enviar.click() 
