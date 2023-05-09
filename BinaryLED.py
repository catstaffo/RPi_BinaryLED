import RPi.GPIO as GPIO
import time

# Set up the GPIO pins for the LEDs
GPIO.setmode(GPIO.BOARD)  # Use physical pins
GPIO.setup(11, GPIO.OUT)  # Pin 29 for LED 1 (most sig bit)
GPIO.setup(12, GPIO.OUT)  # Pin 31 for LED 2
GPIO.setup(13, GPIO.OUT)  # Pin 33 for LED 3
GPIO.setup(15, GPIO.OUT)  # Pin 35 for LED 4
GPIO.setup(16, GPIO.OUT)  # Pin 37 for LED 5 (least sig bit)

# Define a function to display a number in binary on the LEDs
def display_binary(number):
    # Convert the number to a binary string
    binary = bin(number)[2:]

    # Pad the string with zeros if necessary
    while len(binary) < 5:
        binary = '0' + binary

    # Turn on the LEDs corresponding to each bit
    GPIO.output(29, int(binary[0]))
    GPIO.output(31, int(binary[1]))
    GPIO.output(33, int(binary[2]))
    GPIO.output(35, int(binary[3]))
    GPIO.output(37, int(binary[4]))

# Loop through numbers 0-31 and display each one in binary on the LEDs
for number in range(32):
    display_binary(number)
    time.sleep(1)  # Wait 1 second before displaying the next number

# Clean up the GPIO pins when finished
GPIO.cleanup()

