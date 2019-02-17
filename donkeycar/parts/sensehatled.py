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
        self.last_usermode_led_status = 0

        print("init")

    def set_rgb(self,x, y, r, g, b):
        self.rgb = (r, g, b)
        self.sense.set_pixel(x, y, self.rgb)

    def shutdown(self):
        self.sense.clear()
        self.running = False

    def toggle(self, condition):
        if condition:
            print("Set RGB Leds : ", self.rgb)
            self.on = True
            self.set_rgb(0, 0, self.rgb[0], self.rgb[1], self.rgb[2])
        else:
            print("Clear RGB Leds")
            #self.sense.clear()
            self.set_rgb(0, 0, 0, 0, 0)
            self.on = False

    def run(self, blink_rate, user_mode_status, target_mode_status):

        if blink_rate != 1 and blink_rate != -1 and self.last_blink_rate != blink_rate:
            print("blink rate : ", blink_rate)

        if blink_rate != self.last_blink_rate:
            self.last_blink_rate = blink_rate

        if blink_rate == 0:
            self.toggle(False)
        elif blink_rate > 0:
            #print("current blink rate : ", self.last_blink_rate, blink_rate)
            if blink_rate != self.last_blink_rate:
                print("Set Blink Rate ", blink_rate)
            self.blink(blink_rate)
        else:
            self.toggle(True)

        self.set_current_mode_status_leds(user_mode_status)
        self.set_target_mode_status_leds(target_mode_status)

    def set_current_mode_status_leds(self, user_mode_status):
        if self.last_usermode_led_status != user_mode_status:
            self.last_usermode_led_status = user_mode_status
            print("current led status : ", user_mode_status)

        if user_mode_status == 1:
            self.sense.set_pixel(5, 5, (0, 255, 0))
        elif user_mode_status == 2:
            self.sense.set_pixel(5, 5, (255, 255, 0))
        elif user_mode_status == 3:
            self.sense.set_pixel(5, 5, (0, 0, 255))

    def set_target_mode_status_leds(self, target_mode):
        if target_mode == 1:
            self.sense.set_pixel(5, 6, (0, 255, 0))
        elif target_mode == 2:
            self.sense.set_pixel(5, 6, (255, 255, 0))
        elif target_mode == 3:
            self.sense.set_pixel(5, 6, (0, 0, 255))

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
