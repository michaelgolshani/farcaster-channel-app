from datetime import datetime
from api.index import db
from datetime import datetime
from api.index import db


class Channel(db.Model):
    __tablename__ = "channels"
    id = db.Column(db.String(100), primary_key=True,
                   unique=True, nullable=False)
    url = db.Column(db.String(200), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    follower_count = db.Column(db.Integer, nullable=False, default=0)
    object = db.Column(db.String(100), nullable=False, default="channel")
    image_url = db.Column(db.String(200), nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    parent_url = db.Column(db.String(200), nullable=False)



    def __repr__(self):
        return f"Channel {self.name}"


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    custody_address = db.Column(db.String(200), nullable=False)
    username = db.Column(db.String(100), nullable=False)
    display_name = db.Column(db.String(100), nullable=False)
    pfp_url = db.Column(db.String(200), nullable=False)
    follower_count = db.Column(db.Integer, nullable=False)
    following_count = db.Column(db.Integer, nullable=False)
    active_status = db.Column(db.String(100), nullable=False)
    power_badge = db.Column(db.Boolean, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now)

    def __repr__(self):
        return f"User {self.username}"
