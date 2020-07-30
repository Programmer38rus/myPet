import bottle
from truckpad.bottle.cors import CorsPlugin, enable_cors

from add import form_list, db_add, find_one_member
app = bottle.Bottle()

@enable_cors
@app.route('/')
def index():

	base_list = form_list()
	db_on_dict = [child.to_dict() for child in base_list]

	return {"Family": db_on_dict}

@enable_cors
@app.route('/add/', method="POST")
def add():

	json = bottle.request.json
	db_add(json)

	return "OK - добавлен член семьи"

@enable_cors
@app.route('/api/family/<uid:int>', method=['GET', 'PUT', 'DELETE'])
def change_and_delete(uid):
	if bottle.request.method == "GET":
		finded = find_one_member(uid)
		return finded

app.install(CorsPlugin(origins=['http://localhost:8081']))

if __name__ == "__main__":
	bottle.run(app, host="localhost", port=8081)
