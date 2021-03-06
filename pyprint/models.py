from datetime import date
from hashlib import md5

from sqlalchemy import Column, Table
from sqlalchemy import Text, String, Date, Integer, ForeignKey, Enum
from sqlalchemy.orm import relationship

from database import Base, engine
from constants import POST_ENUMS, POST



posts_tags = Table(
    'posts_tags', Base.metadata,
    Column('post_id', Integer, ForeignKey('posts.id')),
    Column('tag_id', Integer, ForeignKey('tags.id')),
)


class Tag(Base):
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True, autoincrement=True)
    slug = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return '<Tag: %s>' % self.slug


class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(200), unique=True, nullable=False)
    tags = relationship('Tag', secondary=posts_tags, backref='posts')
    created_time = Column(Date, default=date.today())
    content = Column(Text)
    type = Column(Enum(*POST_ENUMS), default=POST)
    password = Column(String(10), nullable=True)

    def __repr__(self):
        return '<Post: %s>' % self.title


class Link(Base):
    __tablename__ = 'links'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    url = Column(String(100))

    def __repr__(self):
        return '<Link: %s>' % self.url


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(20))
    password = Column(String(32))

    def check(self, password):
        return self.password == md5(password).hexdigest()

    def __repr__(self):
        return '<User: %s>' % self.username


metadata = Base.metadata

if __name__ == "__main__":
    metadata.create_all(engine)
