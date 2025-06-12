import os
import datetime




#if  os.path.exists("novel.txt"):
#    os.rename("novel.txt", "first_draft.txt")
#else:
#    print("File 'novel.txt' does not exist, so it cannot be renamed.") 


print(os.path.getsize("spider.txt"))
print(os.path.getmtime("spider.txt"))



timestamp = os.path.getmtime("spider.txt")
print(datetime.datetime.fromtimestamp(timestamp))

#print(os.path.abspath("spider.txt"))


file= os.path.abspath("spider.txt")
if os.path.isfile(file):
    print(os.path.isfile(file))
    print(os.path.getsize(file))
else:
	print("File not found")

