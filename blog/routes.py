from flask import Flask, render_template
from blog import app
from blog.models import Entry
app = Flask(__name__)  
from faker import Faker
from blog.models import Entry, db


@app.route("/")
def index():
 all_posts = Entry.query.filter_by(is_published=True).order_by(Entry.pub_date.desc())
 return render_template("homepage.html", all_posts=all_posts)

def generate_entries(how_many=10):
   fake = Faker()
   for i in range(how_many):
       post = Entry(
           title=fake.sentence(),
           body='\n'.join(fake.paragraphs(15)),
           is_published=True
       )
       db.session.add(post)
   db.session.commit()
   
if __name__ == "__main__":
    app.run(debug=True)
   