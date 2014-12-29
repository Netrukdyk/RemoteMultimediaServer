from win32api import keybd_event, MapVirtualKey
from win32con import KEYEVENTF_KEYUP
import time
import os

VK_MEDIA_NEXT_TRACK = 0xB0
VK_MEDIA_PREV_TRACK = 0xB1
VK_MEDIA_STOP = 0xB2
VK_MEDIA_PLAY_PAUSE = 0xB3
VK_VOLUME_MUTE = 0xAD
VK_VOLUME_DOWN = 0xAE
VK_VOLUME_UP = 0xAF
VK_LAUNCH_MEDIA_SELECT = 0xB5
VK_SLEEP = 0x5F
VK_F11 = 0x7A
VK_LMENU = 0xA4 #left alt
VK_RETURN = 0x0D #enter

nextCode = MapVirtualKey(VK_MEDIA_NEXT_TRACK, 0)
prevCode = MapVirtualKey(VK_MEDIA_PREV_TRACK, 0)
stopCode = MapVirtualKey(VK_MEDIA_STOP, 0)
playCode = MapVirtualKey(VK_MEDIA_PLAY_PAUSE, 0)
muteCode = MapVirtualKey(VK_VOLUME_MUTE, 0)
voldCode = MapVirtualKey(VK_VOLUME_DOWN, 0)
voluCode = MapVirtualKey(VK_VOLUME_UP, 0)
mediaCode = MapVirtualKey(VK_LAUNCH_MEDIA_SELECT, 0)
sleepCode = MapVirtualKey(VK_SLEEP, 0)
f11Code = MapVirtualKey(VK_F11, 0)
lmenuCode = MapVirtualKey(VK_LMENU, 0)
returnCode = MapVirtualKey(VK_RETURN, 0)

def next():
	keybd_event(VK_MEDIA_NEXT_TRACK, nextCode)
	
def prev():
	keybd_event(VK_MEDIA_PREV_TRACK, prevCode)
	
def play():
	keybd_event(VK_MEDIA_PLAY_PAUSE, playCode)
	
def stop():
	keybd_event(VK_MEDIA_STOP, stopCode)
	
def mute():
	keybd_event(VK_VOLUME_MUTE, muteCode)
	
def vold():
	keybd_event(VK_VOLUME_DOWN, voldCode)
	
def volu():
	keybd_event(VK_VOLUME_UP, voluCode)

def media():
	keybd_event(VK_LAUNCH_MEDIA_SELECT, mediaCode)

def zoom():
	#keybd_event(VK_F11, f11Code)
	keybd_event(VK_LMENU, 0,0,0)
	keybd_event(VK_RETURN, 0,0,0)
	time.sleep(.05)
	keybd_event(VK_LMENU,0 ,KEYEVENTF_KEYUP ,0)
	keybd_event(VK_RETURN,0 ,KEYEVENTF_KEYUP ,0)
	
def sleep():
	#keybd_event(VK_SLEEP, sleepCode)
	os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
