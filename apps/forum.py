import web

from utils.jinja import render

urls = (
    '', 'Index',
    '/', 'Index',
    '/board/(.*?)', 'Board',
)



class Index:


    def GET(self):
        """
        Return the list of boards
        """
        return render('/forum/index.html')



class Board:


    def GET(self, board):
        """
        Return the page of topics associated with this board
        """
        return render('/forum/board.html')


app = web.application(urls, locals())

if __name__ == '__main__':
    app.run()
