from bs4 import BeautifulSoup as soup
import requests
import re
import time
import pandas as pd

# URL for the Blitz.gg champion statistics page
url = "https://blitz.gg/lol/tierlist"

# Send an HTTP GET request to the website
response = requests.get(url)

# Check if the request was successful (status code 200)
Champion_names = []
Corresponding_Win_rate = []

if response.status_code == 200:
    # Parse the HTML content of the page
    soup = soup(response.content, 'html.parser')

    table_container = soup.find('div',{'class':'card-frame card-contents'})
    li_elements = table_container.find_all('li', class_ = "⚡464ba1e1")
    for li_element in li_elements:
        li_elements_2 = li_element.find_all('li', class_ = "⚡e1a31ee0")
        for children in li_elements_2:
            img_element = children.find('img', {"class": "⚡a243cb06 champion-image champion-img"})
            win_rate = children.find("span", {"class" : "type-caption--semi"})
            if img_element and win_rate:
                alt_text = img_element.get('alt')
                win_rate_text = win_rate.text 
                Champion_names.append(alt_text)
                Corresponding_Win_rate.append(win_rate_text)
    
    print("Success")

# Creating Data Frame
data = {'Champion': Champion_names, 'WinRate(%)': Corresponding_Win_rate}

# Create a DataFrame
Champion_Stat = pd.DataFrame(data)

# Remove '%' character from the 'WinRate(%)' column
Champion_Stat['WinRate(%)'] = Champion_Stat['WinRate(%)'].str.replace('%', '')

# Convert 'WinRate(%)' column to numeric (float)
Champion_Stat['WinRate(%)'] = pd.to_numeric(Champion_Stat['WinRate(%)'])

print(Champion_Stat['WinRate(%)'])


#
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from bs4 import BeautifulSoup
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


# # Set up a headless browser using Selenium
# options = webdriver.ChromeOptions()
# options.add_argument("--headless")

# # Initialize the driver with options
# driver = webdriver.Chrome(options=options)

# url = "https://blitz.gg/lol/champions/overview"

# # Load the page
# driver.get(url)

# # Get the initial page source
# page_source = driver.page_source

# # Parse the HTML content of the page
# soup = BeautifulSoup(page_source, 'html.parser')

# # Find all spans with class 'champion-name'
# champion_spans = soup.find_all('span', {'class': 'champion-name'})

# if champion_spans:
#     # Loop through all found spans and print the champion names
#     for champion_span in champion_spans:
#         champion_name = champion_span.text
#         print(f"Champion: {champion_name}")

# # Scroll down the page to trigger additional content loading
# for _ in range(3):  # You may need to adjust the number of scrolls based on the page structure
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
#     # Wait for the next link to be present before proceeding
#     element_present = EC.presence_of_element_located((By.CSS_SELECTOR, '#main-content > div.⚡28fbadf2 > div.⚡de27659b.inner-wrapper-col > div > div > section > div > div > table > tbody > tr:nth-child(21) > td:nth-child(3) > a > span'))
#     WebDriverWait(driver, 10).until(element_present)

#     time.sleep(2)  # Add a delay to allow content to load

# # Get the updated page source
# page_source = driver.page_source

# # Parse the updated HTML content
# soup = BeautifulSoup(page_source, 'html.parser')

# # Find all spans with class 'champion-name' again
# champion_spans = soup.find_all('span', {'class': 'champion-name'})

# if champion_spans:
#     # Loop through all found spans and print the champion names
#     for champion_span in champion_spans:
#         champion_name = champion_span.text
#         print(f"Champion: {champion_name}")
# else:
#     print("No additional champion names found on the page.")

# # Close the browser
# driver.quit()
