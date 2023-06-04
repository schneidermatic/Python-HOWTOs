from jinja2 import Environment, select_autoescape, FileSystemLoader
from pyapp.utils import TimeStamp
import json
import os

class TemplateHandler():

    def __init__(self, app_name, template_path, template):
        template_dir = os.path.join(os.path.dirname(__file__), template_path)
        self.env = Environment(
            autoescape=select_autoescape(['json']),
            loader=FileSystemLoader(template_dir),
            trim_blocks=True, 
            lstrip_blocks=True
        )
        self.template = self.env.get_template(template)
    
    def get_data(self):
        timestamp = TimeStamp.format()
        return json.dumps(json.loads(self.template.render(timestamp=timestamp)))