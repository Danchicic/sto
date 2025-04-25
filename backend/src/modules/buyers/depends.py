from typing import Optional

from . import schemas


def get_buyers_conditionals(
    company_id: Optional[int] = None,
    model_id: Optional[int] = None,
    auto_type_id: Optional[int] = None,
    cost_max: Optional[int] = None,
    cost_min: Optional[int] = None,
    year: Optional[int] = None,
) -> schemas.BuyersConditionals:
    return schemas.BuyersConditionals(**locals())
