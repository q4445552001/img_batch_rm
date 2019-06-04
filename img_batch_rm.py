import os

path = '/var/camera/image/'
list = os.popen('ls ' + path).read().split('\n')

for dir in list :
	if dir :
		os.chdir(path + dir)
		if dir != 'gamerch':
			print 'Check ' + path + dir
			#print dir
			#print os.getcwd()
			os.system('ls | grep -v ' + os.popen('ls | tail -n 1').read().strip() + '| xargs rm')

path = '/var/camera/image/pixiv/'
list = os.popen('ls ' + path).read().split('\n')

for dir in list :
	if dir :
		os.chdir(path + dir)
		print 'Check ' + path + dir
		os.system('ls | grep -v ' + os.popen('ls | tail -n 1').read().strip() + '| xargs rm')