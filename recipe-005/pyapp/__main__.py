"""The main entry point. Invoke as `pyapp' or `python -m pyapp'.

"""

import sys
from pyapp.bootstrap import Bootstrap

def main():

   app_name="pyapp"
   app_release="0.1.0"

   try:
      bootstrap = Bootstrap(app_name, app_release)
      bootstrap.run()
   except Exception as exc:
      print("\nEXCEPTION: " + str(exc) + "\n")
      sys.exit(1)   

if __name__ == "__main__":
   main()