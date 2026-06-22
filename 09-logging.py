import logging
#By default on ly Warning, critical and error gets printed
# below lines need to be added to print all log levels
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s- %(message)s', datefmt='%Y-%m-%d %H:%m:%s')

logging.info("This is info message")
logging.debug("This is debug message")
logging.warning("This is warning message")
logging.critical("This is critical message")
logging.error("This is error message")
# 2026-06-22 19:06:1782136332 - root - INFO- This is info message
# 2026-06-22 19:06:1782136332 - root - DEBUG- This is debug message
# 2026-06-22 19:06:1782136332 - root - WARNING- This is warning message
# 2026-06-22 19:06:1782136332 - root - CRITICAL- This is critical message
# 2026-06-22 19:06:1782136332 - root - ERROR- This is error message

## Create custom logger
# create file helper.py
import logging
logger = logging.getLogger(__name__) # __name__ is filename in this case helper.py
logger.info("Hello..this is info from helper logging")

# in main file main.py call this helper function
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s- %(message)s', datefmt='%Y-%m-%d %H:%m:%s')
import helper
#output:
# 2026-06-22 19:06:1782136643 - helper - INFO- Hello..this is info from helper logging