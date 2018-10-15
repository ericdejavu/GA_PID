# -*- coding:utf-8 -*-
import wiringpi as rpi
import UUGear import *
from const_str import *

import time

# v=读取到的数值
# n=实际数值
#
# R1=30000
# R2=7500
#
# 公式：
# v=(( n * 5.0 ) / 1024.0 ) / ( R2 / ( R1 + R2 ))

class Motor:
    def __init__(self):
        rpi.wiringPiSetup()
        self.pin_out(pin=SERIAL_LED_PIN)
        self.pin_out(pinpin=SYS_STATUS_PIN)
        self.pin_softpwm(pin=MOTOR_PIN_P)
        self.pin_softpwm(pin=MOTOR_PIN_N)
        self.pin_in(pin=INPUT_PIN_R)
        self.pin_in(pin=SWITCH_PIN)
        self.get_arduino()

    def get_arduino(self):
        UUGearDevice.setShowLogs(0)
        self.device = UUGearDevice(ARDUINO_DEVICE)
        if self.device.isValid():
            self.high(SERIAL_LED_PIN)
            for i in range(MAX_TRY_CNT):
                print '%0.2' % self.get_volt()
                time.sleep(0.2)
        else:
            self.low(SERIAL_LED_PIN)
            print 'during device connectting throw error'
            self.device_disconnect()


    def device_disconnect(self):
        self.device.detach()
        self.device.stopDaemon()


    def get_volt(self):
        r = ARDUINO_TO_RPI_R2 / ( ARDUINO_TO_RPI_R1 + ARDUINO_TO_RPI_R2 )
        mapping = ( self.device.analogRead(ARDUINO_FEEDBACK_PIN) * 5.0 ) / 1024.0
        return mapping / R

    def get_angle(self):
        mapping = ( self.device.analogRead(ARDUINO_FEEDBACK_PIN) * 180 ) / 1024.0
        return mapping

    def pin_out(self,pin):
        rpi.pinMode(pin,PIN_OUTPUT)

    def pin_pwm(self,pin):
        rpi.pinMode(pin,PIN_PWM)

    def pin_softpwm(self,pin):
        self.pin_out(pin)
        rpi.softPwmCreate(pin,MIN_PWM_VAL,MAX_PWM_VAL)

    def pin_in(self,pin):
        rpi.pinMode(pin,PIN_INPUT)

    def high(self,pin):
        rpi.digitalWrite(pin,HIGH)

    def low(self,pin):
        rpi.digitalWrite(pin,LOW)

    def pwm(self,pin,val):
        if MIN_PWM_VAL =< val =< MAX_PWM_VAL:
            rpi.softPwmWrite(pin,val)

    def sys_led(self,mode,rate):
        if mode == BLINK:
            self.high(pin=SYS_STATUS_PIN)
            self.low(pin=SYS_STATUS_PIN)
        elif mode == RUNNING:
            self.high(pin=SYS_STATUS_PIN)
        elif mode == SHUTDOWN:
            self.low(pin=SYS_STATUS_PIN)
