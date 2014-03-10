import web

from utils.render import render

urls = (
    '', 'Index',
    '/', 'Index',
)



class Index:


    def GET(self):
        return render('stuff/index.html')


app = web.application(urls, locals())

if __name__ == '__main__':
    app.run()
