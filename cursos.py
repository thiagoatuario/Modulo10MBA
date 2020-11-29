import requests
from bs4 import BeautifulSoup

url = 'https://www.unipe.edu.br/graduacao/'

req = requests.get(url)
print(req.content)

soup = BeautifulSoup(req.content, 'html.parser')

lista_cursos = soup.find_all('div',class_="curso")

#print(lista_cursos)

for lista_nomes in lista_cursos:
    lista = lista_nomes.find_all('h3')#,class="imagem-cursos-vitrine ls-is-cached lazyloaded")
    #print(lista)
    for lista_dados in lista:
        print(lista_dados.next_element)



