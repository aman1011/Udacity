import os
import string
def rename_files():
	
	# get the files
	file_list = os.listdir(r"/Users/gaman/Downloads/prank")
	print(file_list)

	saved_path = os.getcwd()
	print(saved_path)

	os.chdir(r"/Users/gaman/Downloads/prank")

	# rename the file in the loop.
	for file_name in file_list:

		# rename the file list
		print("Changing the filename from " + file_name + " to " + file_name.translate(None, "0123456789"))
		os.rename(file_name, file_name.translate(None, "0123456789"))

rename_files()