"""
Copyright (c) 2024 Tomi Bilcu. All rights reserved.

This work is licensed under the terms of the MIT license.  
For a copy, see LICENSE.txt.
"""

import cv2
from pyzbar.pyzbar import decode
from fetch_product import fetch_product


def read_barcode(source):

    detectedBarcodes = decode(source)  # source is in opencv format


    if detectedBarcodes:

          # Traverse through all the detected barcodes in image
        for barcode in detectedBarcodes: 
           
            # Locate the barcode position in image
            (x, y, w, h) = barcode.rect
             
            # Put the rectangle in image using
            # cv2 to highlight the barcode
            cv2.rectangle(source, (x-10, y-10),
                          (x + w+10, y + h+10),
                          (255, 0, 0), 2)
             
            if barcode.data != "":
               
                # Print the barcode data
                print(barcode.data)
                print(barcode.type)
                print( fetch_product((barcode.data).decode()) )


    if __name__ == "__main__":
        cv2.imshow("Image", source)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        return source, len(detectedBarcodes)


# testing manually if works
if __name__ == "__main__":
    image="Img.jpg"
    read_barcode(image)