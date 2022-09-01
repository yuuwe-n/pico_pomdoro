# pico-pomodoro
> simple pomodoro timer using a raspberry pi pico microcontroller

# docs
[pico](https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html)

# development

development notes are for OpenBSD based machines

# firmware
[python sdk](https://datasheets.raspberrypi.com/pico/raspberry-pi-pico-python-sdk.pdf)

Find Raspberry Pi Pico inside dmesg to see if it is connected
```
dmesg | grep uhub
```

Install firmware
1. disconnect usb connection with pico
2. see drives using `sysctl.hwdisknames`
3. connect pico
4. see drives using `sysctl.hwdisknames`, if you see a new drive conncted, that is the pico probably
5. mount/add firmware
```
mount /dev/<disk> /mnt/usb
doas wget https://micropython.org/download/rp2-pico/rp2-pico-latest.uf2
```
6. disconnect/reconnect usb

7. connect via minicom `pkg_add minicom`
```
minicom -D /dev/ttyU0
```

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

`pkg_add cmake`

```
git clone https://github.com/raspberrypi/picotool.git
cd picotool
mkdir build
cd build
cmake ..
make
```
