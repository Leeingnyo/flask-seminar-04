from sqlalchemy import Column, Integer, UnicodeText, DateTime
from blog.database import Base

class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    name = Column(UnicodeText, nullable=False)
    created_at = Column(DateTime, nullable=False)
    content = Column(UnicodeText, nullable=False)
    ip = Column(UnicodeText)
    post_id = Column(Integer) # should i use forign key?
    # relationship 과 backref 를 걸어주세요

    def __init__(self, name, created_at, content, ip=None):
        self.name = name
        self.created_at = created_at
        self.content = content
        self.ip = ip

    def __repr__(self):
        return '<Comment %s %s %d>' % (self.created_at.strftime('%Y-%m-%d %H:%M:%S'), self.name, self.post_id)
