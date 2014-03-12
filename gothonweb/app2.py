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
key = [player[0] for player in lst]
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
        list.append((cname, session.count))
        web.seeother("/")
		
		
class Start(object):
    def GET(self):
        global cname
        # this is used to "setup" the session with starting values
        session.room = map.START
        print key
        lst.append((cname, session.count))
        print [player[1] for player in lst]
        web.seeother("/game")
		
class Score(object):
    def GET(self):
		str1 = ""
		for i, name in enumerate(key):
			str1 += name + " : " + str(lst[i][1])
		if str1 == "":
			str1 = "no values to display"
		return render.scores(s=str1)



class GameEngine(object):
     
    def GET(self):
        global cname
        print key
        if session.room and session.count >= 1:
            won = False
            if session.room.description == map.the_end_winner.description:
                won = True
                lst.append((key[-1], session.count))
                file = open("scores.json", "w")
                json.dump(lst, file, sort_keys = True, indent = 4)
                file.close()
            if session.room.name == "death" or (session.room.name == "The End" and won == False):
                session.count -= 1
            return render.show_room(room=session.room, count=lst[cname], n=cname, win=won)
        elif (session.count >= 1):
            # why is there here? do you need it?
            session.count -= 1
            return render.you_died()
        else:
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