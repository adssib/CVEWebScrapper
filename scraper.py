import requests
import os

# This is the base URL "https://www.cvedetails.com/vulnerability-list/year-2025/month-1/January.html?page=1&order=1"

months = [
    "January", "February", "March", "April", "May", "June", 
    "July", "August", "September", "October", "November", "December"
]

out_dir = "out"
try :
    os.mkdir(out_dir)
except: 
    print("Folder already exsist")

# x will represent the month number
for x in range (2):
    # y is the number of pages we are going to loop through 
    for y in range (2):
        baseURL = f"https://www.cvedetails.com/vulnerability-list/year-2024/month-{x}/{months[x]}.html?page={y}&order=1"
        page = requests.get(baseURL)
        
        outputFileName = f"_cvedetails_{y}_{months[x]}_2024"
        fileExtension = ".txt"
        # os.mknod(fileName) 

        f = open(out_dir,outputFileName + fileExtension , "w")
        f.write(page.text)
f.close 



# print(page.text)
 