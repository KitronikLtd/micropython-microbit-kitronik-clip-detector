# micropython-microbit-kitronik-clip-detector

Example MicroPython (for BBC micro:bit) code for the Kitronik Clip Detector board (www.kitronik.co.uk/5678 )

Note:
The example code is used for the web editor for python micro:bit ( python.microbit.org )

Read Digital Sensor:
This package will return back a True or False for detection with a comparision of a reference reading (taken at the start).  Pin selection is by "P0", "P1", "P2".  Detection selection is by "Dark", "light"
```blocks
readDigitalSensor("P2", "Dark")
```

Read Analog Sensor:
This package will return back a ADC value from 0-1023 representing the analog voltage of the sensor.  Pin selection is by "P0", "P1", "P2".
```blocks
readAnalogSensor("P0")
```

Sensor Setup:
This package will set the threshold for the sensors depending on what the is required to detect. Selection is by "Line", "Light", "Object".
```blocks
sensorSetup("Line")
```
