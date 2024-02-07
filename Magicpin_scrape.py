import requests
from bs4 import BeautifulSoup

def scrape_menu(url):
    """
    Scrape the Magicpin website to extract the food menu and price details as mentioned in the task
    i have just used BeautifulSoup here

    Args:
    - url (str): The URL of the Magicpin website.

    Returns:
    - dict: A dictionary containing menu items as keys and their respective prices as values.

    i havent handled or written any error handling mechanism because i had no problem fetching the info 
    success code : 200

    """
    # This is the code to fetch webpage content
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Finding  all sections with class 'categoryItemHolder' to scrape perticular item
    #i got to know the class name from the websites page sourse so its easy to fetch content under that
    menu_sections = soup.find_all('section', class_='categoryItemHolder')

    # Initializing a dictionary to store menu details for proper formating
    menu_details = {}

    # Extract menu items and prices
    for section in menu_sections:
        item_name = section.find('a', class_='itemName').text.strip()
        item_price = section.find('span', class_='itemPrice').text.strip()
        menu_details[item_name] = item_price

    return menu_details

def main():
    # URL of the Magicpin website
    url = 'https://magicpin.in/New-Delhi/Paharganj/Restaurant/Eatfit/store/61a193/delivery/'

    # Scrape the menu
    menu = scrape_menu(url)

    # Print the menu details
    for item, price in menu.items():
        print(f"{item} - {price}")

if __name__ == "__main__":
    main()


#Hope my code is satisfactory for the team....Thankyou...
    #                                                 ------Kirandeep.k