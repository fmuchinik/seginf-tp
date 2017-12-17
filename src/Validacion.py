#!/usr/bin/env python

import getpass

from Encrypter import Encrypter

if __name__ == "__main__":
	try:
		secretZero = getpass.getpass("Ingrese el secreto inicial \n")
		theEncrypter = Encrypter(secretZero)

		with open('youlogfile.log') as fp:
			for line in fp:
				data = bytes.decode(line.partition(':')[2].strip())
				if (line.partition(':')[0] == theEncrypter.givemeMac(data)):
					print("El log %s" % line + " --Es Correcto")
				else:
					print("El log %s" % line + " --Es Incorrecto")
	except (IOError, SystemExit):
		raise
	except KeyboardInterrupt:
		print ("Crtl+C Pressed. Shutting down.")
