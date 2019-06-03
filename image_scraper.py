import os, sys
from bs4 import BeautifulSoup
import requests
from tkinter import *

def retrieve_input():
    namedir = T.get("1.0","end-1c")
    return namedir

def getpicsus():
    dirname = retrieve_input()
    r0 = "https://unsplash.com/search/photos/" + dirname
    r = requests.get(r0)
    html_doc = r.content
    soup = BeautifulSoup(html_doc, "html.parser")

    imagetags = soup.findAll("img", {"class":"_2zEKz"})

    original = os.getcwd()
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    os.chdir(dirname)

    x = 0

    for image in imagetags:
        try:
            url = image['src']
            source = requests.get(url)
            if source.status_code == 200:
                with open("us " + dirname + " - " + str(x) + ".jpg", "wb") as f:
                    f.write(requests.get(url).content)
                    f.close()
                    x += 1
        except:
            pass
    os.chdir(original)

def getpicspx():
    dirname = retrieve_input()
    r0 = "https://www.pexels.com/search/" + dirname
    r = requests.get(r0)
    html_doc = r.content
    soup = BeautifulSoup(html_doc, "html.parser")

    imagetags = soup.findAll("img", {"class":"photo-item__img"})

    original = os.getcwd()
    if not os.path.exists(dirname):
        os.makedirs(dirname)

    os.chdir(dirname)

    x = 0

    for image in imagetags:
        try:
            url = image['src']
            source = requests.get(url)
            if source.status_code == 200:
                with open("px " + dirname + " - " + str(x) + ".jpg", "wb") as f:
                    f.write(requests.get(url).content)
                    f.close()
                    x += 1
        except:
            pass
    os.chdir(original)



root = Tk()
root.title("Lazy Man's Image Scraper")
lbl = Label(root, text="Input your desired search term in the text box, and pick the source.")
lbl.pack()
root.geometry('500x300')

T = Text(root, height=1, width=30)
T.pack()
unsplash = Button(root, text = "Search Unsplash", command = getpicsus)
pexels = Button(root, text = "Search Pexels", command = getpicspx)
unsplash.pack()
pexels.pack()




root.mainloop()