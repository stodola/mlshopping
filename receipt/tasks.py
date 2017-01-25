#from __future__ import absolute_import, unicode_literals
from celery.decorators import task

from .models import Paragon, ParagonItems
import pytesseract
from PIL import Image, ImageFilter
from .image_utils import to_text

@task(name='tessaract_in_action')
def items_from_image(image):
    hj=Paragon.objects.get(image=image)
    dane = pytesseract.image_to_string(Image.open(hj.image.path), lang='pol')
    dane2 = to_text(dane)
    for i,j in dane2:
        p=ParagonItems(id_paragonu=hj, cena =j, produkt=i)
        p.save()
    hj.image_data = dane2
    hj.save()



