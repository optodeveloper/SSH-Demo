# README for groov EPIC Secure Shell (SSH) Demo

To get secure shell access for your _groov_ EPIC PR-1 processor, first get a free shell license key by contacting Preferred Customer Specialists at pcs@opto22.com, then go to [manage.groov.com](manage.groov.com), select the PR-1 you want to apply the shell access key to, and then download the license file for that device.<br>
Once you have the file, go to the _groov_ Manage **System** menu in a web browser, select **License**, **Upload License**, and then upload the file you downloaded from manage.groov. After that you will need to create a shell user through the **System** **Shell** menu, which will also open port 22 for you to get remote access.

To access your _groov_ EPIC using SSH over Windows use the [PuTTY SSH client](https://www.putty.org/).<br>
Once you have the client installed, put your hostname into the connection destination, with the default port **22** and **SSH** connection type, then click **Open**. You will need to trust the new connection and log in with the user you created in groov manage, then you're good to go!

--------

To get this entire folder onto your _groov_ EPIC run the following command in the folder you want to download it to:<br>
`git clone https://github.com/optodeveloper/SSH-Demo.git`

Then navigate into the new folder with:<br>
`cd SSH-Demo`

And to view the files:<br>
`ls`

--------

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

*"pulseprogram"* Flashes output 22 on module 0 twenty two times. Source code is **pulseprogram.cpp**, uses the OptoMMP C++ SDK.
* `./pulseprogram` to run the program.


--------

## REST API: Python Scripts

The following Python Scripts use RESTful APIs thru the requests package to communicate with *groov* EPIC.

### NOTE: Updating API KEY
Before using any of the following scripts you will need to install Python-pip **and** update the API key in the `apiKey.py` file. 

**To install the requests package on *groov* EPIC:**
1. `sudo apt-get update`
2. `sudo apt-get install python-pip`
3. `sudo pip install requests`

**To get and update the API key:**
1. Go to https://hostname/manage, replacing "hostname" with your device's unique hostname.
2. Select **Accounts**
3. Select or create an account with Admin permissions.
4. Copy the long string under **API Key** at the bottom of the page, it will look like "`M7FjTXTepYhQnc9fFViTP3S3pY5GcwYP`".
5. In the shell type `nano apiKey.py`
6. Replace the `key` variable string value with the key from the Admin user, just using arrow keys and backspace or delete to remove the old string and right click to paste into PuTTY.
7. Press `ctrl + o` to write the changes and `enter` to keep the file name.
8. Press `ctrl + x` to exit the _nano_ text editor.

#### The following require an API key from a user with _groov_ Manage permissions:

*"pulsePython_Output"* will pulse _Python_Output_ on module 0, digital output channel 22, using the Manage REST API.
* `python pulsePython_Output.py`    will pulse the output twenty-two times.

*"writePython_Output"* will toggle _Python_Output_ on module 0, digital output channel 22, using the Manage REST API.
* `python writePython_Output.py on`    will turn the output on.
* `python writePython_Output.py off`    will turn the output off.

*"readtc"* returns the decimal value of analog input channel 0, module 2, which should have a thermocouple installed, using the Manage REST API.
* `python readtc.py`    will read the input channel and output the result.

*"restreaddigmodch"* returns the state of the given module and channel: two required parameters for module and channel number using the Manage API.
* `python restreaddigmodch.py 0 1`    will read the digital state of localhost module 0, channel 1, and output the result.

*"restwritedigmodch0or1"* sets the state of the given module and channel: three required parameters for module number, channel number, and state 1 or 0 using the Manage API.
* `python restwritedigmodch0or1.py 0 1 1`    will write the digital state of localhost module 0, channel 1 to be = 1 (on/true) and attempt confirmation.

#### The following require an API key from a user with PAC Control REST API permissions:

*"writePython_Var"* will write the given value to the _Python_Var_ int32 variable using the PAC Control REST API.
* `python writePython_Var.py 22`    will write 22 to the variable.

*"readLPTvar"* returns the decimal value of PAC Control float variable "_Presure_Transducer_1_" using the PAC Control REST API.
* `python readLPTvar.py`    will read the variable and output the result.
