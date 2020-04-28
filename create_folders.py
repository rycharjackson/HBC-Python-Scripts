import os

src = os.listdir(os.getcwd())


# Cycle through list of files in folder
# Create a folder for every type of file extension
# If folder exists. Don't create it
# Prints Lists of New Folders created


for items in src:
	  ext = items.split(".")[-1:]
	  try: 
	    os.makedirs(os.path.join(os.getcwd(), ext))
	  
	  	
	  
	  		
