import enum
from sqlalchemy.types import Enum
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, Integer, String, ForeignKey, UnicodeText, Boolean, BigInteger
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Role(enum.Enum):
    DRAGON = 1
    TRAINER = 2
    ADMIN = 3


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    chat_id = Column(BigInteger, unique=True)
    tele_handle = Column(String(25), nullable=False, unique=True)
    tele_name = Column(String(100))
    dragon_id = Column(Integer, ForeignKey('users.id'), index=True)
    # ref: https://github.com/sqlalchemy/sqlalchemy/issues/1403#issue-384617192
    registered = Column(Boolean, nullable=False,
                        default=False, server_default="0")
    is_admin = Column(Boolean, nullable=False,
                        default=False, server_default="0")
    dragon = relationship('User', remote_side=[id], backref=backref(
        'trainer', uselist=False), uselist=False, post_update=True)
    details = relationship('UserDetails', uselist=False, back_populates='user', lazy='joined')


class UserDetails(Base):
    __tablename__ = 'user_details'

    user_id = Column(Integer, ForeignKey(User.id),
                     primary_key=True, nullable=False)
    name = Column(String(100))
    likes = Column(UnicodeText)
    dislikes = Column(UnicodeText)
    room_number = Column(String(7))
    requests = Column(UnicodeText)
    level = Column(Integer)
    user = relationship('User', back_populates='details')


class MessageMapping(Base):
    __tablename__ = 'message_mapping'

    sender_message_id = Column(
        BigInteger, primary_key=True, autoincrement=False, nullable=False)
    sender_chat_id = Column(BigInteger, primary_key=True,
                            autoincrement=False, nullable=False)
    receiver_message_id = Column(BigInteger, primary_key=True, nullable=False)
    receiver_chat_id = Column(BigInteger, primary_key=True, nullable=False)
    receiver_caption_message_id = Column(BigInteger, nullable=True)
    deleted = Column(Boolean, nullable=False,
                     default=False, server_default="0")
    message_from = Column(Enum(Role), nullable=False)
