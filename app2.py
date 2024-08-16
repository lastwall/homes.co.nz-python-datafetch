from config import API_BASE_URL, LATITUDE, LONGITUDE, LIMIT
from data_fetcher import DataFetcher
from database import Database
from analyzer import analyze_data

def main():
    # Fetch data
    fetcher = DataFetcher(API_BASE_URL)

    # Example usage of fetch_property_data
    data = fetcher.fetch_property_data(LATITUDE, LONGITUDE, LIMIT)
    
    # Example usage of fetch_map_cards
    polylines = ["ecji`@bov_F?|zJ{bT??}zJzbT?"]
    page = 1
    limit = 60
    display_rentals = True
    for_rent = True
    for_sale = True
    just_sold = True
    off_market = True
    sale_max    = 2250000
    #num_bedrooms
    #num_bedrooms_max
    #num_bathrooms
    #num_bathrooms_max

    map_cards_data = fetcher.fetch_map_cards(polylines, page, limit, display_rentals, for_rent, for_sale, just_sold, off_market,sale_max)
    
    # Initialize and populate the database with map cards data
    db = Database()
    db.store_data(map_cards_data)
    
    # Analyze the data
    analyze_data()

if __name__ == "__main__":
    main()
