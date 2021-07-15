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
    r.encoding = 'utf8'
    soup = BeautifulSoup(r.text, 'lxml')
    emoji = soup.find('span', class_='emoji').get_text()
    # STITCHING THEM ALL
    results['emoji'] = emoji
    results['url'] = url
    h1_name = soup.find('h1').get_text().strip()
    results['name'] = h1_name.replace(emoji, "").strip()



    h2_titles = soup.find_all('h2')

    # GET INTRO
    try:
        meaning_title = [x for x in h2_titles if "Meaning of" in str(x)][0]
        emoji_intro = next_nearest_sibling(meaning_title, 'p').get_text()
        results['intro'] = emoji_intro
    except IndexError:
        pass

    # GET EXAMPLE
    try:
        example_of = [x for x in h2_titles if "Examples of" in str(x)][0]
        emoji_example = next_nearest_sibling(example_of, 'ul')
        emoji_example_list = [x.get_text() for x in emoji_example.find_all('li')\
                                if x.get_text() != '+add']
        results['example'] = emoji_example_list
    except IndexError:
        pass
# GET COMBO
    try:
        combo_title = [x for x in h2_titles if "Combinations " in str(x)][0]
        combo_elem = next_nearest_sibling(combo_title, 'ul')
        combo_list = [x.get_text() for x in combo_elem.find_all('li')\
                                if x.get_text() != '+Add']
        results['combination'] = combo_list
    except IndexError:
        pass
# GET KAOMOJI
    try:
        kaomoji_title = [x for x in h2_titles if "kaomojis" in str(x)][0]
        kaomoji_elem = next_nearest_sibling(kaomoji_title, 'ul')
        kaomoji_list = [x.get_text() for x in kaomoji_elem.find_all('li')\
                                if x.get_text() != '+Add']
        results['kaomoji'] = kaomoji_list
    except IndexError:
        pass
# GET IMAGES
    try:
        table = soup.find(class_="emoji-pics")
        if table:
            names = [x.get_text() for x in table.find_all('td')]
            links = [x.get('src') for x in table.find_all('img')]
            results['images'] = dict(zip(names[1:], links))
    except IndexError:
        pass

# GET RELATED
    try:
        rel_div = soup.find('div', id="Related_Emojis")
        ul_related = next_nearest_sibling(rel_div, 'ul')
        results['related_emoji'] = [x.get_text().strip() \
            for x in ul_related.find_all('span')]
    except IndexError:
        pass


    # GET TABLES (UNICODE INFO, TRANSLATION)
    # ADDED SAFE CHECK
    try:
        tables = pandas.read_html(str(soup))
        py_tables = [x.set_index(0).squeeze().to_dict() for x in tables]
        for t in py_tables:
            if "Full name" in t.keys():
                infotable = t
                results['unicode_info'] = infotable
            if "Another names, keywords" in t.keys():
                translation = t
                results['translation'] = translation
    except (IndexError, ValueError):
        pass


    # Returns the final result
    print(f"NAME : {results['name']}")
    return results


if __name__=='__main__':
    import json
    with open("all_emoji.json") as fin:
        data = json.load(fin)
    urls = list(data.values())
    print (f"Total : {len(urls)}")
    results = []
    for url in urls:
        print(f"{len(results)}/{len(urls)}")
        try:
            data = get_emoji(url)
            if "Collection" not in data['name'] and data['url'] == url:
                results.append(data)
                print(f"Appended {url}")
            
        except:
            print(f"ERROR ==> {url}")
            # print(f"==>DATA : {data}")
            traceback.print_exc()
            print(f"**************Not collected {url}")
    # emojis = [get_emoji(url) for url in urls]
    with open("emoji_wiki.json", "w") as fout:
        data = json.dumps(results, indent=2)
        fout.write(data)




