import os
import shutil

dir1 = "E:/songs"
dir2 = "E:/Photos/Misc"
dir3 = "E:/Book and documents"
dir4 = "E:/Softwares"
dir5 = "E:/Photos/Videos/Misc"
dir6 = "E:/Compressed"

def moveto(dst):
    return lambda src: shutil.move(src, dst)

action = {
    'pdf': moveto(dir3),
    'docx': moveto(dir3),
    'exe': moveto(dir4),
    'jpg': moveto(dir2),
    'png': moveto(dir2),
    'gif': moveto(dir2),
    'torrent': os.remove,
    'rar': moveto(dir6),
    'mp3': moveto(dir1),
    'mp4': moveto(dir5),
    'wav': moveto(dir1),
    'zip': moveto(dir6),
    'jpeg': moveto(dir2),

}
item = 0
src_dir = 'C:/Users/Soumik/Downloads'
for file in os.listdir(src_dir):
    ext = os.path.splitext(file)[1][1:]
    if ext in action:
        action[ext](os.path.join(src_dir, file))
        print('item number',item+1,'is moved to',ext,'folder')
        item = item + 1