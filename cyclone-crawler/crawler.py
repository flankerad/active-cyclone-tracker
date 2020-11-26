import requests
from bs4 import BeautifulSoup
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def get_active_cyclones(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, features='html.parser')
        basin_storms = soup.find_all("div", class_="basin_storms")

        active_cyclones = {}
        for basin in basin_storms
            region = basin.h3
            lis = basin.ul.children
            data = {}
            for ele in lis:
                if len(ele) == 1:
                    continue
                # Individual region storm
                text = ele.a.text.split("-")
                cid = text[0].strip()
                cname = text[1].strip()
                speed = cname.partition('(')[2].partition(')')[0]
                name = cname.replace(f'({speed})', '')
                name = name.rpartition(' ')
                ctype = name[0].strip()
                name = name[1].strip()
                active_cyclones.append(f"({cid}, {name}, {speed}, {ele.a.attrs['href']},
                                        {ele.img.attrs['src']}, {ctype}, {region})")

        return ','.join(active_cyclones)

    except Exception as e:
        logger.error(e)


