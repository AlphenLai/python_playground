from pymavlink import mavutil
import sys
import time

# Create the connection
# Need to provide the serial port and baudrate
master = mavutil.mavlink_connection("/dev/serial/by-id/usb-Hex_ProfiCNC_CubeBlack_1A002E001351373332383537-if00", baud=115200)

# Restart the ArduSub board !
# master.reboot_autopilot()

master.mav.log_request_list_send(
    master.target_system,
    master.target_component,
    0,
    0xffff)

while True:
    msg = master.recv_match()
    if not msg:
        continue
    if msg.get_type() == 'LOG_ENTRY':
        print("\n\n*****Got message: %s*****" % msg.get_type())
        print("Message: %s" % msg)
        print("\nAs dictionary: %s" % msg.to_dict())
        # Armed = MAV_STATE_STANDBY (4), Disarmed = MAV_STATE_ACTIVE (3)
        if msg.num_logs == msg.id:
            break

print ('begin to request log data')
master.mav.log_request_data_send(
    master.target_system,
    master.target_component,
    117,
    5591040,
    90)

while True:
    msg = master.recv_match()
    if not msg:
        continue
    if msg.get_type() == 'LOG_DATA':
        print("\n\n*****Got message: %s*****" % msg.get_type())
        print("Message: %s" % msg)
        print("\nAs dictionary: %s" % msg.to_dict())
        # Armed = MAV_STATE_STANDBY (4), Disarmed = MAV_STATE_ACTIVE (3)