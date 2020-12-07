import json
import logging
from app.db import get_data
from config import KEYS

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def get_response(conn, path):
      """
      Parses url params from Path
      Creates params dictionary
      params: {
            fields: <values>.
            conditions: <values>
            }
      for building query by db.query_builder

      Parameters
      ----------
      conn: object, mandatory
            postgres connection object

      path: str, mandatory
            url parameters of API

      Returns
      ----------
      list
            a list of dictionaries of active cyclones
            with time updated into string
      """

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
