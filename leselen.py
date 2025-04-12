import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

product_name=input("ürün ismi giriniz.")

url = f"https://www.aliexpress.com/wholesale?SearchText={product_name}"

driver = webdriver.Chrome()

driver.get(url)

element = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div/div[2]/div/div[2]/div[2]/div[2]/span[3]')
element.click()

page_source=driver.page_source
soup = BeautifulSoup(page_source, "html.parser")

product_links = soup.find_all("a", {"class" : "manhattan--container--1lP57Ag cards--list--2-tE5ph search-card-item"})




driver.quit()

# Ürün sayfasının kaynağını alın
"""toplam_url = f"https:{product_url}"
    response = requests.get(toplam_url)"""
