__EPICS Environment for MPEX RF Test Stand__


This repo contains the EPICS environment for MPEX RF test stand, including EPICS base, Ethernet IP driver, EPICS IOC, and python scripts.

## Set up `pyepics`

```
cd python
python3 -m venv epics-venv
source epics-venv/bin/activate
python -m pip install --upgrade pip
pip install pyepics
```

## Set up EPICS

Go to the top folder of this repo.

```
cd epics-base
make
cd ../ether_ip
make
cd ../ioc
make
```

You can clean up the make by running

```
cd epics-base
make distclean
cd ../ether_ip
make distclean
cd ../ioc
make distclean
```


## Run EPICS IOC

The EPICS IOC folder is 

```
ioc
```

Run the IOC

```
cd ioc/iocBoot/iocrfTestStand
./st.cmd
```

## Run Python script

```
cd python
python3 meas01.py
```

Then you should see something like

```
test01 3.0 1782181319.868512
test01 4.0 1782181320.87212
test01 5.0 1782181321.87212
test01 6.0 1782181322.871884
test01 7.0 1782181323.872146
test01 8.0 1782181324.872189
```

on your screen.