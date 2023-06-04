# -*- coding: utf-8 -*-

# NOTE: Legend was generated with - 
#       https://patorjk.com/software/taag/#p=display&f=Slant&t=demoapp

class Legend:

    @staticmethod
    def show(release, startup_time):
         legend_text = '''
       __                                     
  ____/ /__  ____ ___  ____  ____  ____  ____ 
 / __  / _ \/ __ `__ \/ __ \/ __ `/ __ \/ __ \\
/ /_/ /  __/ / / / / / /_/ / /_/ / /_/ / /_/ /
\__,_/\___/_/ /_/ /_/\____/\__,_/ .___/ .___/ 
                               /_/   /_/                                               
----------
v{release}
    '''.format(release=release, startup_time=startup_time)
         print(legend_text, flush=True)