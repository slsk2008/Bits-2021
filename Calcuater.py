print("                                                                                               ❗❗❗Calculater by Sakul Kumara❗❗❗                                                                            ")
print("                     ")
print("                     ")
print(" ※ Modes")
print("                     ")
print("a- Standard")
print("b - Odd or Even")
print("c - Programmer")
print("d - Area of shapes")
print("                     ")

c=str(input("Enter the letter of mode you want:-  "))

if (c== 'a'):
      first_number = input("Enter your first number:-   ")
      operation  = str(input("Enter the sum ( +,-,/,*):-   "))
      second_number = input("Enter your second  number:-  ")
      
      if (operation == '+'):
          output = first_number+second_number
          
      elif (operation == '-'):
          output = first_number-second_number
          
      elif (operation == '*'):
          output = first_number*second_number
          
      elif (operation == '/'):
          output = first_number/second_number
                 
      print("Answer:-   ",output)

elif(c== 'b'):
    
    print("                     ")
    n= int(input("Enter the number:-  "))

    if(n%2==1):
        print("odd")

    else:
        print("even")

elif(c== 'c'):
    print("                     ")
    print(" ※ Mode")
    print(" t - Binary")
    print(" u - Decimal")
    print(" v - Octal")
    print(" w - Hexadecimal")
    print("                     ")
    z = str(input("Enter letter of mode:- "))

    if(z=='t'):
        binary = int(input("Enter Value: "))
        print("Octal = ", oct(binary))
        print("Hex = ", hex(binary))

    elif(z=='u'):
         demicimal = int(input("Enter Value:- "))
         print("Binary = ", bin(demicimal))
         print("Octal = ", oct(demicimal))
         print("Hex = ", hex(demicimal))
         
    elif(z=='v'):
         octal = int(input("Enter Value:-  "))
         print("Binary = ", bin(octal))
         print("Hex= ", hex(octal))
         
    elif(z=='w'):
        hexadicimal= input("Enter Value:-  ")
        print("Binary = ", bin(hexadicimal))
        print("Octal= ", oct(hexadicimal))

    else:
        print("Please Reviwe letter of mode")

        
          
elif(c== 'd'):
    print("※Shapes")
    print("                     ")
    print("aaa - Circle")
    print("bbb - Square")
    print("ccc - Triangle")
    print("fff - Rectangle")
    print("                     ")
    q = str(input("Enter the letters of shape you want:- "))
    
    if(q=='bbb'):
            Square = int(input("Enter the Length of side:- "))
            print("cm[k], m[l],km[m]")
            lrn = input("Enter the number of Unit:- ")
            if(lrn == 'k'):
                 print(Square*Square,lrn,"cm2")
           
            elif(lrn == 'l'):
                print(Square*Square,lrn,"m2")

            elif(lrn == 'm'):
                print(Square*Square,"km2")

            else:
                print("Please Reviwe letter of mode")

   
            
            
            
