# in this file we will check if the files contain any duplicates

def find_duplicates(file_path):
    seen = set()  
    duplicates = set()  

    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            if line in seen:
                duplicates.add(line)
            else:
                seen.add(line)

    if duplicates:
        print("Duplicate lines found:")
        for duplicate in duplicates:
            print(duplicate)
    else:
        print("No duplicates found.")

# Usage
find_duplicates("allCVE.txt")
