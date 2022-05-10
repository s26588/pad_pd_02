from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://www.pap.pl/')

# a)
cookies = driver.find_element(by=By.XPATH, value='//*[@id="cookie"]/div/div/div/div/div/div[1]')
cookies.click()

# b)
driver.maximize_window() # zwiekszamy wielkosc okna

time.sleep(2)

# c)
englishLang = driver.find_element(by=By.XPATH, value='//*[@id="navbar"]/ul[2]/li[3]/a')
englishLang.click()

# d)
businnes = driver.find_element(by=By.XPATH, value='//*[@id="block-mainnavigationen"]/ul/li[3]/a')
businnes.click()

# e)
titlesElems = driver.find_elements(by=By.CSS_SELECTOR, value=".title")
titles = []

for title in titlesElems:
  titles.append(title.text)

# print(titles)

# f)
images = driver.find_elements(By.CSS_SELECTOR, value=".newsList img")
for i, image in enumerate(images):
  with open(f'{i}.png', 'wb') as file:
    file.write(image.screenshot_as_png)

# g)
lastPage = driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/section[2]/div/div[2]/div[1]/div[2]/div/nav/ul/li[5]/a')
driver.execute_script("arguments[0].scrollIntoView(true);", lastPage);
driver.execute_script("window.scrollTo(0, scrollY - 100);");

# h)
lastPage.click()
activePage = driver.find_element(by=By.CSS_SELECTOR, value='.pager__item.active')

driver.execute_script("arguments[0].scrollIntoView(true);", activePage);
driver.execute_script("window.scrollTo(0, scrollY - 100)");

print(activePage.text)

driver.quit()