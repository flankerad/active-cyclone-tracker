import requests
import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def api(err, res):
      logger.info(f"ERR:{err} RESP:{res}")

# Define GET API
