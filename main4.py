from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://dps.psx.com.pk').text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('table', class_='tbl dataTable no-footer')
print(jobs)
for job in jobs:
	print(job)