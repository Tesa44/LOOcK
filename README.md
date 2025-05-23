![logo](/logo_loock.png)


# LOOcK Application for unlocking locks using face ID

how to install?

throught linux and docker

`docker build -t loock .`

`xhost +local:docker`

```docker run -it --rm \ 

  --device /dev/video0:/dev/video0 \ 

  -e DISPLAY=$DISPLAY \ 

  -v /tmp/.X11-unix:/tmp/.X11-unix \ 

  loock

xhost -local:docker```

