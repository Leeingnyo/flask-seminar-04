from sqlalchemy import Column, Integer, UnicodeText, DateTime
# to see more type, http://docs.sqlalchemy.org/en/latest/core/type_basics.html
from blog.database import Base

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(UnicodeText, nullable=False)
    created_at = Column(DateTime, nullable=False)
    content = Column(UnicodeText, nullable=False)

    def __init__(self, title, created_at, content):
        self.title = title
        self.created_at = created_at
        self.content = content

    def __repr__(self):
        return '<Post %s %s>' % (self.created_at.strftime('%Y-%m-%d %H:%M:%S'), self.title)
