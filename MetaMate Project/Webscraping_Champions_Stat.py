from bs4 import BeautifulSoup as soup
import requests
import re
import time

# URL for the Blitz.gg champion statistics page
url = "https://blitz.gg/lol/tierlist"

# Send an HTTP GET request to the website
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = soup(response.content, 'html.parser')

    table_container = soup.find('div',{'class':'card-frame card-contents'})
    li_elements = table_container.find_all('li', class_ = "⚡464ba1e1")
    for li_element in li_elements:
        li_elements_2 = li_element.find_all('li', class_ = "⚡e1a31ee0")
        for children in li_elements_2:
            img_element = children.find('img', {"class": "⚡a243cb06 champion-image champion-img"})
            if img_element:
                alt_text = img_element.get('alt')
                print(f"Champion: {alt_text}")
    
    print("Success")




# Reference Later on
#     if table_container:
#         print("Success")
#         # Find the <tbody> tag within the "table-container"
#         tbody = table_container.find('tbody')
#         if tbody:
#             print("Success")
#             # Extract champion names from each <td> tag within <tbody>
#             champion_names = [td.find('span', class_='champion-name').text.strip() for td in tbody.find_all('a', class_='cell type-body2-form--bold champion-meta')]
#             print(champion_names)
#             # Print the extracted champion names
#             for champion_name in champion_names:
#                 print(f"Champion Name: {champion_name}")
#         else:
#             print("Unable to find <tbody> tag.")
#     else:
#         print("Unable to find div with class 'table-container'.")
# else:
#     print(f"Failed to retrieve data. Status code: {response.status_code}")

    # Extract the relevant information, e.g., champion names, win rates, pick rates, etc.
    # This will depend on the specific structure of the website's HTML.
    # Use browser developer tools to inspect the HTML structure and identify the elements you need.
#     champion_link = soup.find('a', class_='cell type-body2-form--bold champion-meta')
#     champion_name = champion_link.find('span', class_='champion-name').text.strip()
#     champion_role = champion_link['href'].split('=')[-1]
#     image_url = soup.find('img', class_='⚡a243cb06 champion-img')['src']
#     #wr = soup.find('div', class_='cell type-body2-form--bold').text.strip()
#     win_rates = [rate.text for rate in soup.find_all("div", class_="cell type-body2-form--bold")]
#     print(f"Champion Name: {champion_name}")
#     print(f"Champion Role: {champion_role}")
    
#     print(f"Champion Wr: {win_rates}")
#     # Print the extracted data
#     #for name, win_rate in zip(champion_names, win_rates):
#         #print(f"Champion: {name}, Win Rate: {win_rate}")
# else:
#     print(f"Failed to retrieve data. Status code: {response.status_code}")