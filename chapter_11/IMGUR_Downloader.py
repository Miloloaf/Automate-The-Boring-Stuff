#! python3

"""
Using existing modules searches a search on IMGUR and fetches the first x images and downloads them
"""

# TODO Give the correct file encoding so that gifs download as gifs rather than jpgs.

from selenium import webdriver
import requests, bs4, shutil, time, os, urllib3

search = "water"

os.makedirs(search, exist_ok=True)

def create_all_links(search):
    links = []
    site = requests.get("https://imgur.com/search?q=" + search)
    site.raise_for_status()

    soup = bs4.BeautifulSoup(site.text, "html.parser")
    item = soup.select('div > a[class="image-list-link"]')

    for a in soup.find_all("a", href = True):
        individual_link = (a["href"])
        if "gallery" in individual_link:
            links.append("https://imgur.com" + individual_link)
    return links

def image_linker(link):
    dlsite = requests.get(link, stream=False)
    dlsite.raise_for_status()
    soup = bs4.BeautifulSoup(dlsite.text, "html.parser")
    imageElem = soup.select(".post-image-container")

    if imageElem == []:
        print("Cound not detect image")

    else:
        print("Image detected")
        id = imageElem[0].get("id")
        imagelink = "https://i.imgur.com/%s.jpg" %id
        return imagelink

def download_image(link):
    dlsite = requests.get(link, stream=False)
    dlsite.raise_for_status()

    print("Image Downloaded")

    imagefile = open(os.path.basename(link), "wb")
    for chunk in dlsite.iter_content(100000):
        imagefile.write(chunk)
    imagefile.close()

def main(search, results):
    link = create_all_links(search)
    for i in range(results):
        image = image_linker(link[i])
        download_image(image)

foo = "https://imgur.com/gallery/7Dhnj1p"
bar = "https://imgur.com/gallery/KnsYwsg"

foo2 = "https://i.imgur.com/7Dhnj1p.png"
bar2 = "https://imgur.com/gallery/0MAlq"

# print(image_linker(bar2))
#download_image(foo2)
#download_image(image_linker(foo))

main(search, 1)

