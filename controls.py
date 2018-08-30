import pyvjoy
j = pyvjoy.VJoyDevice(1)

def xAxis(angle):
	bearing=16834-int((angle/90)*16384) 
	j.set_axis(pyvjoy.HID_USAGE_X,bearing)

def reCentre():
	j.set_button(2,0)
	j.set_button(1,0)
	j.set_axis(pyvjoy.HID_USAGE_Y,0x0000)
	j.set_button(1,0)
def yAxis(speed):
	j.set_button(2,0)
	acceleration=int((speed/100)*32678)
	j.set_axis(pyvjoy.HID_USAGE_Y,acceleration)
	
def Brake():
	j.set_button(1,0)
	j.set_button(2,1)
	