from sqlalchemy import Column, Integer, UnicodeText, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref
from blog.database import Base

class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    name = Column(UnicodeText, nullable=False)
    created_at = Column(DateTime, nullable=False)
    content = Column(UnicodeText, nullable=False)
    ip = Column(UnicodeText)
    post_id = Column(Integer, ForeignKey('posts.id'), nullable=False) # should i use foreign key?
    # you can use relationship without foreign key constraint
    # see http://stackoverflow.com/questions/37806625/sqlalchemy-create-relations-but-without-foreign-key-constraint-in-db

    post = relationship('Post', backref=backref('comments', order_by=id))
    # 'Post'는 Comment 처럼 Mapper 이름
    # http://docs.sqlalchemy.org/en/latest/orm/relationship_api.html#sqlalchemy.orm.relationship
    # http://docs.sqlalchemy.org/en/latest/orm/relationship_api.html#sqlalchemy.orm.backref

    def __init__(self, name, created_at, content, post_id, ip=None):
        self.name = name
        self.created_at = created_at
        self.content = content
        self.post_id = post_id
        self.ip = ip

    def __repr__(self):
        return '<Comment %s %s %d>' % (self.created_at.strftime('%Y-%m-%d %H:%M:%S'), self.name, self.post_id)
