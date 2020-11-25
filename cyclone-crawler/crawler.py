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
        for basin in basin_storms:
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
                name = cname.replace(f'({speed})', ''),
                data[cid] = {
                    "cid": cid,
                    "name": name,
                    "speed": speed,
                    "url": ele.a.attrs['href'],
                    "img": ele.img.attrs['src'],
                    "active": True
                }

            active_cyclones[region] = data

        return active_cyclones

    except Exception as e:
        logger.error(e)


