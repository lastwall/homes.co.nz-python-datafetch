import requests

class DataFetcher:
    def __init__(self, api_base_url):
        self.api_base_url = api_base_url

    def fetch_property_data(self, lat, long, limit):
        url = f'{self.api_base_url}/properties/nearby?lat={lat}&long={long}&limit={limit}'
        response = requests.get(url)
        if response.status_code == 200:
            return response.json().get('cards', [])
        else:
            return []

    def fetch_additional_details(self, property_id):
        url = f'{self.api_base_url}/details?property_id={property_id}'
        response = requests.get(url)
        if response.status_code == 200:
            return response.json().get('property', {})
        else:
            return {}
        
    def fetch_map_cards(self, polylines, page, limit, display_rentals, for_rent, for_sale, just_sold, off_market,sale_max):
        url = f'{self.api_base_url}/map/cards'
        payload = {
            "polylines": polylines,
            "page": page,
            "limit": limit,
            "display_rentals": display_rentals,
            "for_rent": for_rent,
            "for_sale": for_sale,
            "just_sold": just_sold,
            "off_market": off_market,
            "off_market": sale_max
        }
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            return response.json().get('cards', [])
        else:
            return []
        
        