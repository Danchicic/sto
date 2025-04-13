from sqlalchemy.orm import mapped_column, Mapped

from . import Base


class Shop(Base):
    __tablename__ = "shops"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()


class Test(Base):
    __tablename__ = "table"

    id: Mapped[int] = mapped_column(primary_key=True)
