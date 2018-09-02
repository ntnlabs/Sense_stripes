from sense_hat import SenseHat
from time import sleep

# setup the enviroment
sense = SenseHat()
sense.set_rotation(0)
sense.low_light = True
sense.clear()

# define many colors
b = (0,0,0)
r1 = (255,0,0)
r2 = (192,0,0)
r3 = (129,0,0)
r4 = (66,0,0)
g1 = (0,255,0)
g2 = (0,192,0)
g3 = (0,129,0)
g4 = (0,66,0)
b1 = (0,0,255)
b2 = (0,0,192)
b3 = (0,0,129)
b4 = (0,0,66)
rb1 = (255,0,255)
rb2 = (192,0,192)
rb3 = (129,0,129)
rb4 = (66,0,66)
gb1 = (0,255,255)
gb2 = (0,192,192)
gb3 = (0,129,129)
gb4 = (0,66,66)
rg1 = (255,255,0)
rg2 = (192,192,0)
rg3 = (129,129,0)
rg4 = (66,66,0)
rgb1 = (255,255,255)
rgb2 = (192,192,192)
rgb3 = (129,129,129)
rgb4 = (66,66,66)

# add startup colorful effect
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

  # Round the values to no decimal place
  # t = round(t, 0)
  # p = round(p, 0)
  # h = round(h, 0)

  if t < 20:
   line1 = [b,b,b,b,b,b,b,r3]
  elif t > 90:
   line1 = [r1,r1,r1,r1,r1,r1,r1,r1]
  else:
   line1 = [r2]*int((t-10)/10)
   if len(line1) < 8:
    line1 = line0[0:8-len(line1)]+line1

  if h < 20:
   line3 = [b,b,b,b,b,b,b,b3]
  elif h > 90:
   line3 = [b1,b1,b1,b1,b1,b1,b1,b1]
  else:
   line3 = [b2]*int((h-10)/10)
   if len(line3) < 8:
    line3 = line0[0:8-len(line3)]+line3

  # Create the message
  # str() converts the value to a string so it can be concatenated
  message = "Temperature: " + str(t) + " Pressure: " + str(p) + " Humidity: " + str(h)


  # Display the scrolling message
  # sense.show_message(message, scroll_speed=0.05)
  print(message)
  image = [line1+line1+line0+line2+line2+line0+line3+line3]
  sense.set_pixels(image[0])
  sleep(10)
