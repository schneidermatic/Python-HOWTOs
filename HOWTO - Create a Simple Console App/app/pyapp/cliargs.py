import sys
import argparse
from argparse import RawTextHelpFormatter
from pyapp.legend import Legend
from pyapp.utils import TimeStamp

class CliArgs():

   def parse(self, config):

      parser = argparse.ArgumentParser(prog=f"{ config.app_name }",
                                       description=f"{ config.app_name } - Skeleton for a simple Python CLI Project",
                                       usage='%(prog)s [options]',
                                       formatter_class=RawTextHelpFormatter)

      parser.add_argument('-f', '--folder',
                        help='set the template folder',
                        dest='folder', default=config.template_folder)

      parser.add_argument('-l', '--loglevel',
                        help='set the loglevel [DEBUG|INFO|WARN|ERROR|CRITICAL]',
                        dest='loglevel', default=config.loglevel)

      parser.add_argument('-L', '--Legend', help='show legend',
                        dest='legend', action='store_true', default=config.validate_sys_argv_len) 

      parser.add_argument('-q', '--quiet', help='run in quiet mode',
                        dest='quiet', action='store_true') 

      parser.add_argument('-t', '--template',
                        help='set the template file - default: template.json.j2',
                        dest='template', default=config.template_file)

      parser.add_argument('-v','--version', action='version', version=f"%(prog)s { config.app_release }")

      args = parser.parse_args()

      timestamp = TimeStamp.format()
      if args.legend == True: Legend.show(config.app_release, timestamp)

      validate_sys_arg_len = True
      if validate_sys_arg_len and len(sys.argv)==1 :
         parser.print_help(sys.stderr)
         sys.exit(1)

      return args