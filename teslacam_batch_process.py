# This code was created to work with TeslaUSB https://github.com/marcone/teslausb
# When this code was created in 2019, all dashcam footage would be copied, even if there was no motion.
# The intent of this code was to trim motion events so that only the relevant cameras with motion data were shown.
# This would clean up the file system from a bunch of segmented videos to a consolodated video with only relevant motion data.
# This code has not been used since 2019. As it does delete folders, please be careful when running and ensure your folders are set right. 
# I do not take responsibility for any unwanted data loss.

import os
# Set this to True if you want to clean up after.
delete = False
basepath = "/path/to/TeslaCam/"
processedpath = '/path/to/TeslaCam/processed/'
dir=os.listdir(basepath)
# The TeslaCam folder has a variety of folders, go through them
for fold in dir:
  # We only care about folders that start with a data (thus a digit)
	if fold[0].isdigit():
		folder = fold + "/"
		dir2=os.listdir(basepath+folder)
		try: 
      # Make a proceessed folder if it doesnt exist
			os.makedirs(processedpath + folder)
		except:
			pass
		front = []
		left = []
		right = []
		other = []
		for clip in dir2:
			if 'front' in clip:
				front+=[clip]
			elif 'left' in clip:
				left+=[clip]
			elif 'right' in clip:
				right+=[clip]
			else:
				other+=[clip]
    # If the clips aren't empty, add them to our processed video as they contain information we care about.
		if front != []:
			cmd = os.popen('dvr-scan -i ' + basepath +folder+(' -i '+basepath+folder).join(front) +' -o ' + processedpath + folder+'front.mp4').read()
		if left != []:
			cmd = os.popen('dvr-scan -i ' + basepath +folder+(' -i '+basepath+folder).join(left) +' -o ' + processedpath + folder+'left.mp4').read()
		if right != []:
			cmd = os.popen('dvr-scan -i ' + basepath +folder+(' -i '+basepath+folder).join(right) +' -o ' + processedpath + folder+'right.mp4').read()
		if other != []:
			cmd = os.popen('dvr-scan -i ' + basepath +folder+(' -i '+basepath+folder).join(other) +' -o ' + processedpath + folder+'other.mp4').read()
		# Clean up empty folders and clips
    if(delete):
			for clip in dir2:
				os.remove(basepath +folder+ clip)
				print('removed' +basepath +folder+ clip)
		os.rmdir(basepath+folder)
