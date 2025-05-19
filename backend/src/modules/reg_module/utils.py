import logging
import random

from redis.asyncio import Redis

from src.core.config import auth_config

logger = logging.getLogger(__name__)


def create_verification_code() -> int:
    """
    simple verification code creator
    :return:
    """
    return random.randint(100_000, 999_999)


async def send_verification_code(phone_number: str, redis: Redis) -> int:
    """
    imitate smtp sender code
    :param phone_number:
    :param redis:
    :return:
    """
    code_to_user = create_verification_code()
    # imitate sms
    try:
        await redis.setex(
            name=phone_number,
            time=auth_config.verification_code_time_expiration,
            value=code_to_user,
        )
        logger.info(
            f"Successfully sent verification code {code_to_user} to {phone_number}"
        )
        return code_to_user
    except Exception:
        logger.exception("Failed to send verification code")
