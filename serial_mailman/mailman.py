import serial

class MailMan():
    TERMINATOR = '\r'.encode('utf8')

    def __init__(self, device, baud=115200, timeout=1):
        self.serial = serial.Serial(device, baud, timeout=timeout)

    def receive(self) -> str:
        line = self.serial.read_until(self.TERMINATOR)
        return line.decode('utf-8').strip()

    def send(self, text: str) -> bool:
        line = '%s\r\f' % text
        self.serial.write(line.encode('utf8'))
        # the line should be echoed.
        # If it isn't, something is wrong.
        return text == self.receive()

    def is_open(self):
        print(self.serial.is_open)

    def close(self):
        self.serial.close()