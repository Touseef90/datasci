from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Reactjs&txtLocation=').text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

for job in jobs:
  company_name = job.h3.text
  skills = job.find('span', class_='srp-skills').text.replace(' ', '')
  published_date = job.find('span', class_='sim-posted').span.text
  more_info = job.header.h2.a['href']
  if 'few' in published_date:
    print(f'Company Name: {company_name.strip()}')
    print(f'Skills: {skills.strip()}')
    print(f'Date: {published_date}')
    print(f'More Info: {more_info.strip()}')
    print('---------------------------------------')
