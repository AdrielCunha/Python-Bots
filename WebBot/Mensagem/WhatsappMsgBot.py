from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

name = input('Digite o nome do contato: ')
msg = input('Digite a mensagem que deseja enviar: ')
msg = ' '*10 + msg
q = int(input('Quantas vezes deseja enviar: '))

browser = webdriver.Chrome('C:\\ChromeDriver\\ChromeDriver')

browser.maximize_window()

browser.get('https://web.whatsapp.com/')

sleep(15)

browser.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/input').send_keys(name, Keys.ENTER)

sleep(2)

for i in range(0, q):
    browser.find_element_by_css_selector("[dir^='ltr']").send_keys("{}".format(msg), Keys.ENTER)
