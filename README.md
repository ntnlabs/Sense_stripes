# Sense_stripes
Show temp, humidity and pressure with three stripes on sense hat LED matrix and send values to a syslog server for better post-measurement evalueation.

Red color is for temp, green for atmosferic pressure and blue is for humidity.

Boundaries (min, max) are 20 and 90 for temperature and humidity and 960 and 1030 for atmosferic pressure. If the value is below this treshold the bar will be 1 LED high but with weaker color as usual. If the value is above this treshold, the bar will be of full height and the color will be brighter. If the value is between, each LED represents 10 points increase from min value starting at min value.

Example: red bar is 5 LEDs high, green bar is 2 LEDs high and blue bar is 8 LEDs high.
Temp reading is 60 degree celsius (first LED is 20 + 4 other LEDs 10 points each means 20 + (4 * 10) = 60).
Pressure is 970 hPa (first LED is 960 + 1 other LED with 10 points means 960 + (1 * 10) = 970).
Humidity is above 90 procent (all LEDs are glowing that means the humidity is outside set boundaries).

The idea was inserted to a file from https://projects.raspberrypi.org/en/projects/getting-started-with-the-sense-hat/8 where is a nice tutorial on reading all three values at once. All I did was the bars ;)

Syslog was added as a small modification of this code: https://community.microfocus.com/t5/ArcSight-User-Discussions/Python-Script-to-Send-Data-as-Syslog/td-p/1598292 (there is a mistake in that code, not important for my scenario).

I am using free version of Splunk and this is the code I am using to show the graphs:

For just one value: host="host.host.host" "temperature/humidity/pressure" | timechart values(temperature) span=1m

For all three values in one graph: host="host.host.host" "temperature/humidity/pressure" | timechart values(temperature) as temperature values(humidity) as humidity values(pressure) as pressure span=1m

I used the "extract new fields" function to extract the fields and have them named like this.

PS: You need to change x.x.x.x for IP of the syslog server in code.
