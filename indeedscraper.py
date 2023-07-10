import requests
from bs4 import BeautifulSoup
import time
import urllib

def scrape_indeed_jobs():
    url = 'https://ca.indeed.com/jobs?q=internship&l=Mississauga%2C+ON&start=20'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
    }
    session = requests.Session()
    response = session.get(url, headers=headers)
    if response.status_code != 200:
        print('Failed to retrieve page:', response.status_code)
        return

    soup = BeautifulSoup(response.content, 'html.parser')
    jobs = soup.find_all('div', class_='jobsearch-SerpJobCard')

    if not jobs:
        print('No jobs found.')
        return

    try:
        with open('internship_jobs.txt', 'w', encoding='utf-8') as file:
            for job in jobs:
                time.sleep(2)
                title = job.find('a', class_='jobtitle').text.strip()
                company = job.find('span', class_='company').text.strip()
                location = job.find('span', class_='location').text.strip()

                file.write(f'Title: {title}\n')
                file.write(f'Company: {company}\n')
                file.write(f'Location: {location}\n')
                file.write('-' * 50)
                file.write('\n')

        print('Scraping complete. Internship jobs saved in "internship_jobs.txt".')
    except Exception as e:
        print('An error occurred while writing to the file:', str(e))


scrape_indeed_jobs()
