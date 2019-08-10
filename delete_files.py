import os

if os.path.exists('file/test.py') :
	os.remove('file/test.py')
	print('The file has been removed!')
else :
	print('The file doesnt exist!')

if os.path.exists('new/') :
	os.rmdir('new')
	print('Directory has been removed!')
else :
	print('Derectory doesnt exist!')