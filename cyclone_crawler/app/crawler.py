import requests
from bs4 import BeautifulSoup
from datetime import datetime
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)



def get_active_cyclones(url):
    """
    Get active cyclones scraps url and returns HTML
    which is then parsed by Beautiful soup
    Extracts fields for updating in database

    Parameters
    ----------
    url: str, mandatory
        url to scrap active cyclones

    Returns
    ----------
    list
        a list of string of database fields
    """
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, features='html.parser')
        basin_storms = soup.find_all("div", class_="basin_storms")

        active_cyclones = []
        for basin in basin_storms:
            region = basin.h3.text
            lis = basin.ul.children
            for ele in lis:
                if len(ele) == 1:
                    continue
                # Individual region storm
                text = ele.a.text.split("-")
                cid = text[0].strip()
                cname = text[1].strip()
                speed = cname.partition('(')[2].partition(')')[0] or 'null'
                name = cname.replace(f'({speed})', '')
                name = name.rpartition(' ')
                ctype = name[0].strip() or 'null'
                name = name[-1].strip()
                img = ele.img.attrs['src'].strip()
                href = ele.a.attrs['href'].strip()
                updated_at = datetime.now().isoformat(sep=' ',
                                timespec='microseconds')

                active_cyclones.append(f"('{cid}','{name}','{speed}','{ctype}','{region}','{href}','{img}', '{updated_at}')")

        return ','.join(active_cyclones)

    except Exception as e:
        logger.error(e)