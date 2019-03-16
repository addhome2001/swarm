from .main import db

class Counter(db.Model):
    __tablename__ ='Counter'
    id = db.Column(db.Integer, primary_key=True)
    counts = db.Column(db.Integer, default=0)

    def __repr__(self):
        return '<Counter %r>' % self.counts