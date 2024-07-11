import requests
from bs4 import BeautifulSoup
import csv

# Read URLs from a text file
urls = []
with open('URLS_to_scrape.txt', 'r') as file:
    urls = [line.strip() for line in file.readlines()]

# Function to fetch and parse the first table of a given URL
def fetch_first_table(url):
    try:
        print(f"Fetching URL: {url}")  # Debugging output
        response = requests.get(url, timeout=10)  # 10 seconds timeout
        response.raise_for_status()  # Raises an HTTPError if the response was an error
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table')  # Find the first table
        if table:
            print(f"Table found for URL: {url}")  # Debugging output
            return [[cell.text for cell in row.find_all(['th', 'td'])] for row in table.find_all('tr')]
        else:
            print(f"No table found for URL: {url}")  # Debugging output
            return None
    except requests.exceptions.RequestException as e:
        print(f"Request error for {url}: {e}")
        return None
    except Exception as e:
        print(f"Error parsing table from {url}: {e}")
        return None

# Append each table to a CSV file
with open('ADScrape.csv', 'a', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    for url in urls:
        try:
            table_data = fetch_first_table(url)
            if table_data:
                writer.writerows(table_data)
                writer.writerow([])  # Add an empty row between tables for readability
        except Exception as e:
            print(f"Error writing table from {url} to CSV: {e}")