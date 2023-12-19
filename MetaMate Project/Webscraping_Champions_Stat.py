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

buttons  = driver.find_elements(By.CSS_SELECTOR, 'button[data-tip]')
print("Success")

# Dictionary to store data for each role
role_data = {}

for i in range(len(buttons)):
    # Find buttons again to avoid StaleElementReferenceException
    buttons = driver.find_elements(By.CSS_SELECTOR, 'button[data-tip]')

    # Click the button to activate it
    buttons[i].click()

    # Wait until the button is active (assuming the button's state changes)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[@data-tip and @data-active="true"]'))
    )

    # Print the role information
    role = buttons[i].get_attribute('data-tip')
    print(f"Role: {role}")

    # Sleep for 10 seconds to allow time for the page to load and data to be scraped
    time.sleep(5)

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
    
    # Create a DataFrame for the current role
    role_df = pd.DataFrame({
        'Champion': champion_names,
        'WinRate(%)': win_rate,
        'BanRate(%)': ban_rate,
        'PickRate(%)': pick_rate,
    })

    # Use separate variables for each role's DataFrame
    if role == 'All':
        all_role_df = role_df
    elif role == 'Top':
        top_role_df = role_df
    elif role == 'Jungle':
        jungle_role_df = role_df
    elif role == 'Mid':
        mid_role_df = role_df
    elif role == 'ADC':
        adc_role_df = role_df
    elif role == 'Support':
        support_role_df = role_df

# Quit the driver
driver.quit()


print("\nRole: Top")
top_role_df['WinRate(%)'] = top_role_df['WinRate(%)'].str.replace('%', '')
top_role_df['WinRate(%)'] = pd.to_numeric(top_role_df['WinRate(%)'])
top_role_df["BanRate(%)"] = top_role_df['BanRate(%)'].str.replace('%', '')
top_role_df['BanRate(%)'] = pd.to_numeric(top_role_df['BanRate(%)'])
top_role_df['PickRate(%)'] = top_role_df['PickRate(%)'].str.replace('%', '')
top_role_df['PickRate(%)'] = pd.to_numeric(top_role_df['PickRate(%)'])
print(top_role_df)


print("\nRole: Jungle")
jungle_role_df['WinRate(%)'] = jungle_role_df['WinRate(%)'].str.replace('%', '')
jungle_role_df['WinRate(%)'] = pd.to_numeric(jungle_role_df['WinRate(%)'])
jungle_role_df["BanRate(%)"] = jungle_role_df['BanRate(%)'].str.replace('%', '')
jungle_role_df['BanRate(%)'] = pd.to_numeric(jungle_role_df['BanRate(%)'])
jungle_role_df['PickRate(%)'] = jungle_role_df['PickRate(%)'].str.replace('%', '')
jungle_role_df['PickRate(%)'] = pd.to_numeric(jungle_role_df['PickRate(%)'])
print(jungle_role_df)


print("\nRole: Mid")
mid_role_df['WinRate(%)'] = mid_role_df['WinRate(%)'].str.replace('%', '')
mid_role_df['WinRate(%)'] = pd.to_numeric(mid_role_df['WinRate(%)'])
mid_role_df["BanRate(%)"] = mid_role_df['BanRate(%)'].str.replace('%', '')
mid_role_df['BanRate(%)'] = pd.to_numeric(mid_role_df['BanRate(%)'])
mid_role_df['PickRate(%)'] = mid_role_df['PickRate(%)'].str.replace('%', '')
mid_role_df['PickRate(%)'] = pd.to_numeric(mid_role_df['PickRate(%)'])
print(mid_role_df)

print("\nRole: ADC")
adc_role_df['WinRate(%)'] = adc_role_df['WinRate(%)'].str.replace('%', '')
adc_role_df['WinRate(%)'] = pd.to_numeric(adc_role_df['WinRate(%)'])
adc_role_df["BanRate(%)"] = adc_role_df['BanRate(%)'].str.replace('%', '')
adc_role_df['BanRate(%)'] = pd.to_numeric(adc_role_df['BanRate(%)'])
adc_role_df['PickRate(%)'] = adc_role_df['PickRate(%)'].str.replace('%', '')
adc_role_df['PickRate(%)'] = pd.to_numeric(adc_role_df['PickRate(%)'])
print(adc_role_df)



print("\nRole: Support")
support_role_df['WinRate(%)'] = support_role_df['WinRate(%)'].str.replace('%', '')
support_role_df['WinRate(%)'] = pd.to_numeric(support_role_df['WinRate(%)'])
support_role_df["BanRate(%)"] = support_role_df['BanRate(%)'].str.replace('%', '')
support_role_df['BanRate(%)'] = pd.to_numeric(support_role_df['BanRate(%)'])
support_role_df['PickRate(%)'] = support_role_df['PickRate(%)'].str.replace('%', '')
support_role_df['PickRate(%)'] = pd.to_numeric(support_role_df['PickRate(%)'])
print(support_role_df)

top_role_df.to_csv(r"C:\Users\Harry Trinh\Documents\GitHub\MetaMate\MetaMate Project\top.csv",index=False)
jungle_role_df.to_csv(r"C:\Users\Harry Trinh\Documents\GitHub\MetaMate\MetaMate Project\jungle.csv",index=False)
mid_role_df.to_csv(r"C:\Users\Harry Trinh\Documents\GitHub\MetaMate\MetaMate Project\mid.csv",index=False)
adc_role_df.to_csv(r"C:\Users\Harry Trinh\Documents\GitHub\MetaMate\MetaMate Project\adc.csv",index=False)
support_role_df.to_csv(r"C:\Users\Harry Trinh\Documents\GitHub\MetaMate\MetaMate Project\sup.csv", index=False)
