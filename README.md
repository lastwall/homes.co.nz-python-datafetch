# Real Estate Data Fetcher homes.co.nz

## Installation Guide

Follow the steps below to setup and run this application:

1. **Install the required packages**

   Use pip to install the necessary packages from the requirements.txt file:

   ```
   pip install -r requirements.txt
   ```

2. **Configure the application**

   Open the `config.py` file and set your settings:

   - `API_BASE_URL`: This is already set to 'https://gateway.homes.co.nz'
   - `LATITUDE`: Replace 'Your_Latitude' with your actual latitude
   - `LONGITUDE`: Replace 'Your_Longitude' with your actual longitude
   - `LIMIT`: This is set to 100
   - `DB_NAME`: This is set to 'properties.db'

   Your `config.py` should look like this:

   ```
   API_BASE_URL = 'https://gateway.homes.co.nz'
   LATITUDE = 'Your_Latitude'  # replace with your actual latitude
   LONGITUDE = 'Your_Longitude'  # replace with your actual longitude
   LIMIT = 100
   DB_NAME = 'properties.db'
   ```

3. **Run the application**

   Use the following command to run the application:

   ```
   python app.py
   ```
