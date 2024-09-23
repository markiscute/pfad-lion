import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

# Set fonts to prevent Chinese garbled characters
plt.rcParams['font.sans-serif'] = ['SimHei']  # Set Chinese font to SimHei
plt.rcParams['axes.unicode_minus'] = False  # Fix issue with negative sign not showing up

# Define the base URL and main tide page URL
BASE_URL = 'https://www.hko.gov.hk'
TIDE_PAGE_URL = BASE_URL + '/en/tide/ttext.htm'

# Function to fetch the HTML content of a page
def fetch_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    else:
        print(f"Failed to fetch page, status code: {response.status_code}")
        return None

# Function to find the 2025 tide data link from the main page
def find_tide_data_link(content):
    soup = BeautifulSoup(content, 'html.parser')
    table = soup.find('table')
    link_tag = table.find('a', href=True, text='2025') if table else None
    if link_tag:
        return BASE_URL + link_tag['href']
    else:
        print("Could not find the link for the 2025 tide data.")
        return None

# Function to parse tide data from the tide page
def parse_tide_data(content):
    soup = BeautifulSoup(content, 'html.parser')
    table = soup.find('table')
    if table:
        data_lines = table.text.splitlines()
        print("Tide data preview:")
        for line in data_lines[:10]:  # Show the first 10 lines
            print(line)
        return data_lines
    else:
        print("Could not find <table> tag containing tide data.")
        return None

# Function to process tide data into dates and heights
def process_tide_data(data_lines):
    dates, heights = [], []
    for line in data_lines[3:]:  # Skip the first few descriptive lines
        parts = line.split()
        if len(parts) >= 3:
            date = parts[0]
            height = round(float(parts[1]), 2)  # Tide height
            dates.append(date)
            heights.append(height)
    return dates, heights

# Function to visualize the tide height data as a bar chart
def plot_tide_data(dates, heights):
    plt.figure(figsize=(10, 6))
    plt.bar(dates, heights, color='b')
    plt.xticks(rotation=90)
    plt.title('Tide Height Changes')
    plt.xlabel('Date')
    plt.ylabel('Tide Height (m)')
    plt.grid(True, axis='y')
    plt.tight_layout()
    plt.show()

# Main execution flow
def main():
    # Fetch the main page content
    main_page_content = fetch_page(TIDE_PAGE_URL)
    
    if main_page_content:
        # Find the link to the 2025 tide data
        tide_data_link = find_tide_data_link(main_page_content)
        
        if tide_data_link:
            # Fetch the tide data page content
            tide_page_content = fetch_page(tide_data_link)
            
            if tide_page_content:
                # Parse and process the tide data
                tide_data_lines = parse_tide_data(tide_page_content)
                if tide_data_lines:
                    dates, heights = process_tide_data(tide_data_lines)
                    
                    # Plot the tide data
                    plot_tide_data(dates, heights)

# Run the main function
if __name__ == '__main__':
    main()
