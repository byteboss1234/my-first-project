try:
    num1 = float(input("පළමු අංකය ඇතුළත් කරන්න: "))
    num2 = float(input("දෙවැනි අංකය ඇතුළත් කරන්න: "))
    op = input("ගණිතමය ලකුණ ඇතුළත් කරන්න (+, -, *, /): ")

    if op == "+":
        print("පිළිතුර:", num1 + num2)
    elif op == "-":
        print("පිළිතුර:", num1 - num2)
    elif op == "*":
        print("පිළිතුර:", num1 * num2)
    elif op == "/":
        print("පිළිතුර:", num1 / num2)
    else:
        print("වැරදි ලකුණක්!")
except ZeroDivisionError:
    print("Error: 0 න් බෙදිය නොහැක!")
except ValueError:
    print("Error: කරුණාකර අංකයක් පමණක් ඇතුළත් කරන්න!")