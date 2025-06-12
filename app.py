
from model.enums.redirecionamento_enum import RedirecionamentoEnum, get_route_path
from venv.Scripts.bottle import static_file, get, route, template, request, error, run


class Aplication:
	# static routes
	@staticmethod
	@get('/<filename:re:.*\.css>')
	def stylesheets(filename):
		return static_file(filename, root=get_route_path(RedirecionamentoEnum.STYLESHEETS))

	@staticmethod
	@get('/<filename:re:.*\.js>')
	def javascripts(filename):
		return static_file(filename, root=get_route_path(RedirecionamentoEnum.JAVASCRIPTS))

	@staticmethod
	@get('/<filename:re:.*\.(jpg|png|gif|ico)>')
	def images(filename):
		return static_file(filename, root=get_route_path(RedirecionamentoEnum.IMAGES))

	@staticmethod
	@get('/<filename:re:.*\.(eot|ttf|woff|svg)>')
	def fonts(filename):
		return static_file(filename, root=get_route_path(RedirecionamentoEnum.FONTS))

	@staticmethod
	@route('/login')  # @get('/login')
	def login():
		return template(get_route_path(RedirecionamentoEnum.LOGIN))

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
			return template(get_route_path(RedirecionamentoEnum.SUCESSO_LOGIN), username=username)
		else:
			return template(get_route_path(RedirecionamentoEnum.LOGIN_COM_FALHA))

	## Metodo que trata o erro 404
	@staticmethod
	@error(404)
	def erro_404(erro):
		print(str(erro))
		return template(get_route_path(RedirecionamentoEnum.ERRO_404))

	@staticmethod
	def run():
		run(host='localhost', port=8080, debug=True, reloader=True)

