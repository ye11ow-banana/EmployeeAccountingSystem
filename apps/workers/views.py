from loguru import logger

from config.settings import logs_config

logger.add(**logs_config)
