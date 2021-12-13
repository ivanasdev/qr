import qrcode 
url = "https://upload.wikimedia.org/wikipedia/commons/e/e9/Sigmund_Freud_1926.jpg"
img =  qrcode.make(url)



img.show()
