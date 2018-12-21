# README for groov EPIC Secure Shell (SSH) Demo

------------

## OptoMMP: Python Scripts

The following Python scripts use OptoMMP thru the socket interface to communicate *groov* EPIC:

*"mmpgetuptime"* returns the uptime (ms) of the controller: one optional parameter for host.
* `python mmpgetuptime.py`    will default to localhost.
* `python mmpgetuptime.py <hostname or IP address>`    will get the given host's uptime.

*"mmpreaddigmodch"* returns the state of the given module and channel: two required parameters for module and channel number.
* `python mmpreaddigmodch.py 0 1`    will read the digital state of localhost module 0, channel 1, and output the result.

*"mmpwritedigmodch0or1"* sets the state of the given module and channel: three required parameters for module number, channel number, and state 1 or 0
* `python mmpwritedigmodch0or1.py 0 1 1`    will write the digital state of localhost module 0, channel 1 to be = 1 (on/true) and attempt confirmation.


--------

## OptoMMP: Executable file compiled from C++ code

*"pulseprogram"* Flashes output 22 on module 0 twenty two times. Source code is pulseprogram.cpp, uses the OptoMMP C++ SDK.
* `sudo chmod +x pulseprogram` to make the file executable,
* `./pulseprogram` to run the program.


--------

## REST API: Python Scripts

The following Python Scripts use the Manage RESTful API thru the requests package to communicate with *groov* EPIC:

*"restreaddigmodch"* returns the state of the given module and channel: two required parameters for module and channel number.
* `python restreaddigmodch.py 0 1`    will read the digital state of localhost module 0, channel 1, and output the result.

*"restwritedigmodch0or1"* sets the state of the given module and channel: three required parameters for module number, channel number, and state 1 or 0
* `python restwritedigmodch0or1.py 0 1 1`    will write the digital state of localhost module 0, channel 1 to be = 1 (on/true) and attempt confirmation.

### **NOTE:** To install the requests package on *groov* EPIC
1. `sudo apt-get update`
2. `sudo apt-get install python-pip`
3. `pip install requests`
