#!/usr/bin/env python

LOG_FILE = 'youlogfile.log'
HOST, PORT = "0.0.0.0", 514


import logging
import SocketServer
import hashlib
import hmac
import getpass


logging.basicConfig(level=logging.INFO, format='%(message)s', datefmt='', filename=LOG_FILE, filemode='a')


__metaclass__ = type

class SyslogUDPHandler(SocketServer.BaseRequestHandler):

	def handle(self):
		data = bytes.decode(self.request[0].strip())
		socket = self.request[1]

		mac = theEncrypter.givemeMac(data)

		newLogLine = mac + ":" + data

		print(newLogLine)
		logging.info(newLogLine)



class Encrypter():

	def __init__(self, secretZero):
		# el secreto inicial se usa lo antes posible para reducir la posibilidad de lecturas en memoria 
		self.actualHashedKey = self.__hashForMac(secretZero)

	def givemeMac(self, msg):
		hmacGenerator = hmac.new(self.actualHashedKey, msg, hashlib.sha1)
		self.actualHashedKey = self.__hashForMac(self.actualHashedKey)

		return hmacGenerator.hexdigest()


	def __hashForMac(self, secret):
		# 0 para distinguir key de hash o de encripcion
		return hashlib.sha1("0" + secret).hexdigest()


if __name__ == "__main__":
	try:
		secretZero = getpass.getpass("Ingrese el secreto inicial \n")
		theEncrypter = Encrypter(secretZero)

		server = SocketServer.UDPServer((HOST,PORT), SyslogUDPHandler)
		print("Escuchando en %s:%s" % (HOST, PORT))
		server.serve_forever(poll_interval=0.5)

	except (IOError, SystemExit):
		raise
	except KeyboardInterrupt:
		print ("Crtl+C Pressed. Shutting down.")






