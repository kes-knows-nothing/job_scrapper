from bs4 import BeautifulSoup
import requests

def extract_jobs1(term):
    url = f"https://weworkremotely.com/remote-jobs/search?term={term}&button=&sort=any_time"
    request = requests.get(url, headers={"User-Agent": "Kimchi"})
    results = []
    if request.status_code == 200:
      soup = BeautifulSoup(request.text, "html.parser")
      jobs = soup.find_all("li", class_="feature")
      for job in jobs:
         company = job.find("span", class_="company")
         position = job.find("span", class_="title")
         location = job.find("span", class_="region")
         if company:
                company = company.string.strip()
         if position:
                position = position.string.strip()
         if location:
                location = location.string.strip()
         if company and position and location:
                job = {
                    'company': company,
                    'position': position,
                    'location': location
                }
                results.append(job)
              
    else:
        print("Can't get jobs.")
    return results