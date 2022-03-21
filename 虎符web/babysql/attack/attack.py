
import binascii

for asci in range(32,126):
	a = chr(asci)
	with  open('sample.txt','a') as f:
		f.write(a+'\n')
		print(1)
		f.close()