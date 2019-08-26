from selenium import webdriver
from selenium.webdriver.common.keys import Keys

pesquisa = input('O que deseja procurar?')

browser = webdriver.Chrome('C:\\Chromedriver\\Chromedriver')

browser.maximize_window()

browser.get('https://www.google.com/')

search = browser.find_element_by_name('q')
search.send_keys(pesquisa)
search.send_keys(Keys.ENTER)

imagem = browser.find_element_by_link_text('Imagens')
imagem.click()
