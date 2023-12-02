#!/bin/bash

cat input.txt | sed -r -e 's/[^0-9]*//g' | sed -r -e 's/(.)(.*)(.)/\1\3/' | sed -r -e 's/^(.)$/\1\1/' | awk '{sum += $1 } END {print sum}'
