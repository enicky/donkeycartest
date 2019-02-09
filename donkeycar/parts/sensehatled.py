class SenseHatLed:
    def __init__(self):
        from sense_hat import SenseHat
        self.sense = SenseHat()
        self.invert = False
        self.rgb = (0,0,0)
        print("init")

    def set_rgb(self,x, y, r, g, b):
        r = r if not self.invert else 100 - r
        g = g if not self.invert else 100 - g
        b = b if not self.invert else 100 - b
        self.rgb = (r, g, b)

        self.sense.set_pixel(x, y, self.rgb)


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
    print("set other tuff")

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
