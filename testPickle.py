from os.path import expanduser
import os
import pickle

homePath = expanduser("~")
print "homePath=", homePath
filePath = os.path.join(homePath, ".dump.txt")
print "filePath=", filePath
dict={'one':1, 'two':2}
file = open( filePath, 'w')
pickle.dump(dict, file)
file.close()

file = open( filePath, 'r')
dict = pickle.load(file)

print dict

