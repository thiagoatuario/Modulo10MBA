from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
import json


def finds(browser, by, expression):
    try:
        return browser.find_elements(by, expression)
    except NoSuchElementException as nse:
        return None

def find(browser, by, expression):
    try:
        return browser.find_element(by, expression)
    except NoSuchElementException as nse:
        return None
a=input("Selecione o item\n")
output  = open('output.json', 'w', encoding='utf-8')
driver = webdriver.Firefox()
driver.get("https://lista.mercadolivre.com.br/" + a)
# elem = driver.find_element_by_tag_name("body")
# elem.send_keys(Keys.END)
# elem.send_keys(Keys.END)
# elem.send_keys(Keys.END)
items = finds(driver, By.CLASS_NAME, 'ui-search-result__content-wrapper')
while True:
    for item in items: 
        descricao = find(item, By.CLASS_NAME, 'ui-search-item__title').get_property("textContent")
        preco = find(item, By.CLASS_NAME, 'ui-search-price').get_property("textContent")
        #metadata_line = find(item, By.CLASS_NAME, 'metadata-line')
        #metadata = finds(metadata_line, By.XPATH , './/span')
        #if (len(metadata) > 0):
        #   preco = metadata[0].get_property("textContent")
            #tempo = metadata[1].get_property("textContent")
        print(descricao)
        # print(metadata_line)
        print(preco)
        #print(tempo)
        # print(spans[1].get_property("textContent"))
        # descricao = find(item, By.CLASS_NAME, 'txt-desc-product-item').get_property("innerHTML")
        # preco = find(item, By.CLASS_NAME, 'area-bloco-preco').get_property("textContent")
        # preco = preco.replace('R$', '')
        # preco = preco.replace('\,', '.')
        # preco = preco.strip()
        item = {'descricao': descricao, 'preco': preco}
        # print(descricao)
        # print(preco)
        output.write(json.dumps(item))
        output.write('\n')
        #try:
            #driver.execute_script("return arguments[0].scrollIntoView(true);", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//li[@class='arrow__right']/a"))))
    nextpage=find(driver,By.CLASS_NAME,"andes-pagination__link")
    if nextpage != None:
        nextpage.click()
        print("Navigating to Next Page")
    else:
        print("Last page reached")
        break
        #except (TimeoutException, WebDriverException) as e:
# driver.close()