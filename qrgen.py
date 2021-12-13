import qrcode

#Add the link at the QR
at_url = "https://github.com/IvnAcosta"

#Create instance for the QR
qr = qrcode.QRCode(
	version=1,
	box_size=10,
	border=6)

qr.add_data(at_url)
qr.make(fit=True)


img = qr.make_image(fill='black',black_color='white')
img.save('ivncv.png')
