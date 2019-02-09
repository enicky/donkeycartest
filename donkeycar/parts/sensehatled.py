import time


class SenseHatLed:
    def __init__(self):
        from sense_hat import SenseHat
        self.sense = SenseHat()
        self.invert = False
        self.rgb = (0, 0, 0)
        self.running = True
        self.on = True
        self.blink_changed = 0
        self.last_blink_rate = 0

        print("init")

    def set_rgb(self,x, y, r, g, b):
        self.rgb = (r, g, b)
        self.sense.set_pixel(x, y, self.rgb)

    def shutdown(self):
        self.running = False

    def toggle(self, condition):
        if condition:
            # print("Set RGB Leds : ", self.rgb)
            self.on = True
            self.set_rgb(0, 0, self.rgb[0], self.rgb[1], self.rgb[2])
        else:
            # print("Clear RGB Leds")
            self.sense.clear()
            self.on = False

    def run(self, blink_rate):
        if blink_rate != 1 and blink_rate != -1 and self.last_blink_rate != blink_rate:
            print("blink rate : ", blink_rate)

        if blink_rate != self.last_blink_rate:
            self.last_blink_rate = blink_rate

        if blink_rate == 0:
            self.toggle(False)
        elif blink_rate > 0:
            if blink_rate != self.last_blink_rate:
                print("Set Blink Rate ", blink_rate)
            self.blink(blink_rate)
        else:
            self.toggle(True)

    def blink(self, rate):
        if time.time() - self.blink_changed > rate:
            self.toggle(not self.on)
            self.blink_changed = time.time()


if __name__ == "__main__":
    import time
    senseHatLed = SenseHatLed()
    senseHatLed.set_rgb(1,1, 255, 0, 0)
    print("set color")
    senseHatLed.set_rgb(0, 0, 255, 0, 0)
    senseHatLed.set_rgb(0, 7, 0, 255, 0)
    senseHatLed.set_rgb(7, 0, 0, 0, 255)
    senseHatLed.set_rgb(7, 7, 255, 0, 255)
    time.sleep(1)
    print("set other stuff")

    delay = 0.1

    iter = 0
    while iter < 100:
        senseHatLed.set_rgb(2,2,iter, 100 - iter, 0)
        time.sleep(delay)
        iter += 1

    iter = 0
    while iter < 100:
        senseHatLed.set_rgb(2,2,100 - iter, 0, iter)
        time.sleep(delay)
        iter += 1
