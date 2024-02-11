from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def setup_database(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()
    return db

class Email(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String(120), nullable=False)
    recipient = db.Column(db.String(120), nullable=False)
    subject = db.Column(db.String(120), nullable=False)
    body = db.Column(db.Text, nullable=False)

class SocialMediaPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.Text, nullable=False)  # Assuming you have a User model elsewhere
    content = db.Column(db.Text, nullable=False)
    hashtags = db.Column(db.Text, nullable=False)

class CustomerReview(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.Text, nullable=False)  # Assuming a Customer model exists
    product_name = db.Column(db.Text, nullable=False)  # Assuming a Product model exists
    review_text = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)  # Assuming a scale of 1-5