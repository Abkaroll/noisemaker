# noisemaker

A completely horrible way of exposing a server's speakers to a computer network.

## Instructions

0) Set up the django server; I'll assume it's at http://localhost:8000.
1) Log into http://localhost:8000/admin and upload a Noise file or three. Maybe make a noise group. Go nuts.
2) Open http://localhost:8000/soundboard.html and test it out
3) Have other devices on your network issue GET requests to http://localhost:8000/play_noise/your-file-name-here
4) Behold as your server's speakers play the requested sound file.

The intent here is to have a bunch of sensors hidden in an office somewhere world issue requests to one or more 
servers also hidden in that office. I'm using it to run the world's most needlessly complicated doorbell.

I wrote this in pursuit of office shenanigans and pranks. It's not production-ready by any means. 
Seriously, don't expose this to the internet. There is no authentication. There's no sign-up flow. There's no
ownership model or permissioning on the data.
