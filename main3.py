from bs4 import BeautifulSoup

with open('mustaqbil.html', 'r') as html_file:
  content = html_file.read()
  soup = BeautifulSoup(content, 'lxml')
  jobs = soup.find_all('div', class_='mat-card mb10 list-item ng-star-inserted')
  for job in jobs:
    skill = job.find('h2', class_='mb5 mt0 tappable').a.text.strip()
    desc = job.find('div', class_='mt10 mb10').text
    date = job.find('div', class_='flex-100px-gap-15px text-right text-muted').text
    print('Skill : ' + skill)
    print('Description : ' + desc)
    print('Date : ' + date)
    print()