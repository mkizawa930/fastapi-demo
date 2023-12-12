from sqlalchemy import Column, String, Integer, Boolean

from app.database import Base


class Task(Base):
    __tablename__ = 'task'
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    is_done = Column(Boolean, nullable=False)
    
