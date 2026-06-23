
TOP = .

SUBDIRS := epics-base ioc ether_ip

.PHONY: all $(SUBDIRS)

all: $(SUBDIRS)

$(SUBDIRS):
	$(MAKE) -C $@
