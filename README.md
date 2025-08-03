![logo](/logo_loock.png)


# Application for unlocking locks using face ID

# LOOcK

Our project implements face ID and actual physical lock (safe) build from scratch by us.

The system is designed to unlock the physical safe anytime the current user has a reference photo in the database and our model reaches the probabilty over 80%.

### physical architecture

<img width="1330" height="855" alt="image" src="https://github.com/user-attachments/assets/b4d167f3-226a-4989-a382-f8b6ff9a853e" />

<img width="584" height="413" alt="image" src="https://github.com/user-attachments/assets/a9a0ca79-6f6f-4a8c-8da9-5abc70cfeb2b" />

Main device here is SHELLY, served with API and managed by our python application.

### how to install?

throught linux and docker

`docker build -t loock .`

`xhost +local:docker`

```docker run -it --rm \ 

  --device /dev/video0:/dev/video0 \ 

  -e DISPLAY=$DISPLAY \ 

  -v /tmp/.X11-unix:/tmp/.X11-unix \ 

  loock

xhost -local:docker```

