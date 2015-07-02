from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/index.html')
def index_return():
	return render_template('index.html')

@app.route('/dispersion.html')
def dispersion():
	return render_template('dispersion.html')

@app.route('/double_exposure.html')
def double_exposure():
	return render_template('double_exposure.html')

@app.route('/drawing.html')
def drawing():
	return render_template('drawing.html')

@app.route('/halftone.html')
def halftone():
	return render_template('halftone.html')

@app.route('/lego.html')
def lego():
	return render_template('lego.html')

@app.route('/mosaic.html')
def mosaic():
	return render_template('mosaic.html')

@app.route('/stereoscope.html')
def stereoscope():
	return render_template('stereoscope.html')

@app.route('/text_portrait.html')
def text_portrait():
	return render_template('text_portrait.html')

@app.route('/warhol.html')
def warhol():
	return render_template('warhol.html')


if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)