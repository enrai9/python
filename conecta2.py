#!/usr/bin/python

import os
import sys

print "Usuario: "
usuario=raw_input()

print "Clave: "
password=raw_input()

print "Base de datos: "
bd=raw_input()

print "Nombre del archivo a comprimir : "
archivo=raw_input()

os.system('mysqldump -u ' + usuario + ' -p' + password + ' ' + bd + ' | gzip > ' + archivo +  '.sql.gz')

