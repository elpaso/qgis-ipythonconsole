# Makefile for a PyQGIS plugin

all: compile

dist: package

install: copy2qgis

# QGIS3 default
QGISDIR=.local/share/QGIS/QGIS3/profiles/default

PY_FILES = IPyConsole.py __init__.py
EXTRAS = icon.png settings.svg
#UI_FILES = Ui_SettingsDialog.py
#RESOURCE_FILES=resources_rc.py

compile: $(UI_FILES) $(RESOURCE_FILES)

%_rc.py : %.qrc
	pyrcc5 -o $@  $<

%.py : %.ui
	pyuic5 -o $@ $<


builddeps:
	@if [ ! -d "./ext-libs" ]; then \
		mkdir ./ext-libs; \
		pip install --target=./ext-libs -r requirements.txt; \
	fi

build: builddeps


deploy: build
	ln -s `pwd` $(HOME)/$(QGISDIR)/python/plugins/ipyconsole

clean:
	find ./ -name "*.pyc" -exec rm -rf \{\} \;
	rm -f ../IPyConsole.zip
	rm -f Ui_IPyConsole.py resources_rc.py

package:
	cd .. && if \[ -f IPyConsole.zip \] ; \
	then \
     	rm IPyConsole.zip ; \
	fi;
	cd .. && find IPyConsole/  -print|grep -v Make |grep -v run* | grep -v .pyc | grep -v zip | grep -v vscode | grep -v .git | zip IPyConsole.zip -@

localrepo:
	cp ../IPyConsole.zip ~/public_html/qgis/IPyConsole.zip

copy2qgis: package
	unzip -o ../IPyConsole.zip -d ~/.qgis/python/plugins

check test:
	@echo "Sorry: not implemented yet."
