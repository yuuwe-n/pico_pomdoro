# pico-pomodoro
> simple pomodoro timer using a raspberry pi pico microcontroller

# docs
[pico](https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html)

# development

development notes are for OpenBSD based machines

# picotool

> im not sure if I already installed the build tools so I am not sure of the dependencies

[pico getting started](https://datasheets.raspberrypi.com/pico/getting-started-with-pico.pdf)

## pico-sdk 

```
git clone -b master https://github.com/raspberrypi/pico-sdk.git
cd pico-sdk
git submodule update --init
```

you can place this export line in your `.profile`

```
export PICO_SDK_PATH=<path to pico sdk>
```

## build
```
git clone https://github.com/raspberrypi/picotool.git
cd picotool
mkdir build
cd build
cmake ..
make
```
