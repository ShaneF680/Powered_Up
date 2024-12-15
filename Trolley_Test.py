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

my_colors = (Color.RED, Color.YELLOW, Color.BLACK)

sensor.detectable_colors(my_colors)

while True:
    # Start the trolley
    train_motor.dc(45)
    hub.light.off()

    if sensor.color() == Color.RED:
        # 5 second stop for passengers
        print("Red")
        train_motor.stop()
        hub.light.on(Color.RED);
        wait(5000)
    elif sensor.color() == Color.YELLOW:
        # boost the speed for 1.5 seconds for a corner so the trolley doesn't slow down
        print("Yellow")
        train_motor.dc(55)
        hub.light.on(Color.YELLOW);
        wait(2000)
