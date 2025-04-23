
from sqlalchemy import ForeignKey, select
from sqlalchemy.orm import Mapped, Session, mapped_column, relationship

from settings.database import Base, connection


class Post(Base):
    title: Mapped[str]
    contnet: Mapped[str]

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship("User", back_populates="posts")

    comments: Mapped["Comment"] = relationship("Comment", back_populates="post")
    
    @classmethod
    @connection
    def get_per_user_id(cls, user_id: int, session: Session = None):
        query = select(cls).where(cls.user_id == user_id)
        rows = session.execute(query)
        rows = rows.scalars().all()
        return rows
        
