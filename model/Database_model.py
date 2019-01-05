from flask import  Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from config import  Config



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = Config.DATABASE_URL

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    username = db.Column(db.String(80), unique=True, nullable=False)

    password = db.Column(db.String(30), nullable=False)

    email = db.Column(db.String(120), unique=True, nullable=False)

    stocks = db.relationship('Stock', backref="stock price")


    def __repr__(self):

        return str({
            "id": self.id,
            "username": self.username,
            "password": self.password,
            "email": self.email
        })

    def validate_user(self,email, password):

        status = User.query.filter_by(email=email.lower()).filter_by(password=password).first()

        if status is None:

            return False

        else:

            return True

    def verify_user_is_available(self,email):

        status = User.query.filter_by(email=email.lower()).first()

        if status is None:

            return True

        else:

            return False

    def get_all_user(self):

        return User.query.all()


    def create_user(self,username,email, password):

        new_user = User(username=username, password=password, email=email.lower())

        db.session.add(new_user)

        db.session.commit()


class Stock(db.Model):

    __tablename__ = 'stocks'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    userId = db.Column(db.Integer,db.ForeignKey('users.id'))

    stockId = db.Column(db.String(80), nullable=False)

    buy = db.Column(db.String(30), nullable=False)

    sell = db.Column(db.String(30), nullable=False)

    loss = db.Column(db.String(30), nullable=False)

    emailtrigger = db.Column(db.Boolean, nullable=False)

    def __repr__(self):

        return str({
            "id": self.id,
            "userId": self.userId,
            "stockId": self.stockId,
            "buy": self.buy,
            "sell": self.sell,
            "loss": self.loss
        })

    def create_stock(self,userid,stockId,buy,sell,loss):

        new_stock = Stock(userId = userid, stockId = stockId.upper() , buy = buy , sell = sell , loss = loss,
                          emailtrigger =True)

        db.session.add(new_stock)

        db.session.commit()

    def get_stocklist_by_userid(self,userid):

        return Stock.query.filter_by(userId=userid).all()

    def update_status_for_user_stock(self,userid,stockid,status=False):

        stock_list = Stock.query.filter_by(userId=str(userid)).filter_by(stockId=str(stockid)).first()

        stock_list.emailtrigger = status

        db.session.commit()


    def update_status_to_true(self):

        sql = text("UPDATE stocks set emailtrigger=TRUE WHERE emailtrigger in (SELECT emailtrigger from stocks where emailtrigger=FALSE)")

        db.engine.execute(sql)

        db.session.commit()


