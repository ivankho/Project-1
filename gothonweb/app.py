import web
from gothonweb import map
from pandas import *

urls = (
  '/game', 'GameEngine',
  '/', 'Index',
  '/score', 'Score',
  "/start", "Start"
)

app = web.application(urls, globals())
dict = {}
global cname

# little hack so that debug mode works with sessions
if web.config.get('_session') is None:
    store = web.session.DiskStore('sessions')
    session = web.session.Session(app, store, initializer={'count': 2})
    web.config._session = session
else:
    session = web.config._session

render = web.template.render('templates/', base="layout")


class Index(object):
    def GET(self):
        # this is used to "setup" the session with starting values
        return render.firstpage()
		
    def POST(self):
        global cname
        f1 = web.input(action2="No Name")
        session.count = 2
        cname=f1.action2
        dict.update({cname : session.count})
        web.seeother("/")
		
		
class Start(object):
    def GET(self):
        global cname
        # this is used to "setup" the session with starting values
        session.room = map.START
        print dict.keys()
        dict.update({cname : session.count})
        print dict.values()
        web.seeother("/game")
		
class Score(object):
    def GET(self):
        str1 = ""
        for key in dict.keys():
            #My attempt to construct a dataframe so as to display the scores in a list
            #str1 = DataFrame(data=int(dict[key]), index=key)
            str1 += key + " : " + str(dict[key]) + '\t'
        if str1 == "":
            str1="No values to display!"
        return render.scores(s=str1)


class GameEngine(object):
     
    def GET(self):
        global cname
        print dict.keys()
        if session.room and session.count >= 1:
            won = False
            if session.room.description == map.the_end_winner.description:
                won = True
                session.count = 2
                dict.update({dict.keys()[-1] : session.count})
            if session.room.name == "death" or (session.room.name == "The End" and won == False):
                session.count -= 1
                dict.update({dict.keys()[-1] : session.count})
            return render.show_room(room=session.room, count=dict[cname], n=cname, win=won)
        elif (session.count >= 1):
            # why is there here? do you need it?
            session.count -= 1
            return render.you_died()
        else:
			return render.gameover()
			

    def POST(self):
        form = web.input(action=None)

        # there is a bug here, can you fix it?
        if session.room and form.action:
            session.room = session.room.go(form.action)

        web.seeother("/game")

if __name__ == "__main__":
    app.run()