import os
import glob
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

results = []
location = '/mnt/nfs/share/upload/'
p_paths = {}
c_paths = {}
i = 1
with open('output_lt1207_mixed.csv') as f_obj:
	for line in f_obj:
		line = line.strip('\n')
		results.append(line.split(','))
for result in results:
	p_barcode = result[0]
	p_finger = result[1]
	c_barcode = result[2]
	c_finger = result[3]
	p_paths[f'{p_barcode}-{p_finger}'] = \
	glob.glob(f'{location}p_barcode/**/*-{p_finger}_{p_barcode}.bmp', \
	recursive=True)

	c_paths[f'{c_barcode}-{c_finger}'] = \
	glob.glob(f'{location}c_barcode/**/*-{c_finger}_{c_barcode}.bmp', \
	recursive=True)
	try:	
		f, (ax1, ax2) = plt.subplots(1, 2, figsize=(16,10))
		try:
			p_img = mpimg.imread(p_paths[f'{p_barcode}-{p_finger}'][0])
			c_img = mpimg.imread(c_paths[f'{c_barcode}-{c_finger}'][0])
			ax1.imshow(p_img, cmap='gray')
			ax1.set_title(f'Probe {p_barcode}_{p_finger}', fontsize=10)
			ax2.imshow(c_img, cmap='gray')
			ax2.set_title(f'Target {c_barcode}_{c_finger}', fontsize=10)
			f.savefig(open(f'./matched/tmp_{i:04d}.jpg', mode='wb'))
			i += 1
			plt.close('all')
		except IndexError:
			pass
	except FileNotFoundError:
		with open('error.log','a') as f_obj:
			f_obj.write(f"{p_barcode},{p_finger},{c_barcode},{c_finger}\n")
