import os
import shutil

src_dir = "download folder location"
#usally C:\User\{username}\Downloads

# file location directory 
# example E:\newfolder


dir1 = "File locations"
dir2 = "File locations"
dir3 = "File locations"
dir4 = "File locations"
dir5 = "File locations"
dir6 = "File locations"
dir7 = "File locations"
dir8 = "File locations"




def moveto(dst):
	filename = os.path.basename(src_dir)
	dest = os.path.join(dst,filename)
	try:
		return lambda src: shutil.move(src, dest)
	except:
		print(e)
    	




action = {
    'pdf': moveto(dir3),
    'docx': moveto(dir3),
    'exe': moveto(dir4),
    'jpg': moveto(dir2),
    'JPG': moveto(dir2),
    'png': moveto(dir2),
    'gif': moveto(dir2),
    'torrent': os.remove,
    'rar': moveto(dir6),
    'mp3': moveto(dir1),
    'mp4': moveto(dir5),
    'wav': moveto(dir1),
    'zip': moveto(dir6),
    'jpeg': moveto(dir2),
    'srt': os.remove,

}

item = 0

for file in os.listdir(src_dir):
    ext = os.path.splitext(file)[1][1:]
    if ext in action:
        action[ext](os.path.join(src_dir, file))
        print('item number',item+1,'is moved to',ext,'folder')
        item = item + 1
