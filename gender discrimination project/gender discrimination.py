#Research Analyst Project On Gender Discrimination


import pandas as pd
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

# Predefined fictitious profiles
profiles = [
    {'name': 'Male_Profile_1', 'gender': 'Male'},
    {'name': 'Male_Profile_2', 'gender': 'Male'},
    {'name': 'Male_Profile_3', 'gender': 'Male'},
    {'name': 'Female_Profile_1', 'gender': 'Female'},
    {'name': 'Female_Profile_2', 'gender': 'Female'},
    {'name': 'Female_Profile_3', 'gender': 'Female'}
]

# Create a DataFrame for profiles
profiles_df = pd.DataFrame(profiles)

# Path to your ChromeDriver
chrome_driver_path = '/path/to/chromedriver'

# Setup Chrome options
options = Options()
options.add_argument('--headless')  # Run Chrome in headless mode
options.add_argument('--disable-gpu')

# Setup WebDriver
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)

# Function to log in to Facebook
def facebook_login(driver, email, password):
    driver.get('https://www.facebook.com/login')
    time.sleep(2)

    # Enter email
    email_elem = driver.find_element(By.ID, 'email')
    email_elem.send_keys(email)

    # Enter password
    password_elem = driver.find_element(By.ID, 'pass')
    password_elem.send_keys(password)

    # Click login button
    login_button = driver.find_element(By.NAME, 'login')
    login_button.click()
    time.sleep(5)  # Wait for the login process to complete

# Function to scrape Facebook Marketplace
def scrape_facebook_marketplace(driver, max_price=1000, radius_km=40):
    # Navigate to Facebook Marketplace
    driver.get(f'https://www.facebook.com/marketplace/category/electronics')
    time.sleep(5)  # Wait for the page to load

    # Scroll down to load more items
    for _ in range(5):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

    # Parse the page source with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Find product listings
    products = []
    for listing in soup.find_all('div', {'class': 'x1n2onr6'}):
        try:
            price = listing.find('span', {'class': 'x193iq5w'}).text
            price = int(price.replace('₹', '').replace(',', ''))  # Convert price to integer
            if price <= max_price:
                title = listing.find('span', {'class': 'x4drpdl'}).text
                location = listing.find('span', {'class': 'xod5r1'}).text
                time_posted = listing.find('span', {'class': 'xzih53c'}).text
                link = listing.find('a', {'class': 'x1i10hfl'})['href']
                products.append({'title': title, 'price': price, 'location': location, 'time': time_posted, 'link': link})
        except Exception as e:
            continue  # Skip any listings that cause an error

    return pd.DataFrame(products)

# Function to match buyers with sellers
def match_buyers_with_sellers(profiles_df, sellers_df):
    while True:
        # Randomly select one male and one female profile
        male_buyer = profiles_df[profiles_df['gender'] == 'Male'].sample(1).iloc[0]
        female_buyer = profiles_df[profiles_df['gender'] == 'Female'].sample(1).iloc[0]

        # Confirm selection
        print(f"Selected profiles:\nMale: {male_buyer['name']}\nFemale: {female_buyer['name']}")
        confirmation = input("Type 'yes' to confirm selection: ").strip().lower()
        if confirmation != 'yes':
            continue

        # Log in to Facebook with male profile (assuming you have their credentials)
        facebook_login(driver, male_buyer['name'], 'password_for_male_profile')
        male_marketplace_data = scrape_facebook_marketplace(driver)

        # Log in to Facebook with female profile (assuming you have their credentials)
        facebook_login(driver, female_buyer['name'], 'password_for_female_profile')
        female_marketplace_data = scrape_facebook_marketplace(driver)

        # Combine data from both profiles
        combined_data = pd.concat([male_marketplace_data, female_marketplace_data]).drop_duplicates().reset_index(drop=True)

        # Filter products under 1000 rupees
        sellers_df = combined_data[combined_data['price'] < 1000]

        # Randomly select a seller
        if not sellers_df.empty:
            selected_seller = sellers_df.sample(1).iloc[0]
            print(f"Selected product:\n{selected_seller}")
            print(f"Link: {selected_seller['link']}")
            proceed = input("Type 'yes' to proceed with this product or 'no' to try again: ").strip().lower()
            if proceed == 'yes':
                return {
                    'male_buyer': male_buyer['name'],
                    'female_buyer': female_buyer['name'],
                    'product': selected_seller['title'],
                    'price': selected_seller['price'],
                    'location': selected_seller['location'],
                    'time': selected_seller['time'],
                    'link': selected_seller['link']
                }

# Example usage
email_male = 'male_profile_facebook_email'
password_male = 'male_profile_facebook_password'
email_female = 'female_profile_facebook_email'
password_female = 'female_profile_facebook_password'

# Match buyers with sellers
match = match_buyers_with_sellers(profiles_df, pd.DataFrame())

# Display the matched result
print("Matched Buyers and Product:")
print(match)

# Close the WebDriver
driver.quit()
