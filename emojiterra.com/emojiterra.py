from bs4 import BeautifulSoup
import requests
import json

def demoji_name(name):
    demojied = ''.join(e for e in name if e.isascii()).strip()
    return demojied

def cate_process(elem):
    name = demoji_name(elem.find('a').get_text())
    link = elem.find('a')['href']
    return {'name': name, 'link':link }

def moji_process(elem):
    name = demoji_name(elem.get_text())
    link = elem['href']
    return {'name': name, 'link':link }

def get_moji():
    r= requests.get("https://emojiterra.com/categories/")
    soup = BeautifulSoup(r.text, 'lxml')
    categories = soup.find_all(class_="archive-parent-sublist")
    catnames = [cate_process(x) for x in categories]

    # get children emojis
    subsection = [x.find(class_="archive-child") for x in categories]
    emo_by_cat = []
    for sub in subsection:
        emojies = sub.find_all('a')
        parsed = [moji_process(emo) for emo in emojies]
        emo_by_cat.append(parsed)

    results = list(zip(catnames, emo_by_cat))

    return results

if __name__=="__main__":
    r = get_moji()
    with open("emojiterra.json", "w") as fout:
        rtext = json.dumps(r, indent=2)
        print(rtext)
        fout.write(rtext)