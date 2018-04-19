import urllib.request
import shutil
import tarfile
import os


# This function recursivly makes directories.
def makedir(directory):
  directory = "".join(str(x) for x in directory)
  try:
    os.stat(directory)
  except:
    try:
      os.mkdir(directory)
    except:
      subDir = directory.split('/')
      while (subDir[-1] == ''):
          subdir = subdir[:-1]
      newDir = ""
      for x in range(len(subDir)-2):
        newDir += (subDir[x])
        newDir += ('/')
      print ("Attempting to pass... " + str(newDir))
      directoryFixer(newDir)
      os.mkdir(directory)

# 
def main(save_path_data='data',save_path_model='examples/hed'):
	makedir(save_path_data + '/')
	makedir(save_path_model + '/')
	print('working')
	# Setup our download paths
	data_file_link  = 'http://vcl.ucsd.edu/hed/HED-BSDS.tar'
	data_file_path  = 'HED-BSDS.tar'

	model_file_link = 'http://vcl.ucsd.edu/hed/5stage-vgg.caffemodel'
	model_file_path = save_path_model + '/5stage-vgg.caffemodel'
	# download the files
	# THE TAR BOY
	with urllib.request.urlopen(data_file_link) as response, open(data_file_path, 'wb') as out_file:
		shutil.copyfileobj(response, out_file)
	# THE CAFFEMODEL BOY
	with urllib.request.urlopen(model_file_link) as response, open(model_file_path, 'wb') as out_file:
		shutil.copyfileobj(response, out_file)
	# with the tar file save it locally
	# then extract it to the dest folder at data/

	# open the tar
	tar = tarfile.open(data_file_path)
	tar.extractall(save_path_data + '/')
	tar.close()

	# done

if __name__ == '__main__':
	main()
