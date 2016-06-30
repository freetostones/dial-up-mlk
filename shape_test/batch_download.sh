#!/bin/bash
baseurl="http://www2.census.gov/geo/tiger/TIGER2015/PRISECROADS/tl_2015_"
endurl="_prisecroads.zip"
for i in `seq -w 1 10`;
do
  wget $baseurl$i$endurl
done
