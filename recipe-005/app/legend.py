# NOTE: Legend was generated with - 
#       https://patorjk.com/software/taag/#p=display&f=Slant&t=demoapp

class Legend:

    @staticmethod
    def show(release, startup_time):
         legend_text = '''
  ____  ____  ____ 
 / __ `/ __ \/ __ \\
/ /_/ / /_/ / /_/ /
\__,_/ .___/ .___/ 
    /_/   /_/                                               
----------
v{release}
    '''.format(release=release, startup_time=startup_time)
         print(legend_text, flush=True)