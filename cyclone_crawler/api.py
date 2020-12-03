import json
import logging
from db import get_data
from config import KEYS

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def get_response(conn, path):
      params = {}
      params['conditions'] = []

      if '?' in path:
            path = path[2:]
            for p in path.split('&'):
                  if 'search' in p:
                        params['fields'] = p.split('=')[1]
                  params['conditions'].append(p)

      data = get_data(conn, params)
      resp = []

      for i in data:
            d = dict(zip(KEYS, i))
            d['updated_at'] = d['updated_at'].\
                              strftime('%d-%m-%Y%H:%M:%S.%f')
            d['created_at'] = d['created_at'].\
                              strftime('%d-%m-%Y%H:%M:%S.%f')
            resp.append(d)

      return resp
