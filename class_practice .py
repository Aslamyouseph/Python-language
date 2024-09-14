class bank:
    def __init__(self,name):
        self.name=name
    def withdrawl(self):
        dep=int(input("Enter the deposit amound of your accound : "))
        cont=True
        while cont:
            actual_pin=33333
            wit=int(input("Enter the withdrawl amound : "))
            pin=int(input("Enter the pin number "))
            if(actual_pin==pin):
                if(wit>dep):
                    print("\n")
                    print(f"sorry {self.name} You have not able to acces this amound : ")
                    print(f"Your bank balance is {dep}")
                    cont=False
                    print("\n")
                else:
                    print("\n")
                    print(f"congratulation {self.name} you can withraw you amound ")
                    print(f"pleas collect your amount  {wit}")
                    dep=dep-wit
                    print(f"Your bank balance is {dep}")
                    print("\n")
            else:
                print(f"Sorry {self.name} your pin number is wrong ")
            
            


name=input("Enter your name : ")
b=bank(name)
b.withdrawl()