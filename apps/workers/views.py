from loguru import logger

from django.conf import settings

logger.add(**settings.LOGS_CONFIG)
