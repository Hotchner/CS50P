from PIL import Image
import sys, os

# for infile in sys.argv[1:]:
#     f, e = os.path.splitext(infile)
#     outfile = f + ".jpg"
#     if infile != outfile:
#         try:
#             with Image.open(infile) as im:
#                 im.save(outfile)
#         except OSError:
#             print("cannot convert", infile)


fotos = ["before1.jpg", "before2.jpg", "before3.jpg"]

for _ in fotos:
    objeto, formato = os.path.splitext(_)
    outfile = objeto + ".jpeg"
    if _ != outfile:
        try:
            with Image.open(_) as im:
                im.save(outfile)
        except OSError:
            print("Cannot convert")