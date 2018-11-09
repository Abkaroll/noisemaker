# noisemaker

A back-end to the world's most needlessly complicated doorbell


## Instructions

1) `python manage.py runserver 0.0.0.0:8000`
2) `python manage.py makesuperuser` to make an administrator
3) Visit [the admin site](http://localhost:8000/admin). Upload a noise file or three. Maybe make a noise group. Go nuts.
4) Open [the soundboard](http://localhost:8000/) and test out your files
5) Issue a GET request to `http://localhost:8000/play_noise/your-file-name-here` from another device on your network
6) Behold as your server's speakers play the requested sound file.

The intent here is to have a computer in the room play a sound when a person interacts with something. For example:

 - Play a chime when somebody opens the door
 - Play a creaking noise when somebody sits in their chair
 - Play a snippet of [heavy metal when Bitcoin prices fall](https://www.youtube.com/watch?v=uS1KcjkWdoU)
 - Have your potted plant shout "FEED ME" when a moisture sensor detects the soil needs to be watered
 - Make a rooster crow when sunlight first hits a solar panel in the window
 
Who knows? This is really just a dumb network-connected jukebox.

**Disclaimer:** this is a *completely horrible* way of exposing your computer's speakers to a network.

Do not use this for anything serious. Do not expose it to the internet. I wrote this in pursuit of office shenanigans. 
It's not production-ready by any means: there is no authentication, no sign-up flow, no logging, no rate limiting, no 
file validation, no ownership model, no data permissioning, etc. Deploy at your own risk.
