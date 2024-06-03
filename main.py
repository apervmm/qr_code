import pyqrcode

qr_str = "https://almas-resume.vercel.app/"

url_to_qr = pyqrcode.create(qr_str)
url_to_qr.png("my_qrcode.png", scale = 8)