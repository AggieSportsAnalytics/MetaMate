#
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

# Initialize the Chrome driver


# Set the URL
url = "https://blitz.gg/lol/champions/overview"
# Set the path to the uBlock Origin extension
ublock_path = r"C:\Users\Harry Trinh\uBlock-Origin.crx"

# Configure Chrome options and add the uBlock Origin extension
chrome_options = Options()
chrome_options.add_extension(ublock_path)

# Initialize the Chrome driver with options
driver = webdriver.Chrome(options=chrome_options)

# Load the page
driver.get(url)

# Wait until the page is fully loaded (adjust the timeout as needed)
try:
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'span.champion-name')),
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div.cell.type-body2-form--bold'))
    )
    print("Success")
except Exception as e:
    print(f"Error waiting for page to load: {e}")
    driver.quit()
    exit()

# Get the initial page height
previous_height = driver.execute_script('return document.body.scrollHeight')
print("Success")

# Scroll down until reaching the bottom of the page
while True:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    print("Success1")
    time.sleep(30)  # Adjust the sleep time based on your page loading speed

    # Get the new page height
    new_height = driver.execute_script('return document.body.scrollHeight')
    print("Success1")

    # Break the loop if scrolling doesn't change the height (indicating the end of the page)
    if new_height == previous_height:
        print("Success2")
        break

    # Update the previous height for the next iteration
    previous_height = new_height
    print("Success1")


# Print all span elements with class "champion-name"
champion_spans = driver.find_elements(By.CSS_SELECTOR, 'span.champion-name')
champion_names = [champion_span.text for champion_span in champion_spans]

# Get all elements with class "cell type-body2-form--bold" containing percentage values using XPath
percentage_elements = driver.find_elements(By.XPATH, '//div[contains(@class, "cell type-body2-form--bold") and contains(text(), "%")]')

# Extract the text from the elements
percentage_values = [element.text for element in percentage_elements]
win_rate = percentage_values[0::3]
ban_rate = percentage_values[1::3]
pick_rate = percentage_values[2::3]


# Quit the driver
driver.quit()

# Creating Data Frame
data = {'Champion': champion_names, 'WinRate(%)': win_rate,'BanRate(%)': ban_rate, 'PickRate(%)': pick_rate, }

# Create a DataFrame
Champion_Stat = pd.DataFrame(data)

# Remove '%' character from the 'WinRate(%)' column
Champion_Stat['WinRate(%)'] = Champion_Stat['WinRate(%)'].str.replace('%', '')

# Convert 'WinRate(%)' column to numeric (float)
Champion_Stat['WinRate(%)'] = pd.to_numeric(Champion_Stat['WinRate(%)'])
# Remove '%' character from the 'WinRate(%)' column
Champion_Stat["BanRate(%)"] = Champion_Stat['BanRate(%)'].str.replace('%', '')

# Convert 'WinRate(%)' column to numeric (float)
Champion_Stat['BanRate(%)'] = pd.to_numeric(Champion_Stat['BanRate(%)'])
# Remove '%' character from the 'WinRate(%)' column
Champion_Stat['PickRate(%)'] = Champion_Stat['PickRate(%)'].str.replace('%', '')

# Convert 'WinRate(%)' column to numeric (float)
Champion_Stat['PickRate(%)'] = pd.to_numeric(Champion_Stat['PickRate(%)'])


print(Champion_Stat)