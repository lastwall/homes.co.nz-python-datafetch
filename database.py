import sqlite3
from config import DB_NAME

class Database:
    def __init__(self):
        self.conn = sqlite3.connect(DB_NAME)
        self.columns = self.get_columns()
        self.create_table()

    def get_columns(self):
        # Define columns as a list of tuples: (column_name, data_type)
        return [
            ('item_id', 'TEXT'),
            ('property_id', 'TEXT'),
            ('address', 'TEXT'),
            ('display_address', 'TEXT'),
            ('cover_image_url', 'TEXT'),
            ('cover_image_url_source', 'TEXT'),
            ('listing_images', 'TEXT'),
            ('google_street_view_url', 'TEXT'),
            ('num_bathrooms', 'INTEGER'),
            ('num_bedrooms', 'INTEGER'),
            ('num_car_spaces', 'INTEGER'),
            ('latest_source', 'TEXT'),
            ('headline', 'TEXT'),
            ('estimated_value_revision_date', 'TEXT'),
            ('display_estimated_lower_value_short', 'TEXT'),
            ('display_estimated_upper_value_short', 'TEXT'),
            ('display_estimated_value_short', 'TEXT'),
            ('estimated_rental_revision_date', 'TEXT'),
            ('display_estimated_rental_lower_value_short', 'TEXT'),
            ('display_estimated_rental_upper_value_short', 'TEXT'),
            ('estimated_rental_yield', 'REAL'),
            ('capital_value', 'REAL'),
            ('improvement_value', 'REAL'),
            ('land_value', 'REAL'),
            ('display_capital_value_short', 'TEXT'),
            ('display_improvement_value_short', 'TEXT'),
            ('display_land_value_short', 'TEXT'),
            ('current_revision_date', 'TEXT'),
            ('city_id', 'INTEGER'),
            ('suburb_id', 'INTEGER'),
            ('unit_identifier', 'TEXT'),
            ('street_number', 'TEXT'),
            ('street', 'TEXT'),
            ('suburb', 'TEXT'),
            ('city', 'TEXT'),
            ('ta', 'TEXT'),
            ('lat', 'REAL'),
            ('long', 'REAL'),
            ('display_price', 'TEXT'),
            ('price', 'REAL'),
            ('date', 'TEXT'),
            ('featured_at', 'TEXT'),
            ('agent_id', 'TEXT'),
            ('agent_name', 'TEXT'),
            ('agent_role', 'TEXT'),
            ('agent_profile_image_url', 'TEXT'),
            ('agent_mobile_phone', 'TEXT'),
            ('agent_office_phone', 'TEXT'),
            ('agent_branch_id', 'TEXT'),
            ('agent_branch_name', 'TEXT'),
            ('agent_logo_url', 'TEXT'),
            ('agent_phone', 'TEXT'),
            ('url', 'TEXT'),
            ('display_price_short', 'TEXT')
        ]

    def create_table(self):
        c = self.conn.cursor()
        # Generate SQL for creating table
        columns_sql = ", ".join([f"{name} {dtype}" for name, dtype in self.columns])
        primary_key_sql = "PRIMARY KEY (item_id, property_id)"
        c.execute(f'''CREATE TABLE IF NOT EXISTS properties ({columns_sql}, {primary_key_sql})''')

    def property_exists(self, item_id, property_id):
        c = self.conn.cursor()
        c.execute("SELECT 1 FROM properties WHERE item_id = ? AND property_id = ?", (item_id, property_id))
        return c.fetchone() is not None

    def store_data(self, data):
        c = self.conn.cursor()

        for item in data:
            values = self.extract_values(item)

            item_id = item.get('item_id', None)
            property_id = item.get('property_id', None)

            if self.property_exists(item_id, property_id):
                self.update_property(c, values, item_id, property_id)
            else:
                self.insert_property(c, values)

        self.conn.commit()

    def extract_values(self, item):
        # Extracting nested data safely
        prop = item.get('property_details', {})
        point = item.get('point', {})
        agent = item.get('agent', None)
        branch = agent.get('branch', {}) if agent and agent.get('branch') else {}

        # Map extracted values to columns order
        values = (
            item.get('item_id', None),
            item.get('property_id', None),
            prop.get('address', None),
            prop.get('display_address', None),
            prop.get('cover_image_url', None),
            prop.get('cover_image_url_source', None),
            ','.join(prop.get('listing_images', [])) if prop.get('listing_images') else None,
            prop.get('google_street_view_url', None),
            prop.get('num_bathrooms', None),
            prop.get('num_bedrooms', None),
            prop.get('num_car_spaces', None),
            prop.get('latest_source', None),
            prop.get('headline', None),
            prop.get('estimated_value_revision_date', None),
            prop.get('display_estimated_lower_value_short', None),
            prop.get('display_estimated_upper_value_short', None),
            prop.get('display_estimated_value_short', None),
            prop.get('estimated_rental_revision_date', None),
            prop.get('display_estimated_rental_lower_value_short', None),
            prop.get('display_estimated_rental_upper_value_short', None),
            prop.get('estimated_rental_yield', None),
            prop.get('capital_value', None),
            prop.get('improvement_value', None),
            prop.get('land_value', None),
            prop.get('display_capital_value_short', None),
            prop.get('display_improvement_value_short', None),
            prop.get('display_land_value_short', None),
            prop.get('current_revision_date', None),
            prop.get('city_id', None),
            prop.get('suburb_id', None),
            prop.get('unit_identifier', None),
            prop.get('street_number', None),
            prop.get('street', None),
            prop.get('suburb', None),
            prop.get('city', None),
            prop.get('ta', None),
            point.get('lat', None),
            point.get('long', None),
            item.get('display_price', None),
            item.get('price', None),
            item.get('date', None),
            item.get('featured_at', None),
            agent.get('id', None) if agent else None,
            agent.get('name', None) if agent else None,
            agent.get('role', None) if agent else None,
            agent.get('profile_image_url', None) if agent else None,
            agent.get('mobile_phone', None) if agent else None,
            agent.get('office_phone', None) if agent else None,
            branch.get('id', None),
            branch.get('branch_name', None),
            branch.get('logo_url', None),
            branch.get('phone', None),
            item.get('url', None),
            item.get('display_price_short', None)
        )
        return values

    def insert_property(self, c, values):
        # Dynamically generate insert SQL
        columns = ", ".join([col[0] for col in self.columns])
        placeholders = ", ".join(["?"] * len(self.columns))
        c.execute(f'''INSERT INTO properties ({columns}) VALUES ({placeholders})''', values)

    def update_property(self, c, values, item_id, property_id):
        # Dynamically generate update SQL
        set_clause = ", ".join([f"{col[0]} = ?" for col in self.columns])
        c.execute(f'''UPDATE properties SET {set_clause} WHERE item_id = ? AND property_id = ?''',
                  values + (item_id, property_id))

    def close(self):
        self.conn.close()
