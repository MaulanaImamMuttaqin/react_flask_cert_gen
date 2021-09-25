from api import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable = False)
    password = db.Column(db.String(150), nullable = False)
    username = db.Column(db.String(150), nullable = False)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email = email).first()

    def __repr__(self):
        return '<User {}>'.format(self.username)