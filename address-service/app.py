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

class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    address = Column(String)

Base.metadata.create_all(bind=engine)

@app.route('/')
def hello():

    address = Address(user_id=1, address='1 John street')
    session.add(address)
    session.commit()

    # Retrieve the total number of user addresses from PostgreSQL
    total_addresses= session.query(Address).count()

    return f'Total addresses: {total_addresses}'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000, debug=True)
