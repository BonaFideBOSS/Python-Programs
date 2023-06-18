from selenium import webdriver
import time
number_of_drivers = int(input("Views : " ))
url = input("URL : " )
drivers =[]
wait = 3
if "twitter.com" in url:
    wait = 5
elif "youtube.com" in url:
    wait = 30
for i in range(number_of_drivers):
    drivers.append(webdriver.Chrome(executable_path = "C:\Program Files\Google\Chrome\chromedriver.exe"))
    drivers[i].get(url)
    time.sleep(wait)
    drivers[i].quit()
