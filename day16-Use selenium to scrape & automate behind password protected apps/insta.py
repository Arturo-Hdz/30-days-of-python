# import getpass
# my_password = getpass.getpass("What is your password")
# print(my_password)
from email.mime import base
from fileinput import filename
from urllib.parse import urlparse
import os
import time
import requests
from conf import INSTA_USERNAME, INSTA_PASSWORD
from selenium import webdriver

browser = webdriver.Firefox()

url = "https://www.instagram.com"
browser.get(url)

time.sleep(2)
username_el = browser.find_element_by_name("username")
username_el.send_keys(INSTA_USERNAME)

password_el = browser.find_element_by_name("password")
password_el.send_keys(INSTA_PASSWORD)

time.sleep(1.5)
submit_btn_el = browser.find_element_by_css_selector("button[type='submit']")
submit_btn_el.click()

body_el = browser.find_element_by_css_selector("body")
html_text = body_el.get_attribute("innerHTML")

print (html_text)

#  xpath
# my_button_xpath = "//button"
# browser.find_elements_by_xpath(my_button_xpath)

# my_follow_btn_xpath = "//a[contains(text(), 'Follow')] [not contains(text(), 'Following')]"
# my_follow_btn_xpath = "//button[contains(text(), 'Follow')] [not contains(text(), 'Following')]"

# follow instagram
# def click_to_follow(browser):
#     my_follow_btn_xpath = "//*[contains(text(), 'Follow')] [not contains(text(), 'Following')] [not contains(text(), 'Followers')]"
#     follow_btn_elements = browser.find_elements_by_xpath(my_follow_btn_xpath)
#     for btn in follow_btn_elements:
#        time.sleep(2) #self-throttle
#        try:
#            btn.click()
#        except:
#            pass

# new_user_url = "https://www.instagram.com/ted/"
# browser.get(new_user_url)
# click_to_follow(browser)

time.sleep(2)
the_rock_url = "https://www.instagram.com/therock/"
browser.get(the_rock_url)

post_url_pattern = "https://www.instagram.com/p/<post-slug-id>"
post_xpath_str = "//a[contains(@href, '/p/')]"
post_links = browser.find_elements_by_xpath(post_xpath_str)
post_link_el = None

if len(post_links) > 0:
    post_link_el = post_links[0]
if post_link_el != None:
    post_href = post_link_el.get_attribute("href")
    browser.get(post_href)

video_els = browser.find_elements_by_xpath("//video")
images_els = browser.find_elements_by_xpath("//img")

base_dir = os.path.dirname(os.path.abspath(__file__))
data_dir  = os.path.join(base_dir, "data")
os.makedirs(data_dir, exist_ok=True)

# PIL to verify the size of any given image
def scrape_and_save(elements):
    for el in elements:
       #     print(img.get_attribute('src'))
        url = el.get_attribute('src')
        base_url = urlparse(url).path
       #  print(base_url)
        filename = os.path.basename(base_url)
        filepath = os.path.join(data_dir, filename)
        if os.path.exists(filepath):
           continue
        with requests.get(url,stream=True) as r:
            try:
                r.raise_for_status()
            except:
                continue
            with open(filepath, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)

scrape_and_save(images_els)
scrape_and_save(video_els)

"""
LONG TERM Goal:
Use machine learning to classify the post's 
image or video
and the comment in a revelant fashion
"""
def automate_comment(browser, content='that is cool!'):
    time.sleep(3)
    comment_xpath_str = "//textarea[contains(@placeholder, 'Add a comment')]"
    comment_el = browser.find_element_by_xpath(comment_xpath_str)
    comment_el.send_keys(content)
    submit_btns_xpath = "button[type='submit']"
    submit_btns_els = browser.find_element_by_css_selector(submit_btns_xpath)
    time.sleep(2)
    for btn in submit_btns_els:
       try:
           btn.click()
       except:
           pass

def automate_likes(browser):
    like_heart_svg__xpath = "//*[contains(@aria-label, 'Like')]"
    all_like_hearts_elements = browser.find_elements_by_xpath(like_heart_svg__xpath)
    max_heart_h = -1
    for heart_el in all_like_hearts_elements:
       print(heart_el.get_attribute("height"))
       h = heart_el.get_attribute("height")
       current_h = int(h)
       if current_h > max_heart_h:
           max_heart_h = current_h

       # like_heart_svg__xpath = "//*[contains(@aria-label, 'Like')]"
    all_like_hearts_elements = browser.find_elements_by_xpath(like_heart_svg__xpath)
    print(max_heart_h)
    for heart_el in all_like_hearts_elements:
       print(heart_el.get_attribute("height"))
       h = heart_el.get_attribute("height")
       if h == max_heart_h or h == f"{max_heart_h}":
           parent_button = heart_el.find_element_by_xpath('..')
           print(parent_button)
           time.sleep(2)
           try:
              parent_button.click()
           except:
              pass