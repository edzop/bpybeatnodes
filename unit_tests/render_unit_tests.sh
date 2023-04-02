#!/bin/bash
path="../"
searchpath=$path/$1*.blend

for f in $( ls $searchpath); do
    echo Processing: $f
    blender -b $f -P render_unit_tests.py
done


