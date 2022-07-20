import requests
import json
from bs4 import BeautifulSoup

SOLOAUTOS_LINK = "https://soloautos.mx/vehiculos/?q=(And.TipoVeh%C3%ADculo.Autos._.(C.Marca.Chevrolet._.Modelo.Camaro.)_.Ano.range(2010..2015)._.Cilindros.8.)"
headers = {
    "Accept-Language": "en-US,en;q=0.9,es-419;q=0.8,es;q=0.7,gl;q=0.6",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}

response = requests.get(url=SOLOAUTOS_LINK, headers=headers)
pagina = response.text
soup = BeautifulSoup(pagina, "html.parser")

lista_modelos = []
modelos = soup.find_all(name="h3")

for modelo in modelos:
    if "Camaro" in modelo.getText():
        m = modelo.getText().strip()
        lista_modelos.append(m)

lista_precios = []
precios = soup.find_all(class_="price")
for precio in precios:
    p = precio.getText().split()[0].strip("$").replace(",", "")
    lista_precios.append(p)

a = soup.select(".price a")

links = []
for link in a:
    href = link["href"]
    if "http" not in href:
        links.append(f"https://www.soloautos.com.mx{href}")
    else:
        links.append(href)

for car in range(len(lista_modelos)):
    data = {
        car: {
            "modelo": lista_modelos[car],
            "precio": lista_precios[car],
            "link": links[car]
        }
    }
    try:
        with open("data.json", mode="r") as file:
            ndata = json.load(file)
    except FileNotFoundError:
        with open("data.json", mode="w") as file:
            json.dump(data, file, indent=4)
    else:
        ndata.update(data)
        with open("data.json", mode="w") as file:
            json.dump(ndata, file, indent=4)
