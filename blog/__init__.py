from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

migrate = Migrate(app, db)
from blog import routes, models
from faker import Faker
from blog.models import Entry, db

@app.shell_context_processor
def make_shell_context():
 return {
 "db": db,
 "Entry": models.Entry
 }


def generate_entries(how_many=15):
   fake = Faker()
   for i in range(how_many):
       post = Entry(
       title=fake.sentence(),
       body='\n'.join(fake.paragraphs(15)),
       is_published=True
       )
       db.session.add(post)
   db.session.commit()