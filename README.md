# noisemaker

A back-end to the world's most needlessly complicated doorbell


## Instructions

1) `python manage.py runserver 0.0.0.0:8000`
2) `python manage.py makesuperuser` to make an administrator
3) Visit [the admin site](http://localhost:8000/admin)
4) Upload a noise file or three. Maybe make a noise group. Go nuts.
5) Open [the soundboard](http://localhost:8000/) and test out your files
6) Issue a GET request to `http://localhost:8000/play_noise/your-file-name-here` from another device on your network
7) Behold as your server's speakers play the requested sound file.
8) Plant network-aware motion sensors all over your office.

The intent here is to run the world's most needlessly complicated doorbell.

**Disclaimer:** this is a *completely horrible* way of exposing your computer's speakers to a network.

Do not use this for anything serious. Do not expose it to the internet. I wrote this in pursuit of office shenanigans. 
It's not production-ready by any means: there is no authentication, no sign-up flow, no logging, no rate limiting, no 
file validation, no ownership model, no data permissioning, etc. Deploy at your own risk.
