import logging

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(
	filename = "logging_demo.log",
	level = logging.DEBUG,
	format = LOG_FORMAT,
	filemode = "w")
logger = logging.getLogger()

logger.debug("Debug level message")
logger.info("Info level message")
logger.warning("Warning level message")
logger.error("Error level message")
logger.critical("Critical level message")

print(logger.level)
