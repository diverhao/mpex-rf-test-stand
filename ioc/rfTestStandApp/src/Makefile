TOP=../..

include $(TOP)/configure/CONFIG
PROD_IOC = rfTestStand

DBD += rfTestStand.dbd
rfTestStand_DBD += base.dbd
rfTestStand_DBD += ether_ip.dbd

rfTestStand_SRCS += rfTestStand_registerRecordDeviceDriver.cpp
rfTestStand_SRCS_DEFAULT += rfTestStandMain.cpp
rfTestStand_SRCS_vxWorks += -nil-

rfTestStand_LIBS += ether_ip
rfTestStand_LIBS += $(EPICS_BASE_IOC_LIBS)

include $(TOP)/configure/RULES

