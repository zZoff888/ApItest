import ddddocr
class codedemo():
    def ddddddor(filename):
        ocr = ddddocr.DdddOcr()
        with open(f'/Users/mac/Desktop/blt/APItest/Data/{filename}', 'rb') as f:
            img_bytes = f.read()
        res = ocr.classification(img_bytes)
        # print(res)
        return res
if __name__ == '__main__':
    codedemo.ddddddor(r'1.jpg')