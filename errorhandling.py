# 2. Error Handling
# Building an Interface Alarm System (IAS) that shows the error messages if some failure happens.

def ias():
    num = input("Enter error code: ").strip()
    if not num.isdigit():
        print("Invalid input! Please enter integers.")
        return
    
    x = int(num)
    if x > 31:
        print("!!--Undetected errors--!!")
        return
    
    binary = format(x, '5b')
    error_msg = ["Container descent rate failure", "Science Payload descent rate failure", "Container position failure", "Science Payload position failure","Release failure"]
    
    error_y = []
    for i, bit in enumerate(binary):
        if bit == '1':
            error_y.append(error_msg[i])
    if not error_y:
        print("No error")
    else:
        print(", ".join(error_y))

ias()

# References:
# https://www.w3schools.com/python/default.asp
# https://pynative.com/python-convert-decimal-number-to-binary-and-vice-versa/
