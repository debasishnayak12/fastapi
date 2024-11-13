from sqlalchemy import Column, Integer, String ,TIMESTAMP
from database import Base
from datetime import datetime

  
class User(Base):
    __tablename__="user_api"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    mobile = Column(String,index = True)
    email = Column(String(255), unique=True, index=True)
    image = Column(String(255),index = True)
    status = Column(Integer,index = True)
    insert_time = Column(TIMESTAMP,server_default ="CURRENT_TIMESTAMP" )
    # update_time = Column(DateTime,index=True,default = None)
    

