import time

def move_forward_smooth(drone, distance_cm=50, speed_cm_s=50, ramp_s=0.2):
    # คำนวณ duration รวม
    speed = max(1, min(int(speed_cm_s), 100))
    total_time = distance_cm / speed
    cruise_time = max(0, total_time - 2 * ramp_s)

    # ramp up (5 step)
    steps = 5
    for i in range(1, steps + 1):
        v = int(speed * i / steps)
        drone.send_rc_control(0, v, 0, 0)
        time.sleep(ramp_s / steps)

    # cruise
    time.sleep(cruise_time)

    # ramp down
    for i in reversed(range(1, steps + 1)):
        v = int(speed * i / steps)
        drone.send_rc_control(0, v, 0, 0)
        time.sleep(ramp_s / steps)

    # stop
    drone.send_rc_control(0, 0, 0, 0)
