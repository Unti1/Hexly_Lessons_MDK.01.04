from sqlalchemy.orm import Mapped, Session, relationship

from models.profile import Profile
from settings.database import Base, connection, uniq_str_an


class User(Base):
    username: Mapped[uniq_str_an]
    email: Mapped[uniq_str_an]
    password: Mapped[str]
    phone: Mapped[str | None]
    profile: Mapped["Profile"] = relationship(
        "Profile",
        back_populates="user",
        uselist=False,
        lazy="joined",
        cascade="all, delete-orphan",
    )

    posts: Mapped["Post"] = relationship(
        "Post", back_populates="user", cascade="all, delete-orphan"
    )

    comments: Mapped["Comment"] = relationship("Comment", back_populates="user")

    @classmethod
    @connection
    def create(
        cls,
        username: str,
        password: str,
        email: str,
        phone=None,
        session: Session = None,
        **data,
    ):
        new_user = cls(username=username, password=password, email=email, phone=phone)
        session.add(new_user)
        session.flush()

        new_profile = Profile(user_id=new_user.id, **data)
        session.add(new_profile)
        session.commit()
        return new_user
    
    # @classmethod
    # @connection
    # def create_many(
    #     cls,
    #     datas: list[dict],
    #     session: Session = None,
    # ):
    #     new_rows = [cls(**data) for data in datas]
    #     session.add_all(new_rows)
    #     session.commit()
    #     return new_rows
