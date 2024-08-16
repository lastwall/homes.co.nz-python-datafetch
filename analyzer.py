
import sqlite3
import pandas as pd
from config import DB_NAME

def analyze_data():
    conn = sqlite3.connect(DB_NAME)
    df = pd.read_sql_query("SELECT * FROM properties", conn)

    # Example analysis: average price
    avg_price = df['price'].mean()
    print(f"Average price of properties: ${avg_price:,.2f}")

    # You can add more complex analysis here

    conn.close()
