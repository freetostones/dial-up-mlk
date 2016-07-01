"""
Parser to find whether a Shapefile record contains the following substrings:
    ["martin luther", "mlk", "m.l.k"]

Call Command by:
  python mlk_parse.py {shapefiles to analyze}
"""

import shapefile
import sys


def main(args):
  """ Function to parse through shape files called in command line.

  Calls the find_mlk_streets function on every shapefile given in "args"

  Args:
    args: list of command line inputs
  """
  del args[0]  # arg for command name

  for state_shapefile in args:
    sf = shapefile.Reader(state_shapefile)
    mlk_streets = find_mlk_streets(sf)
    if mlk_streets:
      print mlk_streets
    else:
      print("State Shapefile returned no MLK streets")


def find_mlk_streets(shapefile_input):
  """ Uses the shapefile library to search for all "mlk" streets.

  Searches each street name field for a Martin Luther King substring

  Args:
    shapefile_input: The shapefile opened by the shapefile library

  Returns:
    List of [Street ID, Street Name] pairs that correspond to MLK streets
  """
  streets = []
  for record in shapefile_input.records():
    name = record[1].lower()  # Ignore capitalization errors
    if ('martin luther' in name) or ('mlk' in name) or ('m.l.k' in name):
      streets.append(record[0:2])
  return streets

if __name__ == '__main__':
  main(sys.argv)
