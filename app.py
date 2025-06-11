from bottle import route, run, request, template, static_file, get



class Aplication:
	# static routes
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
	@route('/login')  # @get('/login')
	def login():
		return template('login')

	@staticmethod
	def check_login(username, password):
		d = {'marcos': 'python', 'joao': 'java', 'pedro': 'go'}
		if username in d.keys() and d[username] == password:
			return True
		return False

	@staticmethod
	@route('/login', method='POST')  # @post('/login')
	def acao_login():
		username = request.forms.get('username')
		password = request.forms.get('password')
		if Aplication.check_login(username, password):
			return template('sucesso_login', username=username)
		else:
			return template('login_com_falha')

	@staticmethod
	def run():
		run(host='localhost', port=8080, debug=True, reloader=True)
