import os, sys
from bs4 import BeautifulSoup
import requests

print("*+++++++++++++++++++++++++++++++++++++++++*")
print("*Welcome to the lazy man's image searcher.*")
print("* Where do you want to search?            *")
print("* 1 - Unsplash                            *")
print("* 2 - Pexels                              *")
print("*+++++++++++++++++++++++++++++++++++++++++*")
engine = input("\n")
r0 = ""
if engine == "1":
    print("Unsplash selected!")
    choice = input("\nWhat is your search term?\n")
    r0 = "https://unsplash.com/search/photos/" + choice
if engine == "2":
    print("Pexels selected!")
    choice = input("\nWhat is your search term?\n")
    r0 = "https://www.pexels.com/search/" + choice
else:
    print("Select a valid choice!")


r = requests.get(r0)
html_doc = r.content
soup = BeautifulSoup(html_doc, "html.parser")

imagetags = soup.findAll("img")

if not os.path.exists(choice):
    os.makedirs(choice)

os.chdir(choice)

x = 0

print("Downloading images...")
for image in imagetags:
    try:
        url = image['src']
        source = requests.get(url)
        if source.status_code == 200:
            with open(choice + " - " + str(x) + ".jpg", "wb") as f:
                f.write(requests.get(url).content)
                f.close()
                x += 1
    except:
        pass

print("Done!")