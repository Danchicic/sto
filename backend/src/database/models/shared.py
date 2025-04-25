from typing import Optional

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base


class TransmissionType(Base):
    __tablename__ = "transmission_types"
    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column()
    cars: Mapped[list["Car"]] = relationship(
        back_populates="transmission_type", cascade="all, delete-orphan"
    )


class CarType(Base):
    __tablename__ = "car_types"
    id: Mapped[int] = mapped_column(primary_key=True)

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
    id: Mapped[int] = mapped_column(primary_key=True)

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
    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column()
    cars: Mapped[list["Car"]] = relationship(
        back_populates="company",
        cascade="all, delete-orphan",
    )
    buyers: Mapped[list["Buyer"]] = relationship(
        back_populates="company",
        cascade="all, delete-orphan",
    )


class Buyer(Base):
    __tablename__ = "buyers"
    id: Mapped[int] = mapped_column(primary_key=True)

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


class Car(Base):
    __tablename__ = "cars"
    id: Mapped[int] = mapped_column(primary_key=True)

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
