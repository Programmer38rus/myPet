import bottle
from truckpad.bottle.cors import CorsPlugin, enable_cors

from add import form_list, db_add
app = bottle.Bottle()

@enable_cors
@app.route('/')
def index(): 
	# bottle.response.headers['Access-Control-Allow-Origin'] = '*'
	base_list = form_list()
	db_on_dict = [child.to_dict() for child in base_list]
	
	return {"Family": db_on_dict}

@enable_cors
@app.route('/add/', method="POST")
def add():

	json = bottle.request.json
	db_add(json)

app.install(CorsPlugin(origins=['http://localhost:8081']))

if __name__ == "__main__":
	bottle.run(app, host="localhost", port=8081)
