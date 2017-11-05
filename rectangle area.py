def areaRactangle(length , breadth):
    '''
        objective : to compute the area of the Ractangle
        input parameters : 
            length : Length of Ractangle 
            breadth : breadth of the Ractangle
        approach  : multiply length and breadth
        return value : area of Ractangle
    '''
    area=length * breadth
    return area

def main():    
    '''
        objective : to compute the area of the Ractangle
        user inputs : 
            length : Length of Ractangle 
            breadth : breadth of the Ractangle
        approach  : to use function areaRactangle()
        return value : area of Ractangle
    '''
    length = int(input("Enter Length of Ractangle: "))
    breadth =int(input("Enter Breadth of Ractangle: "))
    print('Length of Ractangle : ' ,length)
    print('Breadth of Ractangle : ' ,breadth)
    print('Area of Ractangle : ' , areaRactangle(length ,breadth))
    
if __name__ == '__main__':
    main()
print("End of the Program")
