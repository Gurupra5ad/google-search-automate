from selenium import webdriver 
import time

browser = webdriver.Chrome('/home/disciple/chromedriver')

browser.get('https://www.google.com')

time.sleep(2)

search_input = browser.find_element_by_name('q')
input_field = input("What do you want to search in google ?")
search_input.send_keys(input_field)

time.sleep(2)

submit_button = browser.find_element_by_css_selector('input[type ="submit"]')
submit_button.click()



