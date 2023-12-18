# import required module
from playsound import playsound
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit



## Image
file_pathi = r"C:\Users\zoom3\Downloads\cattus2.jpg"
file_paths = r"C:\Users\zoom3\Downloads\cattus.wav"

fig=plt.figure("Immagine originale")
img = matplotlib.image.imread(file_pathi)
plt.imshow(img)
def onclick_lm(event):
    playsound(file_paths)
# for playing note.wav file

cid = fig.canvas.mpl_connect('button_press_event', onclick_lm)
plt.show()