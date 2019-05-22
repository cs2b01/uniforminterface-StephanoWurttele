from flask import Flask, render_template, request, session, Response, redirect
from database import connector
from model import entities
import json

db=connector.Manager()
engine=db.createEngine()

app=Flask(__name__)

@app.route('/', methods=['GET'])
def index():
	db_session = db.getSession(engine)
	user = entities.Usuario(codigo="201810424", nombre="Stephan", apellido="Wurttele", password="123")
	# user2 = entities.Usuario(codigo="201810715", nombre="Yennifer", apellido="Ramirez", password="456")
	user3 = entities.Usuario(codigo="201810685", nombre="Mayra", apellido="Molina", password="789")
	db_session.add(user)
	db_session.add(user3)
	db_session.commit()
	return render_template('index2.html')


@app.route("/users")
def users():
	db_session = db.getSession(engine)
	users = db_session.query(entities.Usuario)
	data = users[:]
	return Response(json.dumps(data, cls=connector.AlchemyEncoder), mimetype='application/json')

if __name__ == '__main__':
    app.secret_key = ".."
    app.run(port=8080, threaded=True, host=('0.0.0.0'))
