# Histogram Equalization
## Overview
Histogram Equalization is a computer image processing technique used to improve contrast in images. It accomplishes this by effectively spreading out the most frequent intensity values, i.e. stretching out the intensity range of the image. This method usually increases the global contrast of images when its usable data is represented by close contrast values. This allows for areas of lower local contrast to gain a higher contrast.
Adaptive Histogram Equalization differs from ordinary histogram equalization in the respect that the adaptive method computes several histograms, each corresponding to a distinct section of the image, and uses them to redistribute the lightness values of the image. It is therefore suitable for improving the local contrast and enhancing the definitions of edges in each region of an image.

- cd into code folder run following command
``` bash
python3 histogram_eq.py --FilePath ../data_files/adaptive_hist_data --visualize True --record False
```
- FilePath -  Video file path. *Default :- '../data_files/adaptive_hist_data'*
- visualize - Shows visualization . *Default :- 'True'*
- record - Records video (histE.mp4 & AHE.mp4) in result folder. *Default :- 'False'*

## Results
### Input
<p align="center">
<img src="result/images/input.png"/>
</p>

### Normal Histogram Equalization
<p align="center">
<img src="result/histE.gif"/>
</p>

### Adaptive Histogram Equalization
<p align="center">
<img src="result/AHE.gif"/>
</p>
