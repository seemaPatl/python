def areaTriangle(length, height):
    '''
    objective:To compute the area of the triangle
    input parameters:
      length:length of the rectangle
      breadth:breadth of the triangle
    approach:multiplying length and heigth
    return value: area of the triangle
    '''
    area=(length*height)/2
    return area
    
def main():
    '''
    objective:To compute the area of the triangle
    user inputs:
      length:length of rectangle
      heigthh:heigth of triangle
    approach:use function areatriangle
    '''
    length=int(input('enter the length of triangle: '))
    heigth=int(input('enter the heigth of the triangle: '))
    print('id(length): ',id(length))
    print('id(heigth): ',id(heigth))
    print('id.(areaTriangle): ',id(areaTriangle))
    print('areaTriangle',areaTriangle)
    print('Length of triangle is: ',length)
    print('Height of triangle is: ',heigth)
    print('Area of the rectangle: ',areaTriangle(length, heigth))
    print('End of output')
    
if __name__=='__main__':
    main()
print('end of program')
