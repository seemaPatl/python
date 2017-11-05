def pyramid(symbol):
     '''
     objective: to print a pyramid
     approach: print several lines of symbols
     '''
     print ('   ',symbol)
     print('  ',symbol,'',symbol)
     print(' ',symbol,'',symbol,'',symbol)
    
def main():
     '''
     objective: to print a pyramid
     approach: to use the function pyramid
     '''
     symbol=input('enter symbol: ')
     pyramid(symbol)
     print ('End of Function')
      
if __name__=='__main__':
     main()
     print ('End of Program')
