from selenium import webdriver
import time
from concurrent.futures import ThreadPoolExecutor


def wait_for(url):
    wait = 5
    if "youtube.com" in url:
        wait = 30
    return wait


def add_views(url):
    try:
        webdriver_path = "C:\Program Files\Google\Chrome\chromedriver.exe"
        options = webdriver.ChromeOptions()
        options.headless = False
        browser = webdriver.Chrome(executable_path=webdriver_path, options=options)
        browser.get(url)
        time.sleep(wait_for(url))
        browser.quit()
    except:
        pass


def thread_pool(url, views):
    urls = [url] * views
    with ThreadPoolExecutor() as thread:
        thread.map(add_views, urls)


def get_user_input():
    url = input("URL : ")
    views = int(input("Views : "))
    thread_pool(url, views)


get_user_input()
