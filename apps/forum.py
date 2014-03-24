import json
from storm.locals import Desc
import web

from utils.jinja import render
from utils.sanitize import sanitizeHtml

from wld.db import getStore
from wld.board import Board, Thread, Message

urls = (
    '', 'Boards',
    '/', 'Boards',
    '/board/([0-9]*)', 'Threads',
    '/board/([0-9]*)/thread/([0-9]*)', 'Messages',
)



class Boards:


    def GET(self):
        """
        Return the index page template with Board info
        """
        store = getStore()
        boards = store.find(Board).order_by(Board.name)
        for board in boards:
            threads = board.threads
            messages_count = 0
            for thread in threads:
                messages_count = messages_count + thread.messages.count()
            board.topics = threads.count()
            board.messages = messages_count
            
        return render('/forum/boards.html', {'boards': boards})



class Threads:


    def GET(self, board_id):
        """
        Return the page of topics associated with this board
        """
        store = getStore()
        board = store.find(Board, Board.id == int(board_id)).one()
        unsorted_threads = board.threads
        #Get each Thread's latest message
        for thread in unsorted_threads:
            messages = thread.messages
            thread.replies = messages.count()
            thread.latest_message = messages.order_by(Desc(Message.created)).first()
        #Sort threads by most recent activity/message posted
        threads = sorted(unsorted_threads, key=lambda m: m.latest_message.created)[::-1]
        return render('/forum/threads.html', {'threads': threads, 'board': board})


    def POST(self, board_id):
        """
        Add a new thread, unless one of the same name already exists
        """
        data = json.loads(web.data())
        web.debug(data)
        name = data.get('name', None)
        message = data.get('message', None)
        if not name or not message:
            raise Exception

        store = getStore()
        possible_dupe = store.find(Thread, Thread.name == name).one()
        if possible_dupe:
            return "dupe"
        new_thread = store.add(Thread())
        new_thread.name = name
        new_thread.board_id = int(board_id)
        new_thread.user_id = 1

        store.flush()

        first_message = store.add(Message())
        first_message.message = message
        first_message.user_id = 1
        first_message.thread_id = new_thread.id
        
        store.commit()

        thread_id = str(new_thread.id)
        new_thread_url = '/forum/board/' + board_id + '/thread/' + thread_id

        return new_thread_url



class Messages:


    def GET(self, board_id, thread_id):
        """
        Return the page of messages for a thread
        """
        store = getStore()
        thread = store.find(Thread, Thread.id == int(thread_id)).one()
        board = store.find(Board, Board.id == thread.board_id).one()
        messages = thread.messages.order_by(Message.created)
        return render('/forum/messages.html', {'messages': messages, 'thread': thread, 'board': board})


    def POST(self, board_id, thread_id):
        """
        Create a new message
        """
        msg = json.loads(web.data()).get('message', None)
        if not msg:
            raise Exception("No message found")

        store = getStore()
        message = store.add(Message())
        message.user_id = 1
        message.thread_id = int(thread_id) 
        message.message = sanitizeHtml(msg)
        store.commit()
    
        return

app = web.application(urls, locals())

if __name__ == '__main__':
    app.run()
