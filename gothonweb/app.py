import web
from gothonweb import map

urls = (
  '/game', 'GameEngine',
  '/', 'Index',
  "/count", "count",
  "/reset", "reset"
)

app = web.application(urls, globals())

# little hack so that debug mode works with sessions
if web.config.get('_session') is None:
    store = web.session.DiskStore('sessions')
    session = web.session.Session(app, store, initializer={'count': 10})
	
    web.config._session = session
else:
    session = web.config._session

render = web.template.render('templates/', base="layout")


class Index(object):
    def GET(self):
        # this is used to "setup" the session with starting values
        session.room = map.START
        session.dict = [['Bob', 10]]
        web.seeother("/game")


class GameEngine(object):

    def GET(self):
        if session.room:
            return render.show_room(room=session.room, count=session.dict[0][1])
        else:
            # why is there here? do you need it?
            session.dict[0][1] = session.dict[0][1] - 1
            print session.dict[0][1]
            return render.you_died()

    def POST(self):
        form = web.input(action=None)

        # there is a bug here, can you fix it?
        if session.room and form.action:
            session.room = session.room.go(form.action)

        web.seeother("/game")

if __name__ == "__main__":
    app.run()