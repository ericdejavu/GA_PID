import motor
import schedule

class Control:
    def __init__(self):
        self.motor = motor.Motor()
        self.sys_status = SHUTDOWN
        schedule.every(0.2).seconds.do(self.motor.sys_led,mode,rate)
        self.init_angle = self.motor.get_angle()
        if not self.is_frist_position_at_zero(self.init_angle):
            self.set_frist_position_to_zero()

    def accept_err(self, _set, val):
        return self.err_between(_set, val, LEFT_OFFSET, RIGHT_OFFSET)

    def err_between(self, _set, val, left, right):
        return _set + left =< val =< _set + right

    def is_frist_position_at_zero(self, angle):
        return self.accept_err(INIT_ANGLE, angle, val)

    def set_frist_position_to_zero(self):
        while self.is_frist_position_at_zero(angle):
            self.motor.get_angle()

    def run(self):
        while True:
            schedule.run_pending()
