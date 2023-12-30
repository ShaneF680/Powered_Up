from pybricks.hubs import CityHub
from pybricks.pupdevices import DCMotor, Light, ColorDistanceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = CityHub()

# Initialize the motor.
train_motor = DCMotor(Port.A)

# Initialize the sensor.
sensor = ColorDistanceSensor(Port.B)

#Override Red
#Color.RED = Color(h=0, s=82, v=55)

my_colors = (Color.RED, Color.BLACK)

sensor.detectable_colors(my_colors)

# This is a function that waits for a desired color.
def wait_for_color(desired_color):
    # While the color is not the desired color, we keep waiting.
    while sensor.color() != desired_color:
        wait(20)

while True:
   # Here you can make your train/vehicle go forward.
    train_motor.dc(40)

    print("Waiting for red ...")
    wait_for_color(Color.RED)

    # Here you can make your train/vehicle go backward.
    train_motor.stop()
    wait(5000)

# Choose the "power" level for your train. Negative means reverse.
#train_motor.dc(40)
#wait(3000)

#train_motor.dc(-40)
#wait(3000)

#train_motor.stop()
