import cv2
import numpy as np
import glob
import os

def write_mp4():
	img_array = []
	for filename in sorted(glob.glob('/home/radiator2/mp4_images/*.jpg'), key=os.path.getmtime):  # sorted by modification time
	    img = cv2.imread(filename)
	    height, width, layers = img.shape
	    size = (width,height)
	    img_array.append(img)
	    # delete image
	    os.remove(filename) 
	 
	out = cv2.VideoWriter('./videos/o1k.mp4',cv2.VideoWriter_fourcc(*'mp4v'), 20, size)  # filename, codec, fps, framesize
	 
	for i in range(len(img_array)):
	    out.write(img_array[i])
	out.release()

def count_files(dir):
    return len([1 for x in list(os.scandir(dir)) if x.is_file()])	

if __name__ == '__main__':
	n_trigger = 300  # number of jpg files before writing mp4 
	while(True):
		n_files = count_files('/home/radiator2/mp4_images/')
		if n_files >= n_trigger:
			write_mp4()  # blocking operation, and resets number of files 


