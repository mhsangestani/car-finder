# import necessary libraries
import requests
import database
from bs4 import BeautifulSoup

# initialize a counter for logging
c = 0

# loop through pages 1 to 20 of the website
for num_page in range(1,21):
    # convert page number to string and format URL
    num_page = str(num_page)
    url = f'https://www.truecar.com/used-cars-for-sale/listings/?page={num_page}&sort[]=best_match'
    
    # send a GET request to the URL
    response = requests.get(url)
    print(response)
    
    # parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # find all car information cards on the page
    cards = soup.find_all(attrs={"card-content vehicle-card-body order-3"})
    
    # loop through each card and extract relevant information
    for card in cards:
        # extract car name
        name = card.find(attrs={"vehicle-header-make-model text-truncate"})
        name = str(name.text)
        
        # extract car price
        price = card.find(attrs={"padding-left-3 vehicle-card-bottom-pricing-secondary vehicle-card-bottom-max-50"})
        price = str(price.text)
        price = price.split('$')[1] # extract just the price
        price = price.replace(',', '') # remove commas from price
        
        # extract car miles
        miles = card.find(attrs={"d-flex w-100 justify-content-between"})
        miles = str(miles.text)
        miles = miles.split('Upfront Price Available' )[0]
        miles = miles.split('Discount Available')[0]
        miles = miles.split(' miles')[0]
        miles = miles.replace(',', '') # remove commas from miles
        
        # create a list of car information to add to the database
        list_Information = [name, miles, price]
        
        # insert car information into the database
        database.insert_car(list_Information)
        
        # increment the counter for logging purposes
        c += 1
    
    # log the number of pages processed and cars added to the database
    print(f"Finished processing page {num_page}. Added {c} cars to the database.")
    
# close the database connection when done
database.conn.close()
