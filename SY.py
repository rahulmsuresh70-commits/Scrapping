from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://books.toscrape.com/")
title = driver.title
books = driver.find_elements(By.CSS_SELECTOR, "article.product_pod h3 a")

with open("books.txt", "w", encoding="utf-8") as file:

    file.write("Website Title: " + title + "\n\n")

    for book in books:
        file.write(book.get_attribute("title") + "\n")


driver.quit()

print("Scraping completed successfully!")