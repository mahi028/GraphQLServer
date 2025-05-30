from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_graphql import GraphQLView
from flask_cors import CORS
from application.dummy import index_blueprint
from .graphql import schema
from .models import db

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///graphql_app.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    CORS(app)  # Enable CORS for all routes
    db.init_app(app)

    app.add_url_rule(
        '/graphql',
        view_func=GraphQLView.as_view(
            'graphql',
            schema=schema,
            graphiql=True
        )
    )

    app.register_blueprint(index_blueprint)

    return app