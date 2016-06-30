import shapefile
print('Opening file')
sf = shapefile.Reader("shapefiles/roads")

mlk_streets = []

for record in sf.records():
    name = record[1].lower()
    if ('martin luther' in name) or ('mlk' in name) or ('m.l.k' in name):
        mlk_streets.append(record)

print(mlk_streets)
