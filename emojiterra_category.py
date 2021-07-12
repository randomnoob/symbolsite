from bs4 import BeautifulSoup
import requests
import json
urls = ['https://emojiterra.com/household/',
        'https://emojiterra.com/professions/',
        'https://emojiterra.com/country-flags/',
        'https://emojiterra.com/spring/',
        'https://emojiterra.com/thinking-face/',
        'https://emojiterra.com/musical-instruments/',
        'https://emojiterra.com/faces-with-tongue/',
        'https://emojiterra.com/summer/',
        'https://emojiterra.com/geometric-symbols/',
        'https://emojiterra.com/activities/',
        'https://emojiterra.com/faces-with-hands/',
        'https://emojiterra.com/lgbt/',
        'https://emojiterra.com/writing/',
        'https://emojiterra.com/birds/',
        'https://emojiterra.com/love/',
        'https://emojiterra.com/marine-animals/',
        'https://emojiterra.com/prepared-food/',
        'https://emojiterra.com/fingers/',
        'https://emojiterra.com/av-symbols/',
        'https://emojiterra.com/thanksgiving/',
        'https://emojiterra.com/asian-food/',
        'https://emojiterra.com/vegetables/',
        'https://emojiterra.com/animals/',
        'https://emojiterra.com/autumn/',
        'https://emojiterra.com/amphibians/',
        'https://emojiterra.com/objects/',
        'https://emojiterra.com/hotel/',
        'https://emojiterra.com/sweet-food/',
        'https://emojiterra.com/fruits/',
        'https://emojiterra.com/buildings/',
        'https://emojiterra.com/ramadan/',
        'https://emojiterra.com/gender/',
        'https://emojiterra.com/sports/',
        'https://emojiterra.com/music/',
        'https://emojiterra.com/drinks/',
        'https://emojiterra.com/travel/',
        'https://emojiterra.com/religious-places/',
        'https://emojiterra.com/people-body/',
        'https://emojiterra.com/round-pushpin/',
        'https://emojiterra.com/flowers/',
        'https://emojiterra.com/hundred-points/',
        'https://emojiterra.com/transport-air/',
        'https://emojiterra.com/faces-with-accessories/',
        'https://emojiterra.com/arrows/',
        'https://emojiterra.com/transport-water/',
        'https://emojiterra.com/list/',
        'https://emojiterra.com/reptiles/',
        'https://emojiterra.com/clothing/',
        'https://emojiterra.com/easter/',
        'https://emojiterra.com/science/',
        'https://emojiterra.com/family/',
        'https://emojiterra.com/other-symbols/',
        'https://emojiterra.com/chinese-new-year/',
        'https://emojiterra.com/awards-medals/',
        'https://emojiterra.com/flags/',
        'https://emojiterra.com/arts-crafts/',
        'https://emojiterra.com/neutral-skeptical-faces/',
        'https://emojiterra.com/other-places/',
        'https://emojiterra.com/hearts/',
        'https://emojiterra.com/maps/',
        'https://emojiterra.com/other-objects/',
        'https://emojiterra.com/monkey-faces/',
        'https://emojiterra.com/light-video/',
        'https://emojiterra.com/person-symbol/',
        'https://emojiterra.com/winking-face/',
        'https://emojiterra.com/costumed-faces/',
        'https://emojiterra.com/flags-emoji/',
        'https://emojiterra.com/medical-symbol/',
        'https://emojiterra.com/computer/',
        'https://emojiterra.com/religion/',
        'https://emojiterra.com/beer-mug/',
        'https://emojiterra.com/seafood/',
        'https://emojiterra.com/umbrella/',
        'https://emojiterra.com/emotions/',
        'https://emojiterra.com/camera/',
        'https://emojiterra.com/faces/',
        'https://emojiterra.com/resting-people/',
        'https://emojiterra.com/gestures/',
        'https://emojiterra.com/keycaps/',
        'https://emojiterra.com/symbols/',
        'https://emojiterra.com/halloween/',
        'https://emojiterra.com/tools/',
        'https://emojiterra.com/sleepy-faces/',
        'https://emojiterra.com/subdivision-flags/',
        'https://emojiterra.com/hairstyle/',
        'https://emojiterra.com/food/',
        'https://emojiterra.com/books-papers/',
        'https://emojiterra.com/events/',
        'https://emojiterra.com/warnings/',
        'https://emojiterra.com/sportive-people/',
        'https://emojiterra.com/smiling-faces/',
        'https://emojiterra.com/office/',
        'https://emojiterra.com/sky-weather/',
        'https://emojiterra.com/plants/',
        'https://emojiterra.com/mails/',
        'https://emojiterra.com/cat-faces/',
        'https://emojiterra.com/sound/',
        'https://emojiterra.com/time/',
        'https://emojiterra.com/small-animals/',
        'https://emojiterra.com/birthday/',
        'https://emojiterra.com/locks/',
        'https://emojiterra.com/top-100/',
        'https://emojiterra.com/mammals/',
        'https://emojiterra.com/angry-face/',
        'https://emojiterra.com/body-parts/',
        'https://emojiterra.com/signs/',
        'https://emojiterra.com/phone/',
        'https://emojiterra.com/smiling-face-with-heart-eyes/',
        'https://emojiterra.com/money/',
        'https://emojiterra.com/hands/',
        'https://emojiterra.com/medicine/',
        'https://emojiterra.com/faces-with-affection/',
        'https://emojiterra.com/school-emojis/',
        'https://emojiterra.com/fantasy/',
        'https://emojiterra.com/activities-hobbies/',
        'https://emojiterra.com/skin-tones/',
        'https://emojiterra.com/transport-ground/',
        'https://emojiterra.com/unwell-faces/',
        'https://emojiterra.com/games/',
        'https://emojiterra.com/concerned-faces/',
        'https://emojiterra.com/shopping/',
        'https://emojiterra.com/geographic/',
        'https://emojiterra.com/dishware/',
        'https://emojiterra.com/negative-faces/',
        'https://emojiterra.com/zodiac-signs/',
        'https://emojiterra.com/people/',
        'https://emojiterra.com/alphanumeric-characters/',
        'https://emojiterra.com/winter/',
        'https://emojiterra.com/disappointed-but-relieved-face/']


def get_submoji(url):
    try:
        r = requests.get(url)
        r.encoding = 'utf8'
        soup = BeautifulSoup(r.text, 'lxml')
        name = soup.find('h1').get_text()
        container = soup.find('div', class_="archive-child")

        emoji = container.find_all('span')
        emoji = [x.get_text().strip() for x in emoji]

        return {name: emoji}
    except AttributeError:
        return None




if __name__ == "__main__":
    result = {}
    for url in urls:
        print(f"processing {url}")
        resp = get_submoji(url)
        if resp:
            result.update(resp)
    with open("homecat.json", "w") as fout:
        data = json.dumps(result, indent=2)
        fout.write(data)
