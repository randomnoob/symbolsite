from typing import final
from bs4 import BeautifulSoup
import requests
import json
import itertools, pandas

def parsemoji(url):
    final_output = {}
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')


    # actual emoji
    actualmoji = soup.find(id="copy-paste")['value']
    final_output['emoji'] = actualmoji
    final_output['url'] = url

    ##  parse meaning   
    meaning = {}
    for x in soup.find(id='meaning').find_all('p'):
        strong = x.find('strong')
        if strong:
            first = x.find('strong').get_text().strip()
            whole = "".join(i for i in x.get_text().strip() if i.isascii())
            last = whole.replace(first, "")
            meaning[first] = last
    final_output['meaning'] = meaning


    # PARSE IMAGES and SUPPORT
    images = {}
    image_element = soup.find(id="image-history")
    vendors = [x.get_text().strip().replace(":", "") \
        for x in image_element.find_all(class_='image-history-vendor')]
    history = image_element.find_all(class_="version-history")
    hist_text = [elem.text.replace("❌","No\n").replace("✅","Yes\n") \
        for elem in history]
    hist_text2 = [x for x in "".join(hist_text).split("\n") if x]
    support_table = dict(map(lambda txt:txt.split(': '), hist_text2))

    imglinks = list(itertools.chain(*[x.find_all('a') for x in history]))
    imgsupport = dict(map(lambda elem: [elem.get_text().strip(), elem['href']], imglinks))

    support_table.update(imgsupport)
    final_output['support'] = support_table

    # UNICODE DATA
    pd_tables = pandas.read_html(str(soup))

    unicode_data = pd_tables[0]
    ud_cleaned = unicode_data.set_index(0).squeeze().to_dict()
    final_output['unicode_data'] = ud_cleaned

    moji_codes = pd_tables[1]
    mc_cleaned = moji_codes.set_index(0).squeeze().to_dict()
    final_output['emoji_codes'] = mc_cleaned

    cldr = soup.find(id="unicode-cldr")
    cldr_rows = [x.get_text().strip() for x in cldr.tbody.find_all('tr')]
    cldr_dict = dict(zip(cldr_rows[::1], cldr_rows[1::2]))
    final_output['other_languages'] = cldr_dict

    print (f"Done : {actualmoji}\n==>{url}\n\n")
    return final_output

if __name__=='__main__':
    with open("emojiterra.json") as fin:
        jsdata = json.load(fin)
    emojis = [x[1] for x in jsdata]
    emojis = list(itertools.chain(*emojis))
    result = []
    counter = 0
    for emo in emojis:
        data = parsemoji(emo['link'])
        counter += 1
        print(f"{counter}...Parsing : {emo['link']}")
        emocopy = emo
        emocopy['data'] = data
        result.append(emocopy)
    with open("emojiterra_single.json", "w") as fout:
        sss = json.dumps(result, indent=2)
        fout.write(sss)