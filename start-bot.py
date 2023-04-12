import random
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

queries = [
    "list1",
    "list2",
    "list3",
    "dst"
]

target_url = "https://www.example.com"

num_iterations = 50

delay_between_iterations = 90

current_query_index = 0

for i in range(num_iterations):
    while True:
        query = queries[current_query_index]
        driver = webdriver.Chrome()
        driver.get("https://www.google.com/")
        search_box = driver.find_element_by_name("q")
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)
        time.sleep(random.randint(20, 50))
        try:
            next_page_button = driver.find_element_by_link_text("Berikutnya")
            next_page_button.click()
        except:
            pass

        time.sleep(random.randint(20, 50))

        search_results = driver.find_elements_by_css_selector("div.r")
        for result in search_results:
            link = result.find_element_by_tag_name("a")
            href = link.get_attribute("href")
            if target_url in href:
                link.click()
                break

        time.sleep(random.randint(20, 50))
        driver.quit()

        current_query_index += 1

        if current_query_index == len(queries):
            current_query_index = 0

        time.sleep(random.randint(20, 50))

        if current_query_index == 0:
            break

    time.sleep(delay_between_iterations)
