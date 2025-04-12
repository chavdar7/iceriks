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

    element = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div/div[2]/div/div[2]/div[2]/div[2]/span[3]')
    element.click()
    
    # Videolu ürün sayfalarını depolamak için liste oluşturun
    video_product_links = []
    
    # 10 tane videolu ürün bulana kadar devam edin
    while len(video_product_links) < 5:
        # Sayfanın kaynağını alın
        page_source = driver.page_source
        
        # Ürün bağlantılarını bulun
        product_links = driver.find_elements(By.CLASS_NAME, "manhattan--container--1lP57Ag cards--list--2-tE5ph search-card-item")
        
        # Ürün sayfalarını kontrol edin ve videolu olanları bulun
        for link in product_links:
            product_url = link.get_attribute["href"]
            if has_video(driver, product_url):
                video_product_links.append(product_url)
            
            # 10 tane videolu ürün bulunduğunda döngüyü durdurun
            if len(video_product_links) == 5:
                break
        
        # Sayfalama için "Next" düğmesini tıklayın
        next_button = driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/div/div[2]/div/div[2]/div[4]/div[1]/ul/li[9]')
        if next_button:
            next_button.click()
            time.sleep(2)
        else:
            break
    
    # WebDriver'ı kapatın
    driver.quit()
    
    return video_product_links

def has_video(driver, product_url):
    # Ürün sayfasını açın
    driver.get(product_url)
    
    # Sayfayı yükleme için biraz bekleyin
    time.sleep(2)
    
    # Sayfa içinde video etiketi (video) var mı kontrol edin
    video_element = driver.find_elements(By.TAG_NAME, 'video')
    
    return len(video_element) > 0

if __name__ == "__main__":
    product_name = input("Aranacak ürünü girin: ")
    video_product_links = search_product(product_name)
    
    if video_product_links:
        print("Videolu ürün sayfaları:")
        for link in video_product_links:
            print(link)
    else:
        print("Videolu ürün bulunamadı.")

#commitlemem gerek