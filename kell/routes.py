from flask        import render_template, url_for
from markupsafe   import escape
from flask        import request
from kell         import app, db
from kell.logic   import schema as dbo

@app.route("/")
def hello_world():
  app.logger.debug("Test")
  app.logger.warning("Warning")
  app.logger.error("An error occured")
  db.create_all()
  return "Hello, World!"

@app.route("/example/<input>")
def example(input):
  print(escape(input))
  return '''<h1> I never knew that flask was this basic</h1><p>yup! She's basic.</p>'''

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

with app.test_request_context():
  ''' I can use this for testing in the future '''
  print(url_for('example', input="Testing"))
  print("url_for('static', filename='style.css') to get static files. Ideally the web server sshould do this. I need to find out how")

with app.test_request_context('/', method='GET'):
  # now you can do something with the request until the
  # end of the with block, such as basic assertions:
  assert request.path == '/'
  assert request.method == 'GET'