#Set the minimum logging level to INFO,
logging.basicConfig(level=logging.info)

#Get a logger object
log = logging.getLogger(__name__)

#Start the loggign file
log.info("Hola Mundo!")

#Exception script example
try:
  #Try to append to a file is normally not writable
  #for anyone other than root
  f = open("/etc/hosts", "w+")
except IOError as ex:
  #The variable "ex" will hold details about the error that occurred
  print("Error appending to file: " + str(ex))
else:
  #If there was not exception close the file.
  f.close()
  
