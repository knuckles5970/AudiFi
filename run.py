from audifi import app


app.config.from_pyfile('../config.py')
app.run(debug=app.config['DEBUG'])
