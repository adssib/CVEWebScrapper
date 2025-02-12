import requests
import os
from bs4 import BeautifulSoup
import time

# This is the base URL "https://www.cvedetails.com/vulnerability-list/year-2025/month-1/January.html?page=1&order=1"

months = [
    "January", "February", "March", "April", "May", "June", 
    "July", "August", "September", "October", "November", "December"
]

# out_dir = "out"
# os.makedirs(out_dir, exist_ok=True)

# x will represent the month number
for x in range (1, 13):
    # y is the number of pages we are going to loop through  till now we will limit it to 3 and thats it 
    for y in range (1, 3):
        baseURL = f"https://www.cvedetails.com/vulnerability-list/year-2024/month-{x}/{months[x-1]}.html?page={y}&order=1"
        page = requests.get(baseURL)

        time.sleep(1) 

        soup = BeautifulSoup(page.content, "html.parser")

        # outputFileName = f"_cvedetails_page_{y}_{months[x-1]}_2024.txt"
        # os.mknod(fileName) 
        # filePath = os.path.join(out_dir, outputFileName)

        cveSearchresults = soup.find(id="ResultsContainer") 

        if cveSearchresults:
            allDivCVE = cveSearchresults.find_all("div", class_="border-top py-3 px-2 hover-bg-light")

            for singleDivCVE in allDivCVE:
                row = singleDivCVE.find("div", class_="row") 
                colMd9 = row.find("div", class_="col-md-9")
                recondRow = colMd9.find("div", class_="row")
                h3 = recondRow.find("h3", class_="col-md-4 text-nowrap")
                link = h3.find("a", href=True) 
                if link:
                    href = link['href']
                    print(href) 
        else:
            print(f"Results container not found on page: {baseURL}")
        # with open(filePath, "w", encoding="utf-8") as f:
        #     f.write(page.text)

        # print(f"File created: {filePath}")



# print(page.text)
 