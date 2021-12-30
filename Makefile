PACKAGE := python-ovsdbg
VERSION := 0.0.13

sources:
	tar czf $(PACKAGE)-$(VERSION).tar.gz bin extras ovs_dbg README.md LICENSE setup.py setup.cfg

.PHONY: sources
