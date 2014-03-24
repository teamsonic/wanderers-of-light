import web

import apps.forum as forum

from utils.jinja import render


urls = (
    '', 'Index',
    '/', 'Index',
    '/forum', forum.app
)



class Index:
    """Main page, duh"""


    def GET(self):
        return render('/index.html')



app = web.application(urls, locals())

if __name__ == '__main__':
    app.run()
