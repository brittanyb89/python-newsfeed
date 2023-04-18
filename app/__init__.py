# Used a from...import statement to import the Flask() function
from flask import Flask

# Used the def keyword to define a create_app() function
def create_app(test_config=None):
  # set up app config
  app = Flask(__name__, static_url_path='/') #the app should serve any static resources from the root directory and not from the default /static directory
  app.url_map.strict_slashes = False # trailing slashes are ignored, so /dashoard/ and /dashboard are the same
  app.config.from_mapping(
    SECRET_KEY='super_secret_key' # used to encrypt session cookies
  )

# defined a route for the app to serve at the root URL
  @app.route('/hello') # turns the hello() function into a route
  def hello(): # returns a string
    return 'Hello, World!' # route's response

# As a comparison, the following code shows how to create the same route by using Express.js:
# app.get('/hello', (req, res) => {
#   res.send('Hello, World!');
# });

  return app

#   When Flasks runs the app package, it tries to call a create_app() function.
#  If it doesn't find one, it will throw an error.