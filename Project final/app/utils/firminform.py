import requests
from bs4 import BeautifulSoup

def login_to_site(session, username, password):
    login_page_url = 'https://www.firminform.de/anmelden'
    
    # Get the login page to retrieve any necessary cookies or hidden form fields
    login_page = session.get(login_page_url)
    
    # Parse the login page to retrieve hidden form fields if necessary
    soup = BeautifulSoup(login_page.text, 'html.parser')
    
    # Find hidden fields (if any)
    hidden_fields = soup.find_all('input', type='hidden')
    form_data = {field.get('name'): field.get('value') for field in hidden_fields}
    
    # Add username and password to the form data
    form_data['login'] = username
    form_data['password'] = password
    
    # URL to send the POST request to
    login_post_url = 'https://www.firminform.de/anmelden'
    
    # Send the POST request to log in
    response = session.post(login_post_url, data=form_data)
    print(response.text)
    
    # Check if login was successful
    if response.ok:
        print('Logged in successfully')
        return True
    else:
        print('Login failed')
        return False

def scrape_data(session, search_url):
    # After logging in, navigate to the desired page
    search_response = session.get(search_url)
    
    if search_response.ok:
        # Parse the search results page
        search_soup = BeautifulSoup(search_response.text, 'html.parser')
        
        # Example: Scraping company names from the search results
        # Adjust the selector according to the actual structure of the search results page
        companies = search_soup.find_all('div', class_='company_name_class')  # Replace 'company_name_class' with the actual class name
        
        for company in companies:
            print(company.get_text(strip=True))
        
        # Return the parsed data if needed
        return [company.get_text(strip=True) for company in companies]
    else:
        print('Failed to load the search results page')
        return []

if __name__ == '__main__':
    # Replace with your actual username and password
    username = '5644f04002@emailcbox.pro'
    password = 'Xzabam12'
    session = requests.Session()
    login_to_site(session, username, password)
    search_url = "https://www.firminform.de/suche?suchbegriff=fu&branchenAbschnitte=&rechtsform=SCE&im_handelsregister_geloescht=false&sortieren="
    scrape_data(session, search_url)
