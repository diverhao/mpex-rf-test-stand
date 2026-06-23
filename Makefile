
TOP = .

SUBDIRS := epics-base ioc ether_ip
APP_DISTCLEAN_SUBDIRS := ioc ether_ip
DISTCLEAN_SUBDIRS := $(APP_DISTCLEAN_SUBDIRS) epics-base
DISTCLEAN_TARGETS := $(DISTCLEAN_SUBDIRS:%=distclean-%)
EPICS_HOST_ARCH ?= $(shell perl epics-base/src/tools/EpicsHostArch.pl)
EPICS_BASE_TOOLS := $(abspath epics-base/src/tools)
export EPICS_HOST_ARCH

.PHONY: all $(SUBDIRS) distclean $(DISTCLEAN_TARGETS)

all: $(SUBDIRS)

distclean: $(DISTCLEAN_TARGETS)

distclean-epics-base: $(APP_DISTCLEAN_SUBDIRS:%=distclean-%)
	$(MAKE) -C epics-base distclean

$(APP_DISTCLEAN_SUBDIRS:%=distclean-%):
	$(MAKE) -C $(@:distclean-%=%) distclean CVSCLEAN=$(EPICS_BASE_TOOLS)/cvsclean.pl DEPCLEAN=$(EPICS_BASE_TOOLS)/depclean.pl

$(SUBDIRS):
	$(MAKE) -C $@
