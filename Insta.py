!pip install selenium
from selenium import webdriver
import time
navegador = webdriver.Chrome("chromedriver.exe")

#Entrar no instagram
navegador.get('https://www.instagram.com/')
time.sleep(5)

#Fazer Login
navegador.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys("SEU USUARIO")
time.sleep(5)
#Preencher senha
navegador.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys("SUA SENHA")

time.sleep(5)
#Clicar em entrar
navegador.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]').click()
time.sleep(10)
#Clicar em agora não "info"
navegador.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()

time.sleep(10)
#Clicar em agora não "Notificação"
navegador.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]').click()

time.sleep(10)
#Clicar em explorar

navegador.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[4]/a').click()

time.sleep(10)
#Clicar em algum perfil

navegador.find_element_by_class_name('eLAPa').click()

for i in range(3):
    # Seguir perfil
    navegador.find_element_by_xpath(
        '/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[2]/button/div').click()
    time.sleep(10)

    # curtir a foto
    navegador.find_element_by_xpath(
        '/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button').click()

    # comentar  na foto
    navegador.find_element_by_xpath(
        '/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea').click()
    navegador.find_element_by_xpath(
        '/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea').send_keys(
        "COMENTARIO NA FOTO")
    navegador.find_element_by_xpath(
        '/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/button').click()
    time.sleep(15)

    # Passar para outro perfil
    navegador.find_element_by_xpath('/html/body/div[6]/div[2]/div/div[2]').click()
    time.sleep(10)

time.sleep(30)

for i in range(3):
    # Seguir perfil
    navegador.find_element_by_xpath(
        '/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[2]/button').click()
    time.sleep(2)

    # curtir a foto
    navegador.find_element_by_xpath(
        '/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button').click()

    # comentar  na foto
    navegador.find_element_by_xpath(
        '/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea').click()
    navegador.find_element_by_xpath(
        '/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea').send_keys(
        "COMENTARIO NA FOTO")
    navegador.find_element_by_xpath(
        '/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/button').click()
    time.sleep(3)

    # Passar para outro perfil
    navegador.find_element_by_class_name('QBdPU ').click()
    time.sleep(10)

for i in range(15):
    # curtir a foto
    navegador.find_element_by_xpath(
        '/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button').click()

    # Passar para outro perfil
    navegador.find_element_by_xpath('/html/body/div[6]/div[2]/div/div[2]').click()
    time.sleep(10)

    