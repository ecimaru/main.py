import bluetooth
from bluetooth import *

client = BluetoothSocket(RFCOMM)
bd_addr = "DC:A6:32:DD:39:C4"

client.connect((bd_addr,1))
print("Coonected. Type something...")

while True :
    data = input('입력하세요.')
    if not data:
        break
    client.send(data)

client.close()