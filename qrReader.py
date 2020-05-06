from pyzbar import pyzbar
import cv2
import numpy as np



"""
Decoded(data=b'qr data', type='QRCODE', rect=Rect(left=179, top=68, width=191, height=193), polygon=[Point(x=179, y=258), Point(x=358, y=261), Point(x=370, y=82), Point(x=185, y=68)])]

"""
class qrReader:
	def __init__(self):
		pass
	def read(self, debug = False):
		cap = cv2.VideoCapture(0)
		while True:
			ret, frame = cap.read()
			barcodes = pyzbar.decode(frame)
			if barcodes is not None:
				for barcode in barcodes:
					(x, y, w, h) = barcode.rect
					cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
					barcodeData = barcode.data.decode("utf-8")
					barcodeType = barcode.type
					font = cv2.FONT_HERSHEY_SIMPLEX
					cv2.putText(frame, barcodeData, (x,y), font, 1, (0,0,255), 2, cv2.LINE_AA)
					if(not debug):
						cap.release()
						return self.parseWifi(barcodeData)
			if(debug):
				cv2.imshow('color', frame)
				if cv2.waitKey(1) & 0xFF == ord('q'):
					break
		cap.release()
		cv2.destroyAllWindows()
	def parseWifi(self,barcodeData):
		dataList = barcodeData.splitlines()
		wifi = dataList[0].replace('ssid:','')
		password = dataList[1].replace('psk:','')
		return wifi, password
		
		

