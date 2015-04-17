#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
***************************************************************************
    propertize.py

    Transform all methods without arguments and that do return something
    into properties for the given input class or module

    ---------------------
    Date                 : April 2015
    Copyright            : (C) 2015 by Alessandro Pasotti (ItOpen)
    Email                : apasotti at gmail dot com
***************************************************************************
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU General Public License as published by  *
*   the Free Software Foundation; either version 2 of the License, or     *
*   (at your option) any later version.                                   *
*                                                                         *
***************************************************************************
"""

__author__ = 'Alessandro Pasotti'
__date__ = 'April 2015'
__copyright__ = '(C) 2015, Alessandro Pasotti'


import inspect

def propertize(cls, prefix='p_', quiet=True):
    """Transform all methods without arguments and that do return something into
    properties for the given input class or module, an optional prefix
    (defaults to _p) is added to the property so that the original function is
    still available"""
    def _cls_propertize(cls, prefix, quiet):
        for k,v in inspect.getmembers(cls):
            if k.find('__') == -1 \
                    and inspect.isroutine(v) \
                    and inspect.getdoc(v) \
                    and inspect.getdoc(v).find('()') != -1 \
                    and inspect.getdoc(v).find('->') != -1:
                attr_name = prefix + k
                setattr(cls, attr_name, property(getattr(cls, k)))
                if not quiet:
                    print 'Propertized %s' % attr_name

    if  inspect.ismodule(cls):
        for k,v in inspect.getmembers(cls):
            if k.find('__') == -1 \
                    and inspect.isclass(v):
                _cls_propertize(v, prefix, quiet)
    elif inspect.isclass(cls):
        _cls_propertize(cls, prefix, quiet)

