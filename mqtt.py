import time
import threading
import paho.mqtt.client

class mqtt(threading.Thread):
    def __init__(self):
        self.client = paho.mqtt.client.Client()
        self.client.tls_set(ca_certs="ca.crt")
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect("192.168.1.15")

        threading.Thread.__init__(self)
        self.start()

    def on_connect(self, client, userdata, flags, rc):
        client.subscribe("time")

    def on_message(self, client, userdata, msg):
        print(msg.topic+":" + str(msg.payload))

    def forever(self):
        self.client.loop_forever()

    def run(self):
        while True:
            time.sleep(1)
            self.client.publish("time", time.time(), qos=2, retain=True)

mq = mqtt()
mq.forever()