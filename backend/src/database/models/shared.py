from typing import Optional

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.database import Base

from sqlalchemy.orm import Mapped, mapped_column
from src.database import Base


class Shop(Base):
    __tablename__ = "shops"

    name: Mapped[str] = mapped_column()
    cars: Mapped[list["Car"]] = relationship(
        back_populates="shop", cascade="all, delete-orphan"
    )
    users: Mapped[list["User"]] = relationship(
        "UserShop", back_populates="shop"
    )


class TransmissionType(Base):
    __tablename__ = "transmission_types"

    name: Mapped[str] = mapped_column()
    cars: Mapped[list["Car"]] = relationship(
        back_populates="transmission_type", cascade="all, delete-orphan"
    )


class CarType(Base):
    __tablename__ = "car_types"

    name: Mapped[str] = mapped_column()
    cars: Mapped[list["Car"]] = relationship(
        back_populates="auto_type",
        cascade="all, delete-orphan",
    )
    buyers: Mapped[list["Buyer"]] = relationship(
        back_populates="auto_type",
        cascade="all, delete-orphan",
    )


class CarsModel(Base):
    __tablename__ = "cars_models"

    name: Mapped[str] = mapped_column()
    cars: Mapped[list["Car"]] = relationship(
        back_populates="model",
        cascade="all, delete-orphan",
    )
    buyers: Mapped[list["Buyer"]] = relationship(
        back_populates="model",
        cascade="all, delete-orphan",
    )


class CompanyName(Base):
    __tablename__ = "company_names"

    name: Mapped[str] = mapped_column()
    cars: Mapped[list["Car"]] = relationship(
        back_populates="company",
        cascade="all, delete-orphan",
    )
    buyers: Mapped[list["Buyer"]] = relationship(
        back_populates="company",
        cascade="all, delete-orphan",
    )


class BuyerUser(Base):
    __tablename__ = "buyer_users"

    buyer_id: Mapped[int] = mapped_column(ForeignKey("buyers.id"), primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), primary_key=True)

    buyer = relationship("Buyer", back_populates="user_link")
    user = relationship("User", back_populates="buyer_link")


class Buyer(Base):
    __tablename__ = "buyers"

    company_id: Mapped[int] = mapped_column(
        ForeignKey("company_names.id", ondelete="CASCADE"),
    )

    model_id: Mapped[int] = mapped_column(
        ForeignKey("cars_models.id", ondelete="CASCADE"),
    )

    auto_type_id: Mapped[int] = mapped_column(
        ForeignKey("car_types.id", ondelete="SET NULL"), nullable=True
    )

    cost: Mapped[int] = mapped_column()
    fio: Mapped[str] = mapped_column()
    latitude: Mapped[float] = mapped_column()
    longitude: Mapped[float] = mapped_column()
    year: Mapped[int] = mapped_column()

    company: Mapped["CompanyName"] = relationship(
        back_populates="buyers",
        lazy="joined",
    )
    model: Mapped["CarsModel"] = relationship(
        back_populates="buyers",
        lazy="joined",
    )
    auto_type: Mapped[Optional["CarType"]] = relationship(
        back_populates="buyers",
        lazy="joined",
    )
    user_link: Mapped["BuyerUser"] = relationship("BuyerUser", back_populates="buyer")


class Car(Base):
    __tablename__ = "cars"

    company_id: Mapped[int] = mapped_column(
        ForeignKey("company_names.id", ondelete="CASCADE"),
    )

    model_id: Mapped[int] = mapped_column(
        ForeignKey("cars_models.id", ondelete="CASCADE"),
    )

    transmission_type_id: Mapped[int] = mapped_column(
        ForeignKey("transmission_types.id", ondelete="SET NULL"), nullable=True
    )

    auto_type_id: Mapped[int] = mapped_column(
        ForeignKey("car_types.id", ondelete="SET NULL"), nullable=True
    )

    shop_id: Mapped[int] = mapped_column(
        ForeignKey("shops.id", ondelete="CASCADE"), nullable=False
    )

    year: Mapped[int] = mapped_column()
    engine_power: Mapped[int] = mapped_column()
    features: Mapped[str] = mapped_column()
    cost: Mapped[int] = mapped_column()
    mileage: Mapped[int] = mapped_column()

    company: Mapped["CompanyName"] = relationship(
        back_populates="cars",
        lazy="joined",
    )
    model: Mapped["CarsModel"] = relationship(
        back_populates="cars",
        lazy="joined",
    )
    transmission_type: Mapped[Optional["TransmissionType"]] = relationship(
        back_populates="cars",
        lazy="joined",
    )
    auto_type: Mapped[Optional["CarType"]] = relationship(
        back_populates="cars",
        lazy="joined",
    )
    shop: Mapped["Shop"] = relationship(
        back_populates="cars",
        lazy="joined",
    )


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    phone_number: Mapped[str] = mapped_column(unique=True)

    roles: Mapped[list["UserRole"]] = relationship(back_populates="user")
    shops: Mapped["UserShop"] = relationship("UserShop", back_populates="user")
    buyer_link = relationship("BuyerUser", back_populates="user")


class Role(Base):
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)

    users: Mapped[list["UserRole"]] = relationship(back_populates="role")


class UserRole(Base):
    __tablename__ = "user_roles"

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), primary_key=True)
    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id"), primary_key=True)

    user: Mapped["User"] = relationship("User", back_populates="roles", foreign_keys=[user_id])
    role: Mapped["Role"] = relationship("Role", back_populates="users", foreign_keys=[role_id])


class UserShop(Base):
    __tablename__ = "user_shops"

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), primary_key=True)
    shop_id: Mapped[int] = mapped_column(ForeignKey("shops.id"), primary_key=True)

    # Дополнительные поля (необязательно)
    user = relationship("User", back_populates="shops")
    shop = relationship("Shop", back_populates="users")
