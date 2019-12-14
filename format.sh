#!/bin/bash
SOURCE=rigol

find ${SOURCE} -name "*.py" | xargs -n1 -P8 pyupgrade --py37-plus
find ${SOURCE} -name "*.py" | xargs -n1 -P8 reorder-python-imports --py37-plus
find ${SOURCE} -name "*.py" | xargs -n1 -P8 black --target-version py37

