# Mini Project - Sort via Perceived Brightness

## Goal
I wanted to sort the colors from this image by perceived brightness

![original](https://github.com/FlorianKempenich/PerceivedBrightness/raw/master/paracord.jpg)

## Result
![sorted by perceived brightness](https://github.com/FlorianKempenich/PerceivedBrightness/raw/master/results/sorted_by_perceived_brightness.png)

## Steps

### 1. Map each pixel to its perceived brightness 
This is the only step where [the script](https://github.com/FlorianKempenich/PerceivedBrightness/blob/master/map_to_perceived_brightness.py) is used. We take the original image and, for each pixel, map the color to its perceive brightness. Then we display the value on the red component. 
![mapped to perceived brightness](https://github.com/FlorianKempenich/PerceivedBrightness/raw/master/results/perceived_option_1.png)

### 2. Manually sort by perceived brightness
![mapped to perceived brightness - sorted](https://github.com/FlorianKempenich/PerceivedBrightness/raw/master/results/perceived_option_1_sorted.png)

### 3. Reproduce the order with the real colors - And DONE 😃
![sorted by perceived brightness](https://github.com/FlorianKempenich/PerceivedBrightness/raw/master/results/sorted_by_perceived_brightness.png)