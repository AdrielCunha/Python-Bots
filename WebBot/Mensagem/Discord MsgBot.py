from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

name = input('Para quem deseja enviar: ')
text = input('O que deseja enviar: ')
q = int(input('Quantas vezes deseja enviar: '))
print('='*80)
email = input('Digite seu email: ')
password = input('Digite sua senha: ')

browser = webdriver.Chrome('C:\\ChromeDriver\\ChromeDriver')

browser.maximize_window()

browser.get('https://discordapp.com/channels/@me')

emailW = browser.find_element_by_xpath('//*[@id="app-mount"]/div[1]/div/div[2]/div/form/div/div[3]/div[1]/div/input')
emailW.send_keys(email)
emailW.send_keys(Keys.TAB)

passwordW = browser.find_element_by_xpath('//*[@id="app-mount"]/div[1]/div/div[2]/div/form/div/div[3]/div[2]/div/input')
passwordW.send_keys(password)
passwordW.send_keys(Keys.ENTER)

sleep(20)

contact = browser.find_element_by_link_text(name)
contact.click()

for i in range(0, q):
    browser.find_element_by_xpath('//*[@id="app-mount"]/div[1]/div/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/div/form/div/div/div/textarea').send_keys(text, Keys.ENTER)
    sleep(1)





