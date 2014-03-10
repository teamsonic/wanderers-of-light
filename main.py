import web
from jinja2 import Environment, FileSystemLoader

import apps.main as index


urls = (
    '', index.app,
    '/', index.app,
)

app = web.application(urls, globals())

if __name__ == '__main__':
    app.run()
