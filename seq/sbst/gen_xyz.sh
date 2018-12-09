#!/bin/sh

PYTHON=python
#PYTHON=python3

Zs='7.4 8.3 9.4'

for Z in $Zs
do
    echo "$PYTHON sbst.py __ZZ__ $Z in.template > in.$Z"
    $PYTHON sbst.py __ZZ__ $Z in.template > in.$Z
done
