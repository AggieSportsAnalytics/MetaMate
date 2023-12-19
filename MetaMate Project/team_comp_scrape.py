import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

def scrape_game(url):
    # Set the path to the uBlock Origin extension
    ublock_path = r"C:\Users\Harry Trinh\uBlock-Origin.crx"

    # Configure Chrome options and add the uBlock Origin extension
    chrome_options = Options()
    chrome_options.add_extension(ublock_path)

    # Initialize the Chrome driver with options
    driver = webdriver.Chrome(options=chrome_options)

    # Load the page
    driver.get(url)

    # Get the initial page height
    previous_height = driver.execute_script('return document.body.scrollHeight')
    print("Success")

    # Find all img tags with the class name "champion_icon_medium"
    ban_tags = driver.find_elements(By.CLASS_NAME, "champion_icon_medium")
    new_ban_tags_from_website = driver.find_elements(By.CLASS_NAME, "champion_icon_medium rounded-circle")

    # Lists to store champion names for ban and pick
    ban_champions = []
    pick_champions = []

    # Iterate through the img tags and extract champion names
    for img_tag in ban_tags:
        champion_name = img_tag.get_attribute("alt")
        # Check if the alt attribute is not empty
        if champion_name:
            # print("Ban Champion Name:", champion_name)
            ban_champions.append(champion_name)
        else:
            src = img_tag.get_attribute("src")
            champion_name = src.split("/")[-1].split(".")[0]
            # print("Pick Champion Name:", champion_name)
            pick_champions.append(champion_name)
    # Create a DataFrame
    df = pd.DataFrame({"Ban": [ban_champions[i:i+5] for i in range(0, len(ban_champions), 5)],
                       "Pick": [pick_champions[i:i+5] for i in range(0, len(pick_champions), 5)]})

    # Print the DataFrame

    # Quit the driver
    driver.quit()
    
    return df

# # Set the URL
# url = "https://gol.gg/tournament/tournament-matchlist/Worlds%20Main%20Event%202023/"

# # Set the path to the uBlock Origin extension if needed
# ublock_path = r"C:\Users\Harry Trinh\uBlock-Origin.crx"

# # Configure Chrome options and add the uBlock Origin extension
# chrome_options = Options()
# chrome_options.add_extension(ublock_path)

# # Initialize the Chrome driver with options
# driver = webdriver.Chrome(options=chrome_options)

# # Load the page
# driver.get(url)

# # List of game URLs
game_urls = ["https://gol.gg/game/stats/53622/page-summary/",
             "https://gol.gg/game/stats/53618/page-summary/",
             "https://gol.gg/game/stats/53613/page-summary/",
             "https://gol.gg/game/stats/53610/page-summary/",
             "https://gol.gg/game/stats/53605/page-summary/",
             "https://gol.gg/game/stats/53600/page-summary/",
             "https://gol.gg/game/stats/53595/page-summary/",
             "https://gol.gg/game/stats/53592/page-summary/",
             "https://gol.gg/game/stats/53589/page-summary/",
             "https://gol.gg/game/stats/53586/page-summary/",
             "https://gol.gg/game/stats/53584/page-summary/",
             "https://gol.gg/game/stats/53581/page-summary/",
             "https://gol.gg/game/stats/53578/page-summary/",
             "https://gol.gg/game/stats/53575/page-summary/",
             "https://gol.gg/game/stats/53572/page-summary/",
             "https://gol.gg/game/stats/53569/page-summary/",
             "https://gol.gg/game/stats/53567/page-summary/",
             "https://gol.gg/game/stats/53564/page-summary/"]

# # Find all <a> tags within <td> tags with the specified class
# link_tags = driver.find_elements(By.CSS_SELECTOR, 'td.text-left.footable-visible.footable-first-column a')

# # Extract the href attribute from each <a> tag
# links = [link.get_attribute('href') for link in link_tags]

# # Print the extracted links
# for link in links:
#     print(link)
#     game_urls.append(str(link))

# # Quit the driver
# driver.quit()

# Scrape each game
dfs = []

# Scrape each game and append the DataFrame to the list
for game_url in game_urls:
    df = scrape_game(game_url)
    dfs.append(df)

# Concatenate all DataFrames in the list into one along the rows
final_df = pd.concat(dfs, axis=0, ignore_index=True)

# Print the final DataFrame
print(final_df)

# save to csv file
final_df.to_csv(r"C:\Users\Harry Trinh\Documents\GitHub\MetaMate\MetaMate Project\World23_MainEvents_comp.csv",index=False)