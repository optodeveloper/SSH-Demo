#include <stdlib.h>
#include "O22SIOMM.h"
#include "O22STRCT.h"
int main() {
	const char *address = "127.0.0.1";
	const int module = 0;
	const int point = 22;
	
	O22SnapIoMemMap demo_EPIC;
	// open a TCP connection to the host at 'address' port 2001
	int nResult = demo_EPIC.OpenEnet2(address, 2001, 10000, 1, SIOMM_TCP);
	if(nResult != SIOMM_OK) {
		printf("OpenEnet2 reports result %d, exiting.\n", nResult);
		exit(0);
	}
	// wait for the TCP connection to complete, not necessary for UDP
	usleep(100000);
	// toggle the output 44 times: ON for even i, OFF for odd i for 22 "pulses".
	for(int i = 0; i < 44; i++) {
		nResult = demo_EPIC.SetHDDigitalPointState(module, point, ((i+1) % 2));
		if(nResult != SIOMM_OK) {
			printf("SetHDDigitalPointState reports result %d, exiting.\n", nResult);
			exit(0);
		}
		// rest for 1/3 seconds before toggling again.
		usleep(333333);
	}
	return 0;
}
