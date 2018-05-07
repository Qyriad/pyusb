import usb.backend
import usb._objfinalizer as _objfinalizer
from ctypes import *

KLIST_HANDLE = c_void_p

class KLST_DEV_COMMON_INFO(Structure):
	_fields_ = \
	[
		("Vid", c_int),
		("Pid", c_int),
		("MI", c_int),
		("InstanceID", c_char * 256)
	]

class KLIST_DEV_INFO(Structure):
	_fields_ = \
	[
			("Common", KLST_DEV_COMMON_INFO),
			("DeviceInterfaceGUID", c_char * 256),
			("DeviceID", c_char * 256),
			("ClassGUID", c_char * 256),
			("Mfg", c_char * 256),
			("DeviceDesc", c_char * 256),
			("Service", c_char * 256),
			("SymbolicLink", c_char * 256),
			("DevicePath", c_char * 256),
			("LUsb0FilterIndex", c_int),
			("Connected", c_bool),
			("KLST_SYNC_FLAG", c_int),
			("BusNumber", c_int),
			("DeviceAddress", c_int),
			("SerialNumber", c_char * 256)
	]


class _libusbK(usb.backend.IBackend):
	def __init__(self):
		self.test = ""
		self.lib = cdll.libusbK
	
	def enumerate_devices(self):
		deviceList = KLIST_DEV_INFO()
		# LstK_Init(deviceList, flags)
		ret = self.lib.LstK_Init(byref(deviceList), 0)
		if ret == 0:
			print("Error initializing device list")
		else:
			count = c_ulong(0)
			self.lib.LstK_Count(deviceList, byref(count))
			print("Count: {}".format(count))


def get_backend():
	return _libusbK()

get_backend().enumerate_devices()
