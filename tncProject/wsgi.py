"""
WSGI config for tncProject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os
import threading
import requests
import time

from whitenoise.django import DjangoWhiteNoise
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tncProject.settings")

application = DjangoWhiteNoise(get_wsgi_application())


def awake():
    minute = 60
    awake_url = os.environ.get('AWAKE_URL')

    while awake_url:
        try:
            print('Start Awaking')
            requests.get(awake_url)
            print("End")
        except Exception:
            print("error")

        time.sleep(5 * minute)


t = threading.Thread(target=awake)
# t.start()
