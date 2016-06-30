"""
Parser to find whether a Shapefile record contains the following substrings:
    ["martin luther", "mlk", "m.l.k"]
"""

import shapefile
import sys

def main(unused_args):
  sf = shapefile.Reader("shapefiles/roads")
  mlk_streets = find_mlk_streets(sf)
  print mlk_streets


def find_mlk_streets(shapefile_input):
  streets = []
  for record in shapefile_input.records():
    name = record[1].lower()  # Ignore capitalization errors
    if ('martin luther' in name) or ('mlk' in name) or ('m.l.k' in name):
      streets.append(record)
  return streets

if __name__ == "__main__":
  main(sys.argv)
