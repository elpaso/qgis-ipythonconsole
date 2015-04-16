# Makefile for a PyQGIS plugin

all: compile

dist: package

install: copy2qgis

PY_FILES = IPyConsole.py __init__.py
EXTRAS = icon.png
#UI_FILES = Ui_IPyConsole.py
                                                                                                                                                                                                                                                                                                                                                                                                               RESOURCE_FILES = resources.py

compile: $(UI_FILES) $(RESOURCE_FILES)

%.py : %.qrc
	pyrcc4 -o $@  $<

%.py : %.ui
	pyuic4 -o $@ $<



clean:
	find ./ -name "*.pyc" -exec rm -rf \{\} \;
	rm -f ../IPyConsole.zip
	rm -f Ui_IPyConsole.py resources.py

package:
	cd .. && find IPyConsole/  -print|grep -v Make | grep -v zip | grep -v .git | zip IPyConsole.zip -@

localrepo:
	cp ../IPyConsole.zip ~/public_html/qgis/IPyConsole.zip

copy2qgis: package
	unzip -o ../IPyConsole.zip -d ~/.qgis/python/plugins

check test:
	@echo "Sorry: not implemented yet."
