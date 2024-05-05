from time import sleep
from datetime import datetime
import pyads
from motion_detection import motionDetector 

REMOTE_IP = "192.168.100.149"
REMOTE_ADS = "172.24.64.1.1.1"
PAUSE_TIME = 10 # 10 second pause when motion detected

md = motionDetector()

STATES = ["IDLE", "MOTION_DETECTED"]
state = STATES[0]

startTime = datetime.now()
curTime= datetime.now()

with pyads.Connection(REMOTE_ADS, pyads.PORT_TC3PLC1, REMOTE_IP) as plc:
    while (md.run()):
        text = [f"Pressure: {plc.read_by_name('GVL_Var.nPressure')}",f"State:{state}"]
        md.setText(text)
        print(text)
        if state == STATES[0]:
            print(f"motion status: {md.motionDetected()}")
            if (md.motionDetected()):
                print(plc.read_by_name('MAIN.bEmergencyStopPump'))
                plc.write_by_name('MAIN.bEmergencyStopPump', True)
                startTime = datetime.now()
                state = "MOTION_DETECTED"
        
        elif state == STATES[1]:
            curTime = datetime.now()
            time_diff = (curTime - startTime).total_seconds()
            if time_diff > PAUSE_TIME:
                print(plc.read_by_name('MAIN.bEmergencyStopPump'))
                plc.write_by_name('MAIN.bEmergencyStopPump', False)
                state = "IDLE"
        else:
            raise(NotImplementedError, f"The state, {state}, is not a valid state!")
    
    md.clean()
print("Cleanly exited program!")
    