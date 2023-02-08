import ddddocr

# ocr = ddddocr.DdddOcr()
# with open('../../Data/1.jpg', 'rb') as f:
#     img_bytes = f.read()
# res = ocr.classification(img_bytes)
#
# print(res)
class codedemo():
    def ddddddor(filename):
        ocr = ddddocr.DdddOcr()
        with open(f'../../Data/{filename}', 'rb') as f:
            img_bytes = f.read()
        res = ocr.classification(img_bytes)
        print(res)
        return res
if __name__ == '__main__':
    codedemo.ddddddor(r'1.jpg')