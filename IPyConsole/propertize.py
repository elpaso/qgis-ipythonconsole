#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
***************************************************************************
    propertize.py

    More Pythonic bindings for the masses.
    Transform all methods of a class without arguments and that do return
    something into properties for the given input class or for all classes
    in the given module.

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
import functools
def propertize(cls, prefix='p_', quiet=True):
    """Transform all methods without arguments and that do return something into
    properties for the given input class or module, an optional prefix
    (defaults to p_) is added to the property so that the original function is
    still available"""

    def _cls_propertize(cls, prefix, quiet):

        def _caller(self, k):
            return getattr(self, k)()

        for k, v in inspect.getmembers(cls):
            if (k.find('__') == -1
                and inspect.isroutine(v)
                and inspect.getdoc(v)
                and inspect.getdoc(v).find('()') != -1
                and inspect.getdoc(v).find('->') != -1):
                attr_name = prefix + k

                # Works fine on bound virtual methods, doesn't work on
                # classmethods
                try:
                    setattr(cls, attr_name, property(functools.partial(_caller, k=k)))
                    if not quiet:
                        print('Propertized %s' % attr_name)
                except TypeError as e:
                    if not quiet:
                        print('Propertized failed for %s' % attr_name)

    if  inspect.ismodule(cls):
        if inspect.isbuiltin(cls):
            return
        for k, v in inspect.getmembers(cls):
            if (k.find('__') == -1
                and inspect.isclass(v)
                and str(v) != 'str'):
                _cls_propertize(v, prefix, quiet)
    elif inspect.isclass(cls):
        _cls_propertize(cls, prefix, quiet)




if __name__ == '__main__':
    # Tests #
    import unittest

    class Animal():
        @classmethod
        def whoami(cls):
            """ () -> """
            return 'Animal'
        def say(self):
            """ () -> """
            return 'sound'
        def move(self):
            """ () -> """
            return 'move'

    class Duck(Animal):
        @classmethod
        def whoami(cls):
            """ () -> """
            return 'Duck'
        def say(self):
            """ () -> """
            return 'quack'
        def move(self):
            """ () -> """
            return 'fly'

    class Dog(Animal):
        def eat(self):
            """ () -> """
            return 'meat'

    propertize(Animal)
    propertize(Dog)
    propertize(Duck)

    class TestInheritance(unittest.TestCase):

        def setUp(self):
            self.animal = Animal()
            self.duck = Duck()
            self.dog = Dog()

        def test_calls(self):
            self.assertEqual(self.animal.say(), 'sound')
            self.assertEqual(self.animal.move(), 'move')
            self.assertEqual(self.duck.say(), 'quack')
            self.assertEqual(self.duck.move(), 'fly')
            self.assertEqual(self.dog.say(), 'sound')
            self.assertEqual(self.dog.eat(), 'meat')
            self.assertEqual(self.dog.move(), 'move')

        def test_properties(self):
            self.assertEqual(self.animal.p_say, 'sound')
            self.assertEqual(self.animal.p_move, 'move')
            self.assertEqual(self.duck.p_say, 'quack')
            self.assertEqual(self.duck.p_move, 'fly')
            self.assertEqual(self.dog.p_say, 'sound')
            self.assertEqual(self.dog.p_eat, 'meat')
            self.assertEqual(self.dog.p_move, 'move')

        def test_raise(self):
            with self.assertRaises(AttributeError):
                self.duck.eat()

        def test_classmethods(self):
            self.assertEqual(self.animal.whoami(), 'Animal')
            self.assertEqual(self.animal.p_whoami, 'Animal')
            self.assertEqual(self.duck.whoami(), 'Duck')
            self.assertEqual(self.duck.p_whoami, 'Duck')


    # Now testing QGIS bindings: this is the hard part!
    from qgis import core
    class TestQGIS(unittest.TestCase):

        def setUp(self):
            propertize(core)


        def test_instance(self):
            self.assertEqual(core.QgsMapLayerRegistry.instance().mapLayers(), {})
            self.assertEqual(core.QgsMapLayerRegistry.instance().p_mapLayers, core.QgsMapLayerRegistry.instance().mapLayers())


    #from IPython import embed; embed()

    unittest.main()
