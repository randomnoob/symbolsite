from typing import final
from bs4 import BeautifulSoup
import requests
import json
import itertools, pandas
import traceback

def next_nearest_sibling(element, desired_tag_name):
    pointer = element
    while pointer.name != desired_tag_name:
        pointer = pointer.next_sibling
    return pointer

def get_emoji(url):
    print(f"Getting {url}")
    results = {}
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')

    emoji = soup.find('span', class_='emoji').get_text()
    # STITCHING THEM ALL
    results['emoji'] = emoji
    results['url'] = url


    h2_titles = soup.find_all('h2')

    try:
        meaning_title = [x for x in h2_titles if "Meaning of" in str(x)][0]
        emoji_intro = next_nearest_sibling(meaning_title, 'p').get_text()
        results['intro'] = emoji_intro
    except IndexError:
        pass

    try:
        example_of = [x for x in h2_titles if "Examples of" in str(x)][0]
        emoji_example = next_nearest_sibling(example_of, 'ul')
        emoji_example_list = [x.get_text() for x in emoji_example.find_all('li')\
                                if x.get_text() != '+add']
        results['example'] = emoji_example_list
    except IndexError:
        pass

    try:
        combo_title = [x for x in h2_titles if "Combinations " in str(x)][0]
        combo_elem = next_nearest_sibling(combo_title, 'ul')
        combo_list = [x.get_text() for x in combo_elem.find_all('li')\
                                if x.get_text() != '+Add']
        results['combination'] = combo_list
    except IndexError:
        pass

    try:
        kaomoji_title = [x for x in h2_titles if "kaomojis" in str(x)][0]
        kaomoji_elem = next_nearest_sibling(kaomoji_title, 'ul')
        kaomoji_list = [x.get_text() for x in kaomoji_elem.find_all('li')\
                                if x.get_text() != '+Add']
        results['kaomoji'] = kaomoji_list
    except IndexError:
        pass

    
    try:
        tables = pandas.read_html(str(soup))
        infotable = tables[1].set_index(0).squeeze().to_dict()
        results['unicode_info'] = infotable
        translation = tables[2].set_index(0).squeeze().to_dict()
        results['translation'] = translation
    except (IndexError, ValueError):
        pass
    return results


if __name__=='__main__':
    with open("emojis.wiki") as fin:
        urls = [x.strip() for x in fin.readlines()]
    print (f"Total : {len(urls)}")
    results = []
    for url in urls:
        try:
            data = get_emoji(url)
            results.append(data)
        except:
            print(f"ERROR ==> {url}")
            traceback.print_exc()
    # emojis = [get_emoji(url) for url in urls]
    with open("emoji_wiki.json", "w") as fout:
        data = json.dumps(results, indent=2)
        fout.write(data)




