import os

def file_name_listdir(file_dir):
	for files in os.listdir(file_dir):  # 不仅仅是文件，当前目录下的文件夹也会被认为遍历到
		if os.path.isdir(files):
		print ("files",files)
	elif os.path.isfile(files):
    	print ("files", files)

file_name_listdir("./")
