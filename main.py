import web

import apps.main as index


urls = (
    '', index.app,
    '/', index.app,
)

#Create a web appplication instance
app = web.application(urls, globals())

#Add URL mapping
app.add_mapping('', index.app)
app.add_mapping('/', index.app)

if __name__ == '__main__':
    app.run()
