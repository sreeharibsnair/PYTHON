import rectangle
import circle
while True:
    print("\n1. Rectangle\n2. Circle\n3. Exit")
    ch=int(input("Enter your choice: "))
    if ch==1:
        l=int(input("Enter length: "))
        b=int(input("Enter breadth: "))
        rectangle.rectarea(l,b)
        rectangle.rectperi(l,b)
    elif ch==2:
        r=int(input("Enter radius: "))
        circle.circlearea(r)
        circle.circleperi(r)
    elif ch==3:
        print("Exiting...")
        break
    else:
        print("Invalid choice")