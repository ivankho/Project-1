import web
from gothonweb import map
import json
import os

urls = (
  '/game', 'GameEngine',
  '/', 'Index',
  '/score', 'Score',
  "/start", "Start",
  "/start2", "Start2",
  "/clear", "Clear"
)

app = web.application(urls, globals())
lst = []
key = []
cname = "No Name"
global otherGame

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
        session.count = 2
        # this is used to "setup" the session with starting values
        return render.firstpage()
		
    def POST(self):
        global cname
        f1 = web.input(value="")
        cname=f1.value
        #lst.append([cname, session.count])
        print lst
        web.seeother("/")
		
		
class Start(object):
    def GET(self):
        global cname
        global otherGame
        otherGame = False
        # this is used to "setup" the session with starting values
        session.room = map.START
        #lst.append([cname, session.count])
        key=[player[0] for player in lst]
        #print [player[1] for player in lst] <--Dont really need right? -Tony, Yvonne
        #print key
        web.seeother("/game")
		
class Start2(object):
    def GET(self):
        global cname
        global otherGame
        otherGame = True
        # this is used to "setup" the session with starting values
        session.room = map.START2
        #lst.append([cname, session.count])
        key=[player[0] for player in lst]
        #print [player[1] for player in lst] <--Dont really need right? -Tony, Yvonne
        #print key
        web.seeother("/game")
		
class Score(object):
    def GET(self):
		try:
			file = open('scores.json', 'r')
			loaded = json.load(file)
			file.close()
		except IOError:
			loaded = "no"
		return render.scores(loaded)

class Clear(object):
	def GET(self):
		os.remove("scores.json")
		del lst[:]
		web.seeother("/score")

class GameEngine(object):
     
    def GET(self):
        global cname
        global otherGame
        print key
        if session.room and session.count >= 1:
            won = False
            if session.room.description == map.the_end_winner.description:
                won = True
                lst.append([cname, session.count])
                file = open("scores.json", "a")
                json.dump(lst, file, sort_keys = True, indent = 4)
                file.close()
            if session.room.name == "death" or (session.room.name == "The End" and won == False):
				session.count -= 1     
            return render.show_room(room=session.room, count=session.count, n=cname, win=won)
        elif (session.count >= 1):
            # why is there here? do you need it?
            session.count -= 1
            return render.you_died(otherGame)
        else:
			lst.append([cname, session.count])
			file = open("scores.json", "a")
			json.dump(lst, file, sort_keys = True, indent = 4)
			file.close()
			return render.gameover()
			

    def POST(self):
        form = web.input(action=None)
        # there is a bug here, can you fix it?
        if session.room and form.action:
            session.room = session.room.go(form.action)

        web.seeother("/game")

if __name__ == "__main__":
    app.run()
