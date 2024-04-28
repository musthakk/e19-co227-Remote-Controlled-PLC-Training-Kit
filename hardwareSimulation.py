from pyfirmata import Arduino, OUTPUT, PWM
import time

# functions...
def HighDigitalIn(pin, state):
    board.digital[pin].write(0)
    state = 1
    return state

def LowDigitalIn(pin, state):
    board.digital[pin].write(1)
    state = 0
    return state

def IncreaseAnalogIn(pin, state):
    
    for i in range(11):
        board.digital[pin].write(i/10.00)
        time.sleep(0.2)
    state = 1
    return state

def DecreaseAnalogIn(pin, state):
    
    for i in range(11):
        board.digital[pin].write(1- i/10.00)
        time.sleep(0.2)
    state = 0
    return state

board = Arduino('COM7')

# define digital output pins./ Digintal Inputs of the PLC (DIn)
DIn_1 = 7
DIn_2 = 6
DIn_3 = 5
DIn_4 = 4


# declare ouputs..
board.digital[DIn_1].mode = OUTPUT
board.digital[DIn_2].mode = OUTPUT
board.digital[DIn_3].mode = OUTPUT
board.digital[DIn_4].mode = OUTPUT

# Initially set the digital outs to HIGH, because relay we have used by default gets on. HIGH signal turns the relay off
board.digital[DIn_1].write(1)
board.digital[DIn_2].write(1)
board.digital[DIn_3].write(1)
board.digital[DIn_4].write(1)
 
 
# define analog output pins./ Analog Inputs of the PLC (AIn)
AIn_1 = 9
AIn_2 = 10
AIn_3 = 11


# declare outputs..
board.digital[AIn_1].mode = PWM
board.digital[AIn_2].mode = PWM
board.digital[AIn_3].mode = PWM

# digital input active states...
DIn_1_active = 0
DIn_2_active = 0
DIn_3_active = 0
DIn_4_active = 0

# analog input active states..
AIn_1_active = 0
AIn_2_active = 0
AIn_3_active = 0

while True:
    print("********************************")
    print("********Control Pannel**********")
    print("1. Control Digital Inputs")
    print("2. Control Analog Inputs ")
    print("3. Exit")
    print("********************************\n")
    
    try:
        option = int(input("Choose your option: ")) # give your option as 1 or 2 or 3
    except:
        print("option should be numeric type\n")
        continue
    
    if (option == 1):
        
        while True:
            print("\n........................................")
            print("********Control Digital Inputs**********")
            print("........................................")
            print("1. High Digital Input (1)")
            print("2. High Digital Input (2)")
            print("3. High Digital Input (3)")
            print("4. High Digital Input (4)")
            print("........................................")
            print("5. Low Digital Input (1)")
            print("6. Low Digital Input (2)")
            print("7. Low Digital Input (3)")
            print("8. Low Digital Input (4)")
            print("9. Back")
            print("........................................\n")
            
            try:
                Selection = int(input("Choose your selection: ")) # give your selection as 1 or 2 or 3
            except:
                print("selection should be numeric type\n")
                continue
            
            # High Input 1
            if (Selection == 1):
                if(DIn_1_active == 0):
                    DIn_1_active = HighDigitalIn(DIn_1, DIn_1_active)
                else:
                    print("Input port 1 is already *ACTIVATED*")
                    continue
            # High Input 2
            elif (Selection == 2):
                if (DIn_2_active == 0):
                    DIn_2_active = HighDigitalIn(DIn_2, DIn_2_active)
                else:
                    print("Input port 2 is already *ACTIVATED*")
                    continue
            # High Input 3
            elif (Selection == 3):
                if (DIn_3_active == 0):
                    DIn_3_active = HighDigitalIn(DIn_3, DIn_3_active)
                else:
                    print("Input port 3 is already *ACTIVATED*")
                    continue
            # High Input 4
            elif (Selection == 4):
                if(DIn_4_active == 0):
                    DIn_4_active = HighDigitalIn(DIn_4, DIn_4_active)
                else:
                    print("Input port 4 is already *ACTIVATED*")
                    continue
            
            
            # Low Input 1
            elif (Selection == 5):
                if (DIn_1_active == 1):
                    DIn_1_active = LowDigitalIn(DIn_1, DIn_1_active)
                else:
                    print("Input port 1 is already *DEACTIVATED*")
                    continue
            # Low Input 2
            elif (Selection == 6):
                if (DIn_2_active == 1):
                    DIn_2_active = LowDigitalIn(DIn_2, DIn_2_active)
                else:
                    print("Input port 2 is already *DEACTIVATED*")
                    continue
            # Low Input 3
            elif (Selection == 7):
                if (DIn_3_active == 1):
                    DIn_3_active = LowDigitalIn(DIn_3, DIn_3_active)
                else:
                    print("Input port 3 is already *DEACTIVATED*")
                    continue
            # High Input 4
            elif (Selection == 8):
                if (DIn_4_active == 1):
                    DIn_4_active = LowDigitalIn(DIn_4, DIn_4_active)
                else:
                    print("Input port 4 is already *DEACTIVATED*")
                    continue
            
            # Back
            elif (Selection == 9):
                print("Back to the Control panel.")
                break
            else:
                print("Invalid Selection")
                continue
            
    elif (option == 2):
        
        while True:
            print("\n........................................")
            print("********Control Analog Inputs**********")
            print("........................................")
            print("1. Increase Analog Input (1)")
            print("2. Increase Analog Input (2)")
            print("3. Increase Analog Input (3)")
            print("........................................")
            print("4. Decrease Analog Input (1)")
            print("5. Decrease Analog Input (2)")
            print("6. Decrease Analog Input (3)")
            print("7. Back")
            print("........................................\n")
            
            try:
                Selection = int(input("Choose your selection: ")) # give your selection as 1 or 2 or 3
            except:
                print("selection should be numeric type\n")
                continue
            
            # High Input 1
            if (Selection == 1):
                if(AIn_1_active == 0):
                    AIn_1_active = IncreaseAnalogIn(AIn_1, AIn_1_active)
                else:
                    print("Input port 1 is already *INCREASED*")
                    continue
            # High Input 2
            elif (Selection == 2):
                if(AIn_2_active == 0):
                    AIn_2_active = IncreaseAnalogIn(AIn_2, AIn_2_active)
                else:
                    print("Input port 2 is already *INCREASED*")
                    continue
            # High Input 3
            elif (Selection == 3):
                if(AIn_3_active == 0):
                    AIn_3_active = IncreaseAnalogIn(AIn_3, AIn_3_active)
                else:
                    print("Input port 3 is already *INCREASED*")
                    continue
            
            
            # Low Input 1
            elif (Selection == 4):
                if (AIn_1_active == 1):
                    AIn_1_active = DecreaseAnalogIn(AIn_1, AIn_1_active)
                else:
                    print("Input port 1 is already *DECREASED*")
                    continue
            # Low Input 2
            elif (Selection == 5):
                if(AIn_2_active == 1):
                    AIn_2_active = DecreaseAnalogIn(AIn_2, AIn_2_active)
                else:
                    print("Input port 2 is already *DECREASED*")
                    continue
            # Low Input 3
            elif (Selection == 6):
                if(AIn_3_active == 1):
                    AIn_3_active = DecreaseAnalogIn(AIn_3, AIn_3_active)
                else:
                    print("Input port 3 is already *DECREASED*")
                    continue
            
            # Back
            elif (Selection == 7):
                print("Back to the Control panel.")
                break
            else:
                print("Invalid Selection")
                continue
        
    elif (option == 3):
        print("Exit...")
        break
    else:
        print("Invlid option")
        continue

    