# -*- coding: utf-8 -*-

import time
import logging

class Logger():

    def __init__(self, config, args):
        self.config = config
        self.args = args

    def get_logger(self):
        return self.logger
        
    def set_logger(self, logger_name):
        numeric_loglevel = getattr(logging, self.args.loglevel.upper(), None)
        logging.basicConfig(level=numeric_loglevel,format=self.config.log_format,datefmt=self.config.log_date_format)
        logging.Formatter.converter = time.gmtime
        self.logger = logging.getLogger(logger_name)