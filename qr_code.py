import segno

qrcode = input("Enter the data you want to save as a qr code:")
qrcode = segno.make_qr(qrcode)
qrcode.save("qrcode1.png")
qrcode.save("qrcode2.png", border=5, dark="#BD38CC")
qrcode.save("qrcode3.png", border=0, dark="#2977EC")



