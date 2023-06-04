# NOTE: Legend was generated with - 
#       https://patorjk.com/software/taag/#p=display&f=Slant&t=demoapp

class Legend:

    @staticmethod
    def show(release, startup_time):
         legend_text = '''
    ____  __  ______ _____  ____ 
   / __ \/ / / / __ `/ __ \/ __ \\
  / /_/ / /_/ / /_/ / /_/ / /_/ /
 / .___/\__, /\__,_/ .___/ .___/ 
/_/    /____/     /_/   /_/                                           

----------
v{release}
    '''.format(release=release, startup_time=startup_time)
         print(legend_text, flush=True)