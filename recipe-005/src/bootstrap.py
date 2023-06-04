# -*- coding: utf-8 -*-

from src.config import Config
from src.cliargs import CliArgs
from src.logger import Logger
from src.program import Program
from pathlib import Path

class Bootstrap:

    def __init__(self, app_name, app_release):
      self.name = app_name
      self.release = app_release
      self.config = Config(app_name.split('.')[0],
                           app_release,
                           str(Path.home()))
      self.args = CliArgs().parse(self.config)
      self.logger = Logger(self.config, self.args)

    def run(self):
      logger = self.logger.get_logger()
      logger.info(f"{self.config.app_name }.py is started.")
      program = Program(self.config, self.args, logger)
      program.start()