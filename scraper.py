from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd
import csv

START_URL = "https://exoplanets.nasa.gov/exoplanet-catalog/"
browser = webdriver.Edge("C:\\Users\\Sreekesh\\Desktop\\WHJ\\PYTHON\\1on4\\C141\\C141TA\\msedgedriver.exe")

browser.get(START_URL)
time.sleep(10)
planets_data = []

def scrape():

    for i in range(0,490):
        
        soup = BeautifulSoup(browser.page_source, "html.parser")
        # print(f'Scrapping page {i+1} ...' )
        
        for ul_tag in soup.find_all("ul", attrs={"class", "exoplanet"}):

            li_tags = ul_tag.find_all("li")
            temp_list = []

            for index, li_tag in enumerate(li_tags):

                if index == 0:                   
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")

            planets_data.append(temp_list)
        browser.find_element(by=By.XPATH, value='//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    # with open("scraper2.csv","w") as f:
    #     csvwriter = csv.writer(f)
    #     csvwriter.writerow(headers)
    #     csvwriter.writerows(planets_data)
    # print(planets_data[1])
            
            
scrape()         
headers = ["name", "light_years_from_earth", "planet_mass", "stellar_magnitude", "discovery_date"]


# Define pandas DataFrame   
planet_df_1 = pd.DataFrame(planets_data, columns=headers)

# # Convert to CSV
planet_df_1.to_csv('scraped_data.csv',index=True, index_label="id")
