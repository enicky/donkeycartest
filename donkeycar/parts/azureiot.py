import random
import time
import iothub_client

from iothub_client import IoTHubClient, IoTHubClientError, IoTHubTransportProvider, IoTHubClientResult
from iothub_client import IoTHubMessage, IoTHubMessageDispositionResult, IoTHubError, DeviceMethodReturnValue

CONNECTION_STRING = "HostName=MyIoTSensorHub.azure-devices.net;DeviceId=car;SharedAccessKey=kWs3cpbwnt0G9xc2J0lEqspFtSz/VTS4Uw8gPb7Xn8k="
PROTOCOL = IoTHubTransportProvider.MQTT
TEMPERATURE = 20.0
HUMIDITY = 60
MSG_TXT = "{\"temperature\": %.2f,\"humidity\": %.2f}"


class AzureIoT:
    def __init__(self):
        print("AzureIoT Constructor")
        self.client = IoTHubClient(CONNECTION_STRING, PROTOCOL)

    def update(self):
        print("update")

    def send_confirmation_callback(self, message, result, user_context):
        print("IoT Hub responded to message with status: %s" % (result))

    def run(self):
        try:
            print("run")
            temperature = TEMPERATURE + (random.random() * 15)
            humidity = HUMIDITY + (random.random() * 20)
            msg_txt_formatted = MSG_TXT % (temperature, humidity)
            message = IoTHubMessage(msg_txt_formatted)

            print("Sending message: %s" % message.get_string())
            self.client.send_event_async(message, self.send_confirmation_callback, None)
            time.sleep(1)
        except IoTHubError as iothub_error:
            print("Unexpected error %s from IoTHub" % iothub_error)
            return

    def run_threaded(self, img_arr=None):
        print("run threaded")



if __name__ == "__main__":
    print("main has been started ... ")
    iot = AzureIoT()
    iot.run()
