
from config import API_BASE_URL, LATITUDE, LONGITUDE, LIMIT
from data_fetcher import DataFetcher
from database import Database
from analyzer import analyze_data

def main():
    # Fetch data
    fetcher = DataFetcher(API_BASE_URL)

    data = fetcher.fetch_property_data(LATITUDE, LONGITUDE, LIMIT)
    
    # Initialize and populate the database
    db = Database()
    db.store_data(data)
    
    # Analyze the data
    analyze_data()

if __name__ == "__main__":
    main()
