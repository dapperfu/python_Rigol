#!/bin/bash
SOURCE=rigol

# Windows
find ${SOURCE} -name "*.py" | xargs -n1 -P8 dos2unix
# Formatting
find ${SOURCE} -name "*.py" | xargs -n1 -P8 pyupgrade --py37-plus
find ${SOURCE} -name "*.py" | xargs -n1 -P8 reorder-python-imports --py37-plus
find ${SOURCE} -name "*.py" | xargs -n1 -P8 black --target-version py37

