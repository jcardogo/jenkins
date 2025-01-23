import logging

#Set the minimum logging level to INFO,
logging.basicConfig(level=logging.INFO)
#Get a logger object
log = logging.getLogger(__name__) #adds your Python module name to the logger’s output

#Start the log file
log.info("Hola Mundo")




#Setting up the logger and StreamHandler
#Creating a logger
stream_logger = logging.getLogger('stream_logger')
stream_logger.setLevel(logging.DEBUG) # Set logger to capture all messages from DEBUG level and above
#Ensure no previous handlerd are attached
stream_logger.handlers = []
#Creating a StreamHandler
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO) #Set handler to display only messages from INFO level and above
#Adding handler to logger
stream_logger.addHandler(stream_handler)
#logging messages at different levels
stream_logger.debug("This is a DEBUG message for stream_logger.")
stream_logger.info("This is an INFO message for stream_logger.")
stream_logger.warning("This is a WARNING message for stream_logger.")
stream_logger.error("This is an ERROR message for stream_logger.")
stream_logger.critical("This is a CRITICAL message for stream_logger.")

"""
Different types of logging handlers
Besides StreamHandler, there are also many other handlers: 

FileHandler

NullHandler

WatchedFileHandler

BaseRotatingHandler

RotatingFileHandler

TimedRotatingFileHandler

SocketHandler

DatagramHandler

SysLogHandler

NTEventLogHandler

SMTPHandler

MemoryHandler

HTTPHandler

QueueHandler

QueueListener

For more information about logging handlers, https://docs.python.org/3/library/logging.handlers.html 
"""