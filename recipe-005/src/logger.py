# -*- coding: utf-8 -*-

import time
import logging
from sys import stdout

class Logger():

    def __init__(self, config, args):
        self.config = config
        self.args = args
        numeric_loglevel = getattr(logging, args.loglevel.upper(), None)
        logging.basicConfig(stream=stdout,level=numeric_loglevel,format=config.log_format,datefmt=config.log_date_format)
        logging.Formatter.converter = time.gmtime
        self.logger = logging.getLogger(__name__)

    def get_logger(self):
        return self.logger