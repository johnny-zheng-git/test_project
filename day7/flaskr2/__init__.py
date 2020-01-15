from .config import DevelopmentConfig
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import click
from flask.cli import with_appcontext
print("=====a=====")


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig())

    db.init_app(app)
    from . import auth
    app.cli.add_command(init_db_command)


    @app.route("/",)
    def index():
        return "<h1>success</h1>"

    return app

def init_db():
    db.drop_all()
    db.create_all()

@click.command("init-db")
@with_appcontext
def init_db_command():
    init_db()
    click.echo("db初始化成功")
