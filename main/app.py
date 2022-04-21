from flask import Flask

from main.functions import square_root, circle_area


def create_app():
	app = Flask(__name__)

	@app.route("/")
	def index():
		return f"Hello world! \n The square root of 4 is {str(square_root(4))}, " \
			f"and the circle with radius 2 has area of {str(circle_area(2))}"
	
	return app



