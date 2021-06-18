import requests
from bs4 import BeautifulSoup

print('*****************************************************','Bienvenido', '*****************************************************', sep='\n')

word = input('Ingrese palabra a buscar:\n')

# split('lenguaje php') split -> ['lenguaje', 'php']
# len(['lenguaje', 'php']) -> 2
# API -> Interfaz promgramacion de aplicaciones
# API REST -> HTTP VERBOS ['GET', 'POST', 'PUT/PATCH', 'DELETE'] get -> MISERVICIO/USUARIOS get ? rut -> rut
# flask - django -> sistemas web
# case 2
# split('php') split -> ['php']
# len(['php']) -> 1

if len(word.split()) == 1: # validamos que se ingrese solo una palabta
    q = 'que es ' + word # generamos parametro de busqueda -> php -> que es php
    response = requests.get('https://google.com/search?q='+q, verify=False) # se realiza peticion http verify=False para omitir errores de certificado de SSL

    soup = BeautifulSoup(response.content, 'html.parser') # Creamos una nueva instancia de BeautifulSoup con el html obtenido

    descriptions = soup.find_all('div', {'class': 'BNeawe s3v9rd AP7Wnd'}) # Se buscan todos los div que contengan las clases entregadas en segundo parametro del metodo find_all
    if descriptions is not None and len(descriptions) > 0: # Se valida si se obtienen coincidencias en el filtro realizado al html

        print('*****************************************************','Se encontraron los siguientes resultados:', '*****************************************************', sep='\n', end='\n\n\n\n')
        for desc in descriptions: # Se recorren todos los resultados
            if desc.text.rfind('Wikipedia') != -1: # Verifica si existe el texto Wikipedia al final del str
                print(desc.text, end='\n\n\n\n') # imprime el texto
                break # finaliza el ciclo
else:
    print('Debe ingresar solo una palabra')


