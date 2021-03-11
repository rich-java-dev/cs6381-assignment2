import sys
from random import randrange
import argparse
from zutils import Publisher
import time
import uuid


parser = argparse.ArgumentParser()
parser.add_argument("--port", default="5555")
parser.add_argument("--topic", default="12345")
parser.add_argument("--proxy", action="store_true", default=True)
args = parser.parse_args()

port = args.port
use_proxy = args.proxy
topic = args.topic

pub_id = uuid.uuid4()

publish = Publisher(port, topic, use_proxy).start()

while True:
    zipcode = topic
    temperature = randrange(-80, 135)
    relhumidity = randrange(10, 60)
    sent_time = time.time()
    msg = f'{pub_id} {temperature} {relhumidity} {sent_time}'

    publish(zipcode, msg)
    # time.sleep(0.00000001)
