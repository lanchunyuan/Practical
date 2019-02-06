import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
results = list()
with open('output_lt1207_mixed.csv','r') as f:
    for line in f:
        results.append(line.split(','))
i = 1
for result in results:
    p_barcode = result[0]
    p_finger = result[1]
    c_barcode = result[2]
    c_finger = result[3]
    try:
        f, (ax1, ax2) = plt.subplots(1, 2, figsize=(16,10))
        p_img = mpimg.imread(f"A/{p_barcode}_{p_finger}.bmp")
        c_img = mpimg.imread(f"R/{c_barcode}_{c_finger}.bmp")
        ax1.imshow(p_img, cmap='gray')
        ax1.set_title(f'Probe {p_barcode}_{p_finger}', fontsize=10)
        ax2.imshow(c_img, cmap='gray')
        ax2.set_title(f'Target {c_barcode}_{c_finger}', fontsize=10)
        f.savefig(open(f"./lt-20181026/tmp_{i:04d}.jpg", mode='wb'))
        i += 1
        plt.close('all')
    except FileNotFoundError:
        pass
