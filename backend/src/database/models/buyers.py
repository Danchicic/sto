from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


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
