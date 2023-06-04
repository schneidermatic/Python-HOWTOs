 # -*- coding: utf-8 -*-

import sys
from src.bootstrap import Bootstrap

def main(app_name, app_release):
   try:
      bootstrap = Bootstrap(app_name, app_release)
      bootstrap.run()
   except Exception as exc:
      print("\nEXCEPTION: " + str(exc) + "\n")
      sys.exit(1)   

if __name__ == "__main__":
   app_name="demoapp"
   app_release="0.1.0"
   main(app_name, app_release)