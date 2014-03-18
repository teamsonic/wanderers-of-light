import web

import apps.stuff as stuff

from utils.jinja import render


urls = (
    '', 'Index',
    '/', 'Index',
    '/stuff', stuff.app
)



class Index:
    """Main page, duh"""


    def GET(self):
        return render('/index.html', {'stuff': 'rawr'})



app = web.application(urls, locals())

if __name__ == '__main__':
    app.run()
