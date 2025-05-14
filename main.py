import requests
from bs4 import BeautifulSoup

# Function to scrape LinkedIn data
def scrape_linkedin(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract company name
        company_name_tag = soup.find('h1', class_='org-top-card-summary__title')
        company_name = company_name_tag.text.strip() if company_name_tag else "N/A"

        # Extract number of employees
        employees_tag = soup.find('span', class_='t-normal t-black--light link-without-visited-state link-without-hover-state')
        employees = employees_tag.text.strip() if employees_tag else "N/A"

        return company_name, employees

    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return None, None


# Read URLs from a file and scrape data
def read_urls_from_file(file_path):
    with open(file_path, 'r') as f:
        return [url.strip() for url in f.readlines() if url.strip()]

def main():
    file_path = 'links.txt'
    urls = read_urls_from_file(file_path)
    for url in urls:
        company_name, employees = scrape_linkedin(url)
        if company_name and employees:
            print(f"Company Name: {company_name}")
            print(f"Number of Employees: {employees}")
        else:
            print(f"Failed to retrieve data for {url}")
        print("=======================================")

if __name__ == "__main__":
    main()
