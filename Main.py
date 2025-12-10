#RC Car

from machine import Pin, PWM
from machine import Pin, UART
import time
import utime
import machine
from machine import I2C



uart = UART(1, 9600, rx=Pin(5), tx=Pin(4) , bits=8, parity=None, stop=1, timeout=1)

car_led = Pin(21, Pin.OUT)#Lewy

Led = Pin(25, Pin.OUT)
Led.on()
PWN_A = Pin(18, Pin.OUT)#Lewy
PWN_B = Pin(22, Pin.OUT)#Prawy

#Osbługa sterownika silników TB6612FNG 
IN_B1 = Pin(27, Pin.OUT)#Prawy
IN_B2 = Pin(26, Pin.OUT)#Prawy


IN_A1 = Pin(19, Pin.OUT)#Lewy
IN_A2 = Pin(20, Pin.OUT)#Lewy

PWN_B.on()
PWN_A.on()

#Osbługa sterownika silników TB6612FNG 
led_counter = 0
led_counter1 = 0
#Klakson
def buzzer():
    buzzer = PWM(Pin(28))
    horn_freq = 450  
    horn_duty = 1000  
    horn_duration = 0.2
    for _ in range(1):  
    
        buzzer.freq(horn_freq)
        buzzer.duty_u16(horn_duty)
        time.sleep(horn_duration)

        
        buzzer.duty_u16(0)
        time.sleep(0.1)

        
        buzzer.freq(horn_freq)
        buzzer.duty_u16(horn_duty)
        time.sleep(horn_duration * 2)  

        
        buzzer.duty_u16(0)
        time.sleep(0.2)

    #Klakson
    buzzer.duty_u16(0)



#Koło prawe
###################
def prawe_forward():
    PWN_B.on()
    IN_B1.off()
    IN_B2.on()

def prawe_back():
    PWN_B.on()
    IN_B1.on()
    IN_B2.off()
def prawe_stop():
    PWN_B.on()
    IN_B1.off()
    IN_B2.off()
###################
#Koło prawe
#Koło lewe
###################
def lewe_forward():
    PWN_A.on()
    IN_A1.off()
    IN_A2.on()

def lewe_back():
    PWN_A.on()
    IN_A1.on()
    IN_A2.off()
def lewe_stop():
    PWN_A.on()
    IN_A1.off()
    IN_A2.off()
###################
#Koło lewe
#2x2
###################
def forweard_2x2():
    lewe_forward()
    prawe_forward()

def back_2x2():
    lewe_back()
    prawe_back()
###################
#2x2
def w_lewo():
    lewe_stop()
    prawe_forward()
    time.sleep(1)
    lewe_forward()
    time.sleep(1)

def w_prawo():
    prawe_stop()
    lewe_forward()
    time.sleep(1)
    prawe_forward()
    time.sleep(1)
    
def w_kolo_prawe():
    prawe_back()
    lewe_forward()
    time.sleep(0.1)
    
def w_kolo_lewe():
    lewe_back()
    prawe_forward()
    time.sleep(0.1)
    


while True:
    #Przyjmowanie i wykonywanie danych.
    if uart.any():
        input_data = uart.read().decode().strip()
        if input_data == "1":
            forweard_2x2()
            time.sleep(0.3)
            lewe_stop()
            prawe_stop()
        if input_data == "2":
            back_2x2()
            time.sleep(0.3)
            lewe_stop()
            prawe_stop()
        if input_data == "3":
            w_prawo()
            time.sleep(0.3)
            lewe_stop()
            prawe_stop()
        if input_data == "4":
            w_lewo()
            time.sleep(0.3)
            lewe_stop()
            prawe_stop()
        if input_data == "5":
            w_kolo_prawe()
            time.sleep(0.3)
            lewe_stop()
            prawe_stop()
        if input_data == "6":
            w_kolo_lewe()
            time.sleep(0.3)
            lewe_stop()
            prawe_stop()
        if input_data == "7":
            buzzer()
        
        #Obsługa led
        if led_counter1 == 1 and input_data == "8":
            car_led.off()
            led_counter1 = 0
        elif input_data == "8":
            if led_counter1 == 0:
                led_counter1 = 1
                car_led.on()
            

