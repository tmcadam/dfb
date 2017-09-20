import os

from jinja2 import Template

TEMPLATE_FILE = 'httpd.conf.template'
CONF_OUT = 'httpd.conf'

PATH = os.path.split(os.path.abspath(__file__))[0].split("/")[1:]
home_path = os.path.join("/", *PATH[:2])
apache_path = os.path.join("/", *PATH[:-1], "apache2")
python_path = os.path.join("/", *PATH)
python_home = os.path.join(python_path, ".env")
wsgi_path = os.path.join(python_path, 'dfb', 'wsgi.py')
app_name = PATH[-2]

kwargs = {  "home_path": home_path,
            "wsgi_script": wsgi_path,
            "app_name": app_name,
            "apache_path": apache_path,
            "python_home": python_home,
            "python_path": python_path,
            "port": 21457
}

with open(TEMPLATE_FILE) as file_template:
    template = Template(file_template.read())
    html = template.render(**kwargs)
    with open(CONF_OUT, 'w') as file_out:
        file_out.write(html)
        print('httpd.conf output successful')
