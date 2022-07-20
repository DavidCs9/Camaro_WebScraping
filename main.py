import json

from selenium import webdriver
from selenium.webdriver.common.by import By

GOOGLE_FORM_LINK = "https://forms.gle/vr2w8mfFknjZETKE6"
chrome_driver_path = r"C:\Users\david\Development\chromedriver.exe"
with open("data.json", mode="r") as file:
    data = json.load(file)

driver = webdriver.Chrome(chrome_driver_path)
driver.get(GOOGLE_FORM_LINK)

for car in range(len(data)):
    modelo = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    modelo.send_keys(data[f'{car}']['modelo'])

    precio = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    precio.send_keys(data[f'{car}']['precio'])

    link = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link.send_keys(data[f'{car}']['link'])

    btn = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
    btn.click()

    otra_respuesta_boton = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    otra_respuesta_boton.click()

