import os

from bottle import route, run
from bottle import request, template
from bottle import static_file, get
from bottle import error

# static routes
class Aplication:
	@staticmethod
	@get('/<filename:re:.*\.css>')
	def stylesheets(filename):
		return static_file(filename, root='static/css')

	@staticmethod
	@get('/<filename:re:.*\.js>')
	def javascripts(filename):
		return static_file(filename, root='static/js')

	@staticmethod
	@get('/<filename:re:.*\.(jpg|png|gif|ico)>')
	def images(filename):
		return static_file(filename, root='static/img')

	@staticmethod
	@get('/<filename:re:.*\.(eot|ttf|woff|svg)>')
	def fonts(filename):
		return static_file(filename, root='static/fonts')

	@staticmethod
	@route('/')
	def login():
		return template('login')

	@staticmethod
	def check_login(username, password):
		d = {'marcos': 'python', 'joao': 'java', 'pedro': 'go'}
		if username in d.keys() and d[username] == password:
			return True
		return False

	@staticmethod
	@route('/', method='POST')  # @post('/login')
	def acao_login():
		username = request.forms.get('username')
		password = request.forms.get('password')

		if not Aplication.check_login(username, password):
			return template('erro_login', sucesso=False, nome=username)

		return template('sucesso_login', nome=username)

	@staticmethod
	@error(404)
	def error404(erro):
		print(erro)
		return template('pagina404')

	@staticmethod
	def run():
		if os.environ.get('APP_LOCATION') == 'heroku':
			port = int(os.environ.get('PORT', 5000))
			run(host='0.0.0', port=port)
		else:
			run(host='localhost', port=8080, debug=True, reloader=True)



