from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped

from src.database import Base


class TransmissionType(Base):
    __tablename__ = "transmission_types"
    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column()


class CarType(Base):
    __tablename__ = "car_types"
    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column()


class CarsModel(Base):
    __tablename__ = "cars_models"
    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column()


class CompanyName(Base):
    __tablename__ = "company_names"
    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column()


class Car(Base):
    __tablename__ = "cars"
    id: Mapped[int] = mapped_column(primary_key=True)

    company_id: Mapped[int] = mapped_column(
        ForeignKey(
            "company_names.id",
            ondelete='CASCADE'
        ),
    )

    model_id: Mapped[int] = mapped_column(
        ForeignKey(
            "cars_models.id",
            ondelete='CASCADE'
        ),
    )

    transmission_type_id: Mapped[int] = mapped_column(
        ForeignKey(
            "transmission_types.id",
            ondelete='SET NULL'
        ),
        nullable=True
    )

    auto_type_id: Mapped[int] = mapped_column(
        ForeignKey(
            "car_types.id", ondelete='SET NULL'
        ),
        nullable=True
    )

    year: Mapped[int] = mapped_column()
    engine_power: Mapped[int] = mapped_column()
    features: Mapped[str] = mapped_column()
    cost: Mapped[int] = mapped_column()
    mileage: Mapped[int] = mapped_column()
