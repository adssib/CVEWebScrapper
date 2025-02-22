import requests
import os
from bs4 import BeautifulSoup
import time
import random

# This is the base URL "https://www.cvedetails.com/vulnerability-list/year-2025/month-1/January.html?page=1&order=1"

months = [
    "January", "February", "March", "April", "May", "June", 
    "July", "August", "September", "October", "November", "December"
]

allCVEs = [] 
year = 2024
outFile = f"{year}_CVE.txt"

# out_dir = "out"
# os.makedirs(out_dir, exist_ok=True)
with open(outFile, "w") as f:

    # x will represent the month number
    for x in range (1, 13):
        # y is the number of pages we are going to loop through  till now we will limit it to 3 and thats it 
        # for y in range (1, 3):
        # we can use a for loop here but it is not gonna take all of the pages 
        # we can get all pages by this method
        # observe than when we send a request and the query is ?page=10000 knowing there may not be there
        # the return is the same page as ?page=1 so we can use this behavior to get all pages 
        pageNumber = 1
        firstPageResponse = None
        while True:
            baseURL = f"https://www.cvedetails.com/vulnerability-list/year-{year}/month-{x}/{months[x-1]}.html?page={pageNumber}&order=1"
            
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
            }
            
            page = requests.get(baseURL, headers=headers)
            
            if page.status_code != 200:
                print(f"Failed to fetch {baseURL}, status code: {page.status_code}")
                continue
            if pageNumber == 1:
                firstPageResponse = page.text
            elif page.text == firstPageResponse:
                print(f"this page {pageNumber} have the same input as the Frist Page!")
                break

            time.sleep(random.uniform(1, 3))  

            try:
                soup = BeautifulSoup(page.content, "html.parser")

                body = soup.find("body")
                firstDiv = body.find("div", class_="container-xxl p-0 d-flex flex-column justify-content-start")
                secondDiv = firstDiv.find("div", class_="container-xxl p-0 d-flex justify-content-start")
                thirdDiv = secondDiv.find(id="contentdiv")
                forthDiv = thirdDiv.find("div", class_="p-0 pe-2")
                main = forthDiv.find("main")
                resultsTableVueDiv = main.find(id="resultsTableVueDiv") 
                cveSearchresults = resultsTableVueDiv.find(id="searchresults") 

                if cveSearchresults:
                    allDivCVE = cveSearchresults.find_all("div", class_="border-top py-3 px-2 hover-bg-light")
                    if not allDivCVE:  # No more CVEs found on the next page, stop pagination
                        print(f"No more CVEs found. Stopping at page {pageNumber} for {months[x-1]}.")
                        break

                    for singleDivCVE in allDivCVE:
                        row = singleDivCVE.find("div", class_="row") 
                        colMd9 = row.find("div", class_="col-md-9")
                        recondRow = colMd9.find("div", class_="row")
                        try:
                            h3 = recondRow.find("h3", class_="col-md-4 text-nowrap")
                            link = h3.find("a", href=True) 
                            if link:
                                href = link['href']
                                fullURL = f"https://www.cvedetails.com{href}"
                                if fullURL not in allCVEs:
                                    allCVEs.append(fullURL)
                                    f.write(fullURL + "\n")
                                    f.flush() 
                                    print(fullURL)
                        except Exception as e:
                            print(f"Error parsing a CVE entry: {e}")

                else:
                    print(f"Results container not found on page: {baseURL}") 
            except AttributeError:                
                print(f"Unexpected page structure for {baseURL}")
           
            pageNumber += 1 

print(f"Total CVEs scraped: {len(allCVEs)}")