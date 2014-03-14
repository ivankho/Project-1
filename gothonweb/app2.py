import web
from gothonweb import map
import json

urls = (
  '/game', 'GameEngine',
  '/', 'Index',
  '/score', 'Score',
  "/start", "Start"
)

app = web.application(urls, globals())
lst = []
key = []
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
        f1 = web.input(value="")
        session.count = 2
        cname=f1.value
<<<<<<< HEAD
=======
        #lst.append([cname, session.count])
        print lst
>>>>>>> 5031efacf0a05c84cc155ed9c74cd19ca1d5cc2e
        web.seeother("/")
		
		
class Start(object):
    def GET(self):
        global cname
        # this is used to "setup" the session with starting values
        session.room = map.START
<<<<<<< HEAD
=======
        #lst.append([cname, session.count])
>>>>>>> 5031efacf0a05c84cc155ed9c74cd19ca1d5cc2e
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



class GameEngine(object):
     
    def GET(self):
        global cname
        print key
        if session.room and session.count >= 1:
            won = False
            if session.room.description == map.the_end_winner.description:
                won = True
                lst.append([cname, session.count])
                file = open("scores.json", "w")
                json.dump(lst, file, sort_keys = True, indent = 4)
                file.close()
            if session.room.name == "death" or (session.room.name == "The End" and won == False):
				session.count -= 1     
            return render.show_room(room=session.room, count=session.count, n=cname, win=won)
        elif (session.count >= 1):
            # why is there here? do you need it?
            session.count -= 1
            return render.you_died()
        else:
			lst.append([cname, session.count])
			file = open("scores.json", "w")
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
