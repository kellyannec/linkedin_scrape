# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 14:43:08 2021

@author: Kelly
"""


# imports
import parameters
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
from parsel import Selector

# function to ensure all key data fields have a value
def validate_field(field): 
    #if field is present pass 
    if field is None:
        field = 'No results'
        return field
    else:
        return field

# defining new variable passing two parameters
writer = csv.writer(open(parameters.file_name, 'w'))

# writerow() method to the write to the file object
writer.writerow(['Name', 'Headline', 'Company', 'Position', 'School', 'Program', 'Location', 'URL'])

# specifies the path to the chromedriver.exe
driver = webdriver.Chrome('C:\ProgramData\Bin\chromedriver')

# driver.get method() will navigate to a page given by the URL address
driver.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')

# sleep for 0.5 seconds
sleep(0.5)

# locate email form by_class_name
username = driver.find_element_by_id('username')

# send_keys() to simulate key strokes
username.send_keys(parameters.linkedin_username)

# sleep for 0.5 seconds
sleep(0.5)

# locate password form by_class_name
password = driver.find_element_by_id('password')

# send_keys() to simulate key strokes
password.send_keys(parameters.linkedin_password)

# sleep for 0.5 seconds
sleep(0.5)

# locate submit button by_xpath
sign_in_button = driver.find_element_by_xpath('//*[@type="submit"]')

# .click() to mimic button click
sign_in_button.click()

# sleep for 0.5 seconds
sleep(0.5)

#locate remember me button by class name
remember_me_button = driver.find_element_by_class_name('btn__primary--large')

#.click() to mimic button click
remember_me_button.click()

#sleep for 0.5 seconds
sleep(0.5)

#open google
driver.get('https:www.google.com')
sleep(3)

#search
search_query = driver.find_element_by_name('q')
search_query.send_keys(parameters.search_query)
sleep(0.5)


search_query.send_keys(Keys.RETURN)
sleep(3)

#extract URLS from google results
linkedin_urls = driver.find_elements_by_css_selector('div > div > div.yuRUbf > a')
linkedin_urls = [url.get_attribute('href') for url in linkedin_urls]
#linkedin_urls = [url.text for url in linkedin_urls]
sleep(0.5)


# linkedin_urls

# linkedin_urls = [url.text for url in linkedin_urls]
# sleep(0.5)


# For loop to iterate over each URL in the list
for linkedin_url in linkedin_urls:

    # get the profile URL 
    driver.get(linkedin_url)
  
   

    # add a 5 second pause loading each URL
    sleep(5)

    # assigning the source code for the webpage to variable sel

    sel = Selector(text=driver.page_source)

    name = sel.xpath('//*[@class = "inline t-24 t-black t-normal break-words"]/text()').extract_first().split()
    name = ' '.join(name)

    headline = sel.xpath('//*[@class = "mt1 t-18 t-black t-normal break-words"]/text()').extract_first().split()
    headline = ' '.join(headline)


#problems
    experience = sel.xpath('//*[@class = "t-16 t-black t-bold"]/text()').extract_first()
    experience = ' '.join(experience.split()) if experience else None
    company = sel.xpath('//*[@class = "pv-entity__secondary-title t-14 t-black t-normal"]/text()').extract_first()
    company = ' '.join(company.split()) if company else None
    school = sel.xpath('//*[@class = "pv-entity__school-name t-16 t-black t-bold"]/text()').extract_first()
    school = ' '.join(school.split()) if school else None
    program = sel.xpath('//*[@class = "pv-entity__comma-item"]/text()').extract_first()
    program = ' '.join(program.split()) if program else None
    location = sel.xpath('//*[@class = "t-16 t-black t-normal inline-block"]/text()').extract_first()
    location = ' '.join(location.split()) if location else None

    url = driver.current_url
    
    #validating if the fields exist on the profile
    name = validate_field(name)
    headline = validate_field(headline)
    company = validate_field(company)
    experience = validate_field(experience)
    school = validate_field(school)
    program = validate_field(program)
    location = validate_field(location)
    url = validate_field(url)

    print('\n')
    print('Name: ', name)
    print('Headline: ', headline)
    print('Company: ', company)
    print('Position: ', experience)
    print('School: ', school)
    print('Program: ', program)
    print('Location: ', location)
    print('URL: ', url)
    print('\n')

    writer.writerow([name,
                  headline,
                  company.encode('utf-8'),
                  experience.encode('utf-8'),
                  school.encode('utf-8'),
                  program.encode('utf-8'),
                  location.encode('utf-8'),
                  url.encode('utf-8')])



# driver.quit()
