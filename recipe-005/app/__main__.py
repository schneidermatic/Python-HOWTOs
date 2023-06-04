"""The main entry point. Invoke as `http' or `python -m httpie'.

"""

import sys
from app.bootstrap import Bootstrap

def main():

   app_name="app"
   app_release="0.1.0"

   try:
      bootstrap = Bootstrap(app_name, app_release)
      bootstrap.run()
   except Exception as exc:
      print("\nEXCEPTION: " + str(exc) + "\n")
      sys.exit(1)   

if __name__ == "__main__":

   main()