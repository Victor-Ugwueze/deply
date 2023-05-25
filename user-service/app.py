from flask import Flask
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

# Connect to PostgreSQL
engine = create_engine('postgresql://postgres:password@db:5432/postgres')
Session = sessionmaker(bind=engine)
session = Session()

# Create a model
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)

Base.metadata.create_all(bind=engine)

@app.route('/')
def hello():
    # Add a user to the database
    user = User(username='John')
    session.add(user)
    session.commit()

    # Retrieve the total number of users from PostgreSQL
    total_users = session.query(User).count()

    return f'Total Users: {total_users}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
