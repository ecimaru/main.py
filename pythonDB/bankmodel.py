from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base, db_session

class Customer(Base):
    __tablename__ = 'customers'
    c_id = Column(String(20), primary_key=True)
    name = Column(String(50))
    account_num = Column(String(20), unique=True)
    total_amount = Column(Integer)
    rat = Column(String(20))

    def __init__(self, c_id, name):
        self.c_id = c_id
        self.name = name
        self.account_num = 0
        self.total_amount = 0
        self.rat = 'normal'

    def __repr__(self):
        return '<{}, {}, {}, {}, {}>'.format(self.c_id, self.name, self.account_num, self.total_amount, self.rat)



class Accounts(Base):
    __tablename__ = 'accounts'
    a_id = Column(String(20), primary_key=True)
    c_id = Column(String(20), unique = True,ForeignKey(Customer.c_id))
    amount = Column(Integer)
    
    def __init__(self,a_id,c_id):
        self.a_id = a_id
        self.c_id = c_id
        self.amount = 0

    def __repr__(self):
        return '<{}, {}, {}>'.format(self.a_id, self.amount, self.c_id)
