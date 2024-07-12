from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query = "laptop"
file = 0
for i in range(1, 2):
    driver.get(f"https://www.amazon.com/s?k={query}&page={i}&crid=374UTLWJJWSI9&sprefix=%2Caps%2C462&ref=nb_sb_ss_recent_1_0_recent")
    elems = driver.find_elements(By.CLASS_NAME, "s-widget-container")
    print(f"{len(elems)} items found")
    for elem in elems:
        d = elem.get_attribute("outerHTML")
        with open(f"data/{query}_{file}.html", "w", encoding="utf-8") as f:
            f.write(d)
            file += 1
            
    time.sleep(10)
driver.close()
