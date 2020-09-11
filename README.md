# eInk_Moon_ISS_PeopleSpace
Raspberry eInk HAT to show the phase of the Moon, where is the ISS, How many people are in the space...


I had a Raspberry and a e-Paper HAT and I wanted to use it to show information like where is the ISS or how many people are now in the space...

I stated to look if there are APIs on the Internet to get those data, and I found them.
OK, gotcha !!!!

Wait, this HAT has 4 buttons, and then, I need 4 data to be shown...

- Where is now the **ISS**?
- How many **people** are now in the **space**?
- In which phase is the **Moon**?
- Is it **going to rain**?

Well, I made it on one evening and the "*FrontEnd*" was ended a few days after.
Don't complain about how the information is shown, I don't like to make this part :)


This project is to show data on a **e-Paper screen**, and the refresh is not every second, it could be every hour or every 5 minutes, depending on what you are showing.
For example, the phase of the Monn is not going to change until some hours, but tht ISS is moving and probably you want to show it every 5 minutes, but not every second.

This is a good project to be used with the eInk screen.

[![GIF](ShowInformation.gif)]

![ISS](ISS.jpg?raw=true "Where is the ISS")
![Space](People_Space.jpg?raw=true "Who is on the Space?")
![Moon](Moon_phase.jpg?raw=true "Moon Phase")
![Weather](WeatherForecast.jpg?raw=true "Weather Forecast")


Needed things:
- **Raspberry PI** (Zero is enough).
- **2.7inch e-Paper HAT**. (I bought mine here: https://www.amazon.de/gp/product/B07FFMH858/ref=ppx_yo_dt_b_asin_title_o04_s00)
- **SD** card (4Gb is enough).


Installation:
Follow the steps on the next files...
- Installation_OS
- Installation_Needed_Software

As an alternative, the Python script can be started during boot by creating a service - more info at https://www.raspberrypi.org/documentation/linux/usage/systemd.md

The file "*ShowInfo.service*" is on the folder.
Copy the ShowInfo.service file into /etc/systemd/system as root:

```
sudo cp ShowInfo.service /etc/systemd/system/
```

Start the service:

```
sudo systemctl start ShowInfo.service
```

Check if the service is running:

```
sudo systemctl status ShowInfo.service
```

The output should be similar to:



```
● ShowInfo.service - ShowInfo

  Loaded: loaded (/etc/systemd/system/ShowInfo.service; disabled; vendor preset: enabled)
  
  Active: active (running) since Fri 2020-09-11 15:17:16 CEST; 14s ago
  
Main PID: 1453 (python3)

  CGroup: /system.slice/ShowInfo.service
  
          └─1453 /usr/bin/python3 ShowInfo.py
          
Sep 11 15:17:16 eInk systemd[1]: Started ShowInfo.
```



If the service is running fine, you can enable it and reboot the Raspberry Pi to load it automatically during boot:

```
sudo systemctl enable ShowInfo.service
```

To stop the service:

```
sudo systemctl stop ShowInfo.service
```
