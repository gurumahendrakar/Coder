import logging
formating = (" %(asctime)s -- %(message)s ")
formating2 = (" %(asctime)s %(levelname)s %(name)s %(message)s ")
logging.basicConfig(level=logging.DEBUG, filename='texting.txt',filemode='a',format=formating)
# :-> logging.disable() # Bebugging work nahi karega stop hojaga

# level = logging.ERROR :> Ye Sirf ( logging.error aur  logging.critical) Pe work karega sirf
#level = logging.INFO :-> Ye Sirf (logging.info aur logging.warning) Pe work karega sirf

name = "Guru"

if name!="Guru":
    print("Tum Guru Nahi Ho App Ye Function Conducte Nahi Kar Sakte")

else:
    logging.warning("Guru Al's Right Brother ")
    logging.error("This Is Now Error Brother")
    print("Welcome To Function Guru ")


# Best Method Create Loggging 
from logging import *
logging = logging.getLogger(__name__) # app jo file pe run karoge ye wahi return karega 

logging.setLevel(level=DEBUG)
file = FileHandler('texting.txt')
format = " %(asctime)s %(levelname)s %(name)s %(message)s "
formater = Formatter(format)
file.setFormatter(formater)
logging.addHandler(file)

logging.warning(" Hey i'm warning ")