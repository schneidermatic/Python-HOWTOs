# -*- coding: utf-8 -*-

import os

class Config():

    def __init__(self, app_name, app_release, app_home, app_pid):
        self.app_name = app_name
        self.app_release = app_release
        self.app_home = app_home
        self.app_pid_file = os.environ.get("APP_PID_FILE", app_pid)
        self.validate_sys_argv_len = os.environ.get("APP_VALIDATE_SYS_ARGV_LEN", False)
        self.log_format = '%(asctime)s.%(msecs)03d %(levelname)s - %(message)s'
        self.log_date_format = '%Y-%m-%dT%H:%M:%S'
        self.loglevel = os.environ.get("APP_LOG_LEVEL", "ERROR")
        self.template_folder = os.environ.get("APP_TEMPLATE_FOLDER")
        self.template_file = os.environ.get("APP_TEMPLATE_FILE", "template.json.j2")