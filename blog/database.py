# code from http://flask-docs-kr.readthedocs.io/ko/latest/patterns/sqlalchemy.html
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///test.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    from blog.models import post
    # 한줄로 하고 싶은데 아쉽다
    # from blog.models import * 가 안돼서 못 함
    Base.metadata.create_all(bind=engine)
