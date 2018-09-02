# Sense_stripes
Show temp, humidity and pressure with three stripes on sense hat LED matrix.

Red color is for temp, green for atmosferic pressure and blue is for humidity.

Boundaries (min, max) are 20 and 90 for temperature and humidity and 960 and 1030 for atmosferic pressure. If the value is below this treshold the bar will be 1 LED high but with weaker color as usual. If the value is above this treshold, the bar will be of full height and the color will be brighter. If the value is between, each LED represents 10 points increase from min value starting at min value.

Example: red bar is 5 LEDs high, green bar is 2 LEDs high and blue bar is 8 LEDs high.
Temp reading is 60 degree celsius (first LED is 20 + 4 other LEDs 10 points each means 20 + (4 * 10) = 60).
Pressure is 970 hPa (first LED is 960 + 1 other LED with 10 points means 960 + (1 * 10) = 970).
Humidity is above 90 procent (all LEDs are glowing that means the humidity is outside set boundaries).

The idea was inserted to a file from https://projects.raspberrypi.org/en/projects/getting-started-with-the-sense-hat/8 where is a nice tutorial on reading all three values at once. All I did was the bars ;)
