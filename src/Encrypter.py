import logging
import SocketServer
import hashlib
import hmac
import getpass

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
