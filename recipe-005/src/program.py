# -*- coding: utf-8 -*-

import os
import sys
import time
from src.template import TemplateHandler

class Program():

    def __init__(self, config, args, logger):
        self.config = config
        self.args = args
        self.logger = logger

    def start(self):
        for i in range(10):
            template_handler = TemplateHandler(app_name=self.config.app_name , template_path=self.args.folder, template=self.args.template)
            template_data = template_handler.get_data()
            self.logger.info(template_data)
            time.sleep(1)