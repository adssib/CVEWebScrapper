import requests
import os

# This is the base URL "https://www.cvedetails.com/vulnerability-list/year-2025/month-1/January.html?page=1&order=1"

months = [
    "January", "February", "March", "April", "May", "June", 
    "July", "August", "September", "October", "November", "December"
]

out_dir = "out"
os.makedirs(out_dir, exist_ok=True)

# x will represent the month number
for x in range (1, 13):
    # y is the number of pages we are going to loop through 
    for y in range (1, 3):
        baseURL = f"https://www.cvedetails.com/vulnerability-list/year-2024/month-{x}/{months[x-1]}.html?page={y}&order=1"
        page = requests.get(baseURL)
        print(f"Fetching data from: {baseURL}")

        outputFileName = f"_cvedetails_page_{y}_{months[x-1]}_2024.txt"
        # os.mknod(fileName) 
        filePath = os.path.join(out_dir, outputFileName)

        with open(filePath, "w", encoding="utf-8") as f:
            f.write(page.text)

        print(f"File created: {filePath}")



# print(page.text)
 