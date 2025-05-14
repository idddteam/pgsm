#webscraping for chrome
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
# Removed unused import

chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--disable-gpu")  # Disable GPU usage
chrome_options.add_argument("--no-sandbox")  # Required for running as root in some environments
chrome_options.add_argument("--disable-dev-shm-usage")  # Avoid shared memory issues
chrome_options.add_argument("--disable-software-rasterizer")  # Prevent fallback to software WebGL
chrome_options.add_argument("--disable-web-security")  # Disable web security (optional, for debugging)
chrome_options.add_argument("--log-level=3")  # Suppress logs
chrome_options.add_argument("--silent")  # Suppress output
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("disable-infobars")
chrome_options.add_argument("--disable-extensions")

# Ensure the correct path to ChromeDriver
from selenium.webdriver.chrome.service import Service
service = Service(r'C:\Users\Hridik\Documents\chrome-win64\chromedriver.exe')  # Replace with the actual path to chromedriver.exe
driver = webdriver.Chrome(service=service, options=chrome_options)

# Function to scrape LinkedIn data
def scrape_linkedin(url):
    driver.get(url)

    try:
        # Extract company name
        try:
            company_name = driver.find_element(By.CLASS_NAME, 'org-top-card-summary__title').text.strip()
        except NoSuchElementException:
            company_name = "N/A"

        try:
            employees = driver.find_element(By.CSS_SELECTOR, 'span.t-normal.t-black--light.link-without-visited-state.link-without-hover-state').text.strip()
        except NoSuchElementException:
            employees = "N/A"
        return company_name, employees
        
    except Exception as e:
        print(f"Company Name:")

        print(f"Error scraping {url}: {e}")
        return None, None


# from link txt file scrape_linkedin

file = 'links.txt'
with open(file, 'r') as f:
    urls = f.readlines()
    urls = [url.strip() for url in urls if url.strip()]  # Remove empty lines and whitespace
    # Print the results
    for url in urls:
        company_name, employees = scrape_linkedin(url)
        if company_name and employees:
            print(f"Company Name: {company_name}")
            print(f"Number of Employees: {employees}")
        else:
            print(f"Failed to retrieve data for {url}")
        print("=======================================")
    # Close the WebDriver after processing all URLs
    driver.quit()