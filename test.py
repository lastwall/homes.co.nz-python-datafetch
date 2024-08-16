import requests
import json

# Define the API endpoint
api_endpoint = "https://property-service.homes.co.nz/map/items"

# Setup the parameters for the web request (example parameters, adjust as needed)
parameters = {
    'limit': '6000',
    'just_sold': 'false',
    'for_sale': 'true',
    'sale_min':'0',
    'sale_max':'0',                      
    'num_bathrooms':'0',
    'num_bedrooms':'0',
    'display_rentals': 'false',
    'for_rent': 'false',
    'rent_bathrooms':'0',
    'rent_bedrooms':'0',
    'rent_max':'0',
    'rent_min':'0',
    'off_market':'false',
    'off_market_bathrooms':'0',
    'off_market_bedrooms':'0',
    'off_market_max':'0',
    'off_market_min':'0',
    'use_expanded_bounding_box':'true',
    'nw_lat':'-36.84266',  # Replace with actual values
    'nw_long':'174.76257', # Replace with actual values
    'se_lat':'-36.84866',  # Replace with actual values
    'se_long':'174.76557'  # Replace with actual values
}

# Make the GET request to the API
response = requests.get(api_endpoint, params=parameters)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    json_response = response.json()
    
    # Define the output file path
    output_file_path = "output.json"
    
    # Write the JSON response to a file
    with open(output_file_path, 'w') as json_file:
        json.dump(json_response, json_file, indent=4)
    
    print(f"JSON response successfully saved to {output_file_path}")
else:
    print(f"Failed to retrieve data from API. Status code: {response.status_code}")
