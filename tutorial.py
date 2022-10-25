import pylidc as pl

# Query for all CT scans with desired traits.
scans = pl.query(pl.Scan).filter(pl.Scan.slice_thickness <= 1,
                                 pl.Scan.pixel_spacing <= 0.6)
print(scans.count())
# => 31

pid = 'LIDC-IDRI-0078'
scan = pl.query(pl.Scan).filter(pl.Scan.patient_id == pid).first()

print(type(pl.Scan.slice_thickness))

print(len(scan.annotations))

nods = scan.cluster_annotations()
print("%s has %d nodules." % (scan, len(nods)))
# => Scan(id=1,patient_id=LIDC-IDRI-0078) has 4 nodules.

for i,nod in enumerate(nods):
    print("Nodule %d has %d annotations." % (i+1, len(nods[i])))
# => Nodule 1 has 4 annotations.
# => Nodule 2 has 4 annotations.
# => Nodule 3 has 1 annotations.
# => Nodule 4 has 4 annotations.



# TODO: data path should be set.
# vol = scan.to_volume()
# print(vol.shape)
# # => (512, 512, 87)

# print("%.2f, %.2f" % (vol.mean(), vol.std()))
# # => -702.15, 812.52