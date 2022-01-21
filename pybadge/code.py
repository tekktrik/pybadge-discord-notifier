"""
This is a Conference Badge type Name Tag that is intended to be displayed on
the PyBadge. Feel free to customize it to your heart's content.
"""

import time
import board
from micropython import const
import displayio
from adafruit_airlift.esp32 import ESP32
from adafruit_ble import BLERadio
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.nordic import UARTService
from discord_display import DiscordMessageGroup
from screen_displays import ScreenManager, SplashBackground, TextSplashScreen

try:
    from typing import Optional
except ImportError:
    pass

# Button Constants
BUTTON_LEFT = const(128)
BUTTON_UP = const(64)
BUTTON_DOWN = const(32)
BUTTON_RIGHT = const(16)
BUTTON_SEL = const(8)
BUTTON_START = const(4)
BUTTON_A = const(2)
BUTTON_B = const(1)

CURRENT_MESSAGE = None

screen = ScreenManager()
screen.set_loading_splash()

# Set up Bluetooth
esp32 = ESP32(
    reset=board.D12,
    gpio0=board.D10,
    busy=board.D11,
    chip_select=board.D13,
    tx=board.TX,
    rx=board.RX,
)
adapter = esp32.start_bluetooth()
ble = BLERadio(adapter)

screen.set_connecting_splash()

# Main loop
while True:
    
    # While connected, look through connections and connect to one with UARTService
    while ble.connected and any(
        UARTService in connection for connection in ble.connections
    ):
        print("UARTService found in connection, getting connection...")
        for connection in ble.connections:
            if UARTService not in connection:
                continue
            uart: UARTService = connection[UARTService]
            print("UARTService connected!")

            # Show message background
    print("No connections to be made :(")
    time.sleep(1)
    
    screen.set_no_message_splash()
    time.sleep(1)

    message = DiscordMessageGroup("This is a test message! It is considerably longer than the previous message, but this will let me test the wrapping and cutoff of texts.", "Tekktrik", 0)
    screen.set_message_splash(message)

    while True:

        time.sleep(1)

            # Main functionality goes here
