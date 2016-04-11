# -*- coding: utf-8 -*-
"""
***************************************************************************
   qgswps.py QGIS Web Processing Service Plugin
  -------------------------------------------------------------------
 Date                 : 09 November 2009
 Copyright         : (C) 2009 by Dr. Horst Duester
 email                : horst dot duester at kappasys dot ch

  ***************************************************************************
  *                                                                         *
  *   This program is free software; you can redistribute it and/or modify  *
  *   it under the terms of the GNU General Public License as published by  *
  *   the Free Software Foundation; either version 2 of the License, or     *
  *   (at your option) any later version.                                   *
  *                                                                         *
  ***************************************************************************
"""
def name():
  return "WPS-Client"
  
def description():
  return "Client for Web Processing Services"

def version():
  return "2.1.5"

def qgisMinimumVersion():
  return "1.5"  
  
def qgisMaximumVersion():
  return "2.99"    

def date():
    return '2016-04-11'
    
def email():
    return 'horst.duester@sourcepole.ch'
    
def author():
  return "Dr. Horst Duester / Sourcepole AG Zurich"
  
def icon():
	return "images/wps-add.png"   

def homepage():
  return "https://github.com/sourcepole/qgis-wps-client"
  
def classFactory(iface):
  from qgswps import QgsWps
  return QgsWps(iface)  
