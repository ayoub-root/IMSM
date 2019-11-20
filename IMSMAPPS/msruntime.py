import paho.mqtt.client as mqtt
class msruntime():
    def __init__(self):
        self.client = mqtt.Client("sss")
        self.client.connect("test.mosquitto.org",1883)




    def pymicroservice(*argv, **kwargs):
        print("run service : " + str(argv[0]) + ' with option : ' + str(kwargs['args']))
        import os, django
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
        django.setup()
        from .models import Microservices
        service = Microservices.objects.get(m_id=argv[1])
        endpoint= service.endpoint

        print(service.cmd)


    def get_ms(self):
        # !/usr/bin/env python3



        # This is the Publisher


        self.client.publish("topic/test", "Hello world!");
    #   self.client.disconnect();
    def run_ms(self):
        # This is the Subscriber
        def on_connect(client, userdata, flags, rc):
            print("Connected with result code " + str(rc))
            client.subscribe("topic/test")
        def on_message(client, userdata, msg):
            if msg.payload.decode() == "Hello world!":
                print("Yes!")
                client.disconnect()

        client2 = mqtt.Client("ddd")
        client2.connect("test.mosquitto.org", 1883)

        client2.on_connect = on_connect
        client2.on_message = on_message

        client2.loop_forever()
if __name__== "__main__":



    a=msruntime()
    a.get_ms()
    a.run_ms()


    print("sss")