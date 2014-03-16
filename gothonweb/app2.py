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
lst2 = []
cname = "No Name"
otherGame = False

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
        return render.firstpage()
		
    def POST(self):
        global cname
        f1 = web.input(value="")
        cname=f1.value
        web.seeother("/")
		
		
class Start(object):
    def GET(self):
        global otherGame
        otherGame = False
        session.room = map.START
        web.seeother("/game")
		
class Start2(object):
    def GET(self):
        global otherGame
        otherGame = True
        session.room = map.START2
        web.seeother("/game")
		
class Score(object):
	def GET(self):
		global otherGame
		try:
			file2 = open('scores2.json', 'r')
			loaded2 = json.load(file2)
			file2.close()
		except IOError:
				loaded2 = "no"
		try:
			file = open('scores.json', 'r')
			loaded = json.load(file)
			file.close()
		except IOError:
				loaded = "no"
		return render.scores(loaded, loaded2)


class Clear(object):
	def GET(self):
		if os.path.isfile("scores.json"):        
			os.remove("scores.json")
			del lst[:]
		if os.path.isfile("scores2.json"):
			os.remove("scores2.json")
			del lst2[:]
		web.seeother("/score")

class GameEngine(object):
     
    def GET(self):
        global cname
        global otherGame
        if session.room and session.count >= 1:
            won = False
            if session.room.description == map.the_end_winner.description:
                won = True
                lst.append([cname, session.count])
                file = open("scores.json", "w")
                json.dump(lst, file, sort_keys = True, indent = 4)
                file.close()
            elif session.room.description == map.fight_win.description:
                won = True
                lst2.append([cname, session.count])
                file2 = open("scores2.json", "w")
                json.dump(lst2, file2, sort_keys = True, indent = 4)
                file2.close()
            if session.room.name == "death" or session.room.name == "Oh no! You have failed."\
            or session.room.name == "Oh no! You died." or (session.room.name == "The End" and won == False):
				session.count -= 1     
            return render.show_room(room=session.room, count=session.count, n=cname, win=won)
        elif (session.count >= 1):
            session.count -= 1
            return render.you_died(otherGame)
        else:
            return render.gameover()
			

    def POST(self):
        form = web.input(action=None)
        if session.room and form.action:
            session.room = session.room.go(form.action)

        web.seeother("/game")

if __name__ == "__main__":
    app.run()
