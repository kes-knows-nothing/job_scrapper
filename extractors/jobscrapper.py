from bs4 import BeautifulSoup
import requests

def extract_jobs(term):
    url = f"https://remoteok.com/remote-{term}-jobs"
    request = requests.get(url, headers={"User-Agent": "Kimchi"})
    if request.status_code == 200:
      soup = BeautifulSoup(request.text, "html.parser")
      jobs = soup.find_all('td', class_="company position company_and_position")
      jobs.pop(0)
      result = []
      for job in jobs:
        job_title = job.find_all("h2")[0]
        jobTitle = job_title.string.strip()
        verified = job.find_all("span", class_="verified")
        isClosed = job.find("span", class_="closed")
        company_name = job.find_all("h3")[0]
        companyName = company_name.string.strip()
        location_pay = job.find_all("div", class_= "location")
        if isClosed == None:
           isHired = "Hiring Now"
        else:
           isHired = isClosed.string.title()
        if verified == []:
           isVerified = "Unverified"
        else:
           isVerified = verified[0].string.title()
        pay = location_pay[len(location_pay) - 1].string
        location_pay.pop(len(location_pay) - 1)
        location = []
        for loca in location_pay:
          location.append(loca.string)
        job_data = {
           "company" : companyName,
           "job_title" :  jobTitle,
           "wanted" : isHired,
           "verified" : isVerified,
           "pay" : pay,
           "location" : location
        }
        result.append(job_data)
      return result
    else:
        print("can't get a job")
   


        
# print("REACT")
# extract_jobs("react")
# print("RUST")
# extract_jobs("rust")
# print("GOLANG")
# extract_jobs("golang")
# print("PTYHON")
# extract_jobs("python")


