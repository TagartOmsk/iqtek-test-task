from sqlalchemy import (
    BigInteger,
    Column,
    Sequence,
    String,
)

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata
USER_ID_SEQ = Sequence('user_id_seq')


class User(Base):
    __tablename__ = 'users'

    user_id = Column(
        BigInteger,
        USER_ID_SEQ,
        primary_key=True,
        server_default=USER_ID_SEQ.next_value(),  # auto-generation of id from defined sequence
    )
    last_name = Column(String(20))
    first_name = Column(String(20))
    middle_name = Column(String(20))
