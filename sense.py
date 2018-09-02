from sense_hat import SenseHat
from time import sleep

# setup the enviroment
sense = SenseHat()
sense.set_rotation(0)
sense.low_light = True
sense.clear()

# define some colors
b = (0,0,0)
r1 = (255,0,0)
r2 = (192,0,0)
r3 = (129,0,0)
g1 = (0,255,0)
g2 = (0,192,0)
g3 = (0,129,0)
b1 = (0,0,255)
b2 = (0,0,192)
b3 = (0,0,129)

# LED startup
# TODO: add startup colorful effect
line0 = [b,b,b,b,b,b,b,b]
line1 = [r2,r2,r2,r2,r2,r2,r2,r2]
line2 = [g2,g2,g2,g2,g2,g2,g2,g2]
line3 = [b2,b2,b2,b2,b2,b2,b2,b2]
image = [line1+line1+line0+line2+line2+line0+line3+line3]

sense.set_pixels(image[0])
sleep(1)
sense.clear()

while True:
  # Take integer readings from all three sensors
  t = int(sense.get_temperature())
  p = int(sense.get_pressure())
  h = int(sense.get_humidity())

  # if temp is below 20, show weak red bar of minimal height (1 led)
  # if temp is abowe 90, show bright red bar of full height (8 leds)
  # if temp is between, show average red bar of height acording to the temp. 1 LED means 10 degrees celsius starting from 20 degrees celsius
  # same for the humidity with blue color
  # same for the pressure with green color and limiting values of 960 and 1030 hPa
  if t < 20:
   line1 = [b,b,b,b,b,b,b,r3]
  elif t > 90:
   line1 = [r1,r1,r1,r1,r1,r1,r1,r1]
  else:
   line1 = [r2]*int((t-10)/10)
   if len(line1) < 8:
    line1 = line0[0:8-len(line1)]+line1

  if p < 960:
   line2 = [b,b,b,b,b,b,b,g3]
  elif p > 1030:
   line2 = [g1,g1,g1,g1,g1,g1,g1,g1]
  else:
   line2 = [g2]*int((p-960)/10)
   if len(line2) < 8:
    line2 = line0[0:8-len(line2)]+line2
    
  if h < 20:
   line3 = [b,b,b,b,b,b,b,b3]
  elif h > 90:
   line3 = [b1,b1,b1,b1,b1,b1,b1,b1]
  else:
   line3 = [b2]*int((h-10)/10)
   if len(line3) < 8:
    line3 = line0[0:8-len(line3)]+line3
    
  # just to see if it's doing what it is supposed to do
  # Create the message
  # str() converts the value to a string so it can be concatenated
  message = "Temperature: " + str(t) + " Pressure: " + str(p) + " Humidity: " + str(h)

  print(message)
  image = [line1+line1+line0+line2+line2+line0+line3+line3]
  sense.set_pixels(image[0])
  sleep(1)
