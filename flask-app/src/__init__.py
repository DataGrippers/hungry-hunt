# Some set up for the application 

from flask import Flask
from flaskext.mysql import MySQL

# create a MySQL object that we will use in other parts of the API
db = MySQL()

def create_app():
    app = Flask(__name__)
    
    # secret key that will be used for securely signing the session 
    # cookie and can be used for any other security related needs by 
    # extensions or your application
    app.config['SECRET_KEY'] = 'someCrazyS3cR3T!Key.!'

    # these are for the DB object to be able to connect to MySQL. 
    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_PASSWORD'] = open('/secrets/db_root_password.txt').readline().strip()
    app.config['MYSQL_DATABASE_HOST'] = 'db'
    app.config['MYSQL_DATABASE_PORT'] = 3306
    app.config['MYSQL_DATABASE_DB'] = 'HungryHunt'  # Change this to your DB name

    # Initialize the database object with the settings above. 
    db.init_app(app)
    
    # Add the default route
    # Can be accessed from a web browser
    # http://ip_address:port/
    # Example: localhost:8001
    @app.route("/")
    def welcome():
        return "<h1>Welcome to the 3200 boilerplate app</h1>"

    # Import the various Beluprint Objects
    from src.customers.customers import customers
    from src.products.products  import products
    from src.appetizers.appetizers import appetizers
    from src.desserts.desserts import desserts
    from src.dietaryrestrictions.dietaryrestrictions import dietary_restrictions
    from src.drinks.drinks import drinks
    from src.kidsmeal.kidsmeal import kidsmeals
    from src.location.location import location
    from src.maincourse.maincourse import maincourses
    from src.menu.menu import menu
    from src.photo.photo import photos
    from src.rating.rating import ratings
    from src.restaurant.restaurant import restaurants
    from src.users.users import users


    # Register the routes from each Blueprint with the app object
    # and give a url prefix to each
    app.register_blueprint(customers,   url_prefix='/c')
    app.register_blueprint(appetizers,   url_prefix='/a')
    app.register_blueprint(desserts,   url_prefix='/d')
    app.register_blueprint(dietary_restrictions,   url_prefix='/d')
    app.register_blueprint(drinks,   url_prefix='/d')
    app.register_blueprint(kidsmeals,   url_prefix='/k')
    app.register_blueprint(location,   url_prefix='/l')
    app.register_blueprint(maincourses,   url_prefix='/m')
    app.register_blueprint(menu,   url_prefix='/m')
    app.register_blueprint(photos,   url_prefix='/p')
    app.register_blueprint(ratings,   url_prefix='/r')
    app.register_blueprint(restaurants,   url_prefix='/r')
    app.register_blueprint(users,   url_prefix='/u')



    # Don't forget to return the app object
    return app