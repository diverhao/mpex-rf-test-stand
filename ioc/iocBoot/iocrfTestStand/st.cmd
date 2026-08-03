#!../../bin/darwin-aarch64/rfTestStand

#- SPDX-FileCopyrightText: 2005 Argonne National Laboratory
#-
#- SPDX-License-Identifier: EPICS

#- You may have to change rfTestStand to something else
#- everywhere it appears in this file

#< envPaths

## Register all support components
dbLoadDatabase "../../dbd/rfTestStand.dbd"
rfTestStand_registerRecordDeviceDriver(pdbbase) 

# drvEtherIP_init
# drvEtherIP_define_PLC "stepper_plc", "10.112.2.14", 0
# EIP_verbosity(10)

## Load record instances
dbLoadRecords("../../db/test01.db")

iocInit()

## Start any sequence programs
#seq sncrfTestStand,"user=1h7"
