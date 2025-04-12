import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def search_product(product_name):
    # AliExpress arama URL'i
    url = f"https://www.aliexpress.com/wholesale?SearchText={product_name}"
    
    # WebDriver seçeneklerini ayarlayın
    options = Options()
    options.add_argument("--window-size=1920x1080")
    
    # WebDriver'ı başlatın
    driver = webdriver.Chrome(options=options)
    
    # Arama sayfasını açın
    driver.get(url)
    
    # Sayfayı yükleme için biraz bekleyin
    time.sleep(2)
    
    driver.find_element(By.CLASS_NAME,'comet-icon comet-icon-viewlist sort--icon--3K4SrhS').click

    # Sayfanın kaynağını alın
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, "html.parser")
    
    # Ürün bağlantılarını bulun
    product_links = soup.find_all("a", {"class":"manhattan--container--1lP57Ag cards--list--2-tE5ph search-card-item"})
    
    for link in product_links:
        print(link)



if __name__ == "__main__":
    product_name = input("Aranacak ürünü girin: ")
    video_product_links = search_product(product_name)
    
    if video_product_links:
        print("Videolu ürün sayfaları:")
        for link in video_product_links:
            print(link)
    else:
        print("Videolu ürün bulunamadı.")
        