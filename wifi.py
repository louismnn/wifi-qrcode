from wifi_qrcode_generator.generator import wifi_qrcode
from PIL import Image

ssid = "" # The wifi network name
password = "" # The password
authentication_type = "WPA"

qr = wifi_qrcode(ssid, False, authentication_type=authentication_type, password=password)

qr.make_image().save("wifi_qr_code.png")
