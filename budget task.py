class Budget:
    def __init__(self, food, clothing, Entertainment):
        self.food = food
        self.clothing = clothing
        self.entertainment = Entertainment
        self.amountFood = 2000
        self.amountClothing = 1000
        self.amountEntertainment = 1200


    """
    This is a budget class for Deposit
    """

    def depos(self):
        print("1. Depost for food")
        print("2. Deposit for clothing")
        print("3. Deposit for entertainment")
        selectedOption = int(input("Please select an option: \n"))

        if selectedOption==1:
            deposited =int(input(f'How much do you want to deposit for {self.food}? \n'))
            print(f'You have sucessfully deposited {deposited} for {self.food}!')
            self.amountFood = self.amountFood + deposited
            print(f"your current balance is {self.amountFood} ")
        elif selectedOption==2:
             deposited =int(input(f'How much do you want to deposit for {self.clothing}? \n'))
             print(f'You have sucessfully deposited {deposited} for {self.clothing}!')
             self.amountClothing = self.amountClothing + deposited
             print(f'Your balance is {self.amountClothing}')
        elif selectedOption==3:
             deposited = int(input(f'How much do you want to deposit for {self.entertainment}? \n'))
             print(f'You have sucessfully deposited {deposited} for {self.entertainment} ')
             self.amountEntertainment = self.amountEntertainment + deposited
             print(f'Your balance is {self.amountEntertainment}')
        else:
            print("You have selected the wrong option!")

    """
    This is a budget class for withdraw
    """


    def wit(self):
        print("1. Withdraw for food")
        print("2. Withdraw for clothing")
        print("3. Withdraw for entertainment")
        selectedOption = int(input("Please select an option: \n"))

        if selectedOption==1:
            withdraw =int(input(f'How much do you want to withdraw for {self.food}? \n'))
            print(f'You have sucessfully withdrew {withdraw} for {self.food}!')
            self.amountFood = self.amountFood - withdraw
            print(f'Your balance is {self.amountFood}')
        elif selectedOption==2:
             withdraw =int(input(f'How much do you want to withdraw for {self.clothing}? \n'))
             print(f'You have sucessfully withdrew {withdraw} for {self.clothing}!')
             self.amountClothing = self.amountClothing - withdraw
             print(f'Your balance is {self.amountClothing}')
        elif selectedOption==3:
             withdraw = int(input(f'How much do you want to withdraw for {self.entertainment}? \n'))
             print(f'You have sucessfully withdrew {withdraw} for {self.entertainment} ')
             self.amountEntertainment = self.amountEntertainment - withdraw
             print(f'Your balance is {self.amountEntertainment}')
        else:
            print("You have selected the wrong option!")
 

    def bal(self):
        
        print(f'Your current  balance  on Food is {self.amountFood}')
        print(f'Your current balance on Clothing {self.amountClothing}')
        print(f'Your current balance on Entertainment is {self.amountEntertainment}')

        
    def trans(self):
         print("Where do you want to transfer from? \n")
         print('1.Food')
         print('2.Clothing')
         print('3. Entertainment')
         Credit = int(input("Please select an option:"))

         print('Where to you want to transfer to? \n')
         print('1.Food')
         print('2.Clothing')
         print('3. Entertainment')
         Debit = int(input("Please select an option:"))

         Amount = int(input('How much do you wish to transfer? \n'))

         if Credit==1:            
            if Debit==2:

                self.amountClothing = self.amountClothing + Amount
                print(f'You have succesfully transfered {Amount}!')
                print(f'Your current balance of Clothing is {self.amountClothing}')
            elif Debit==3:
                self.amountEntertainment = self.amountEntertainment + Amount
                print(f'You have succesfully transfered {Amount}!')
                print(f'Your current balance of Clothing is {self.amountEntertainment}')

            else:
                exit()

         if Credit==2:
            if Debit==1:
                self.amountFood = self.amountFood + Amount
                print(f'You have succesfully transfered {Amount}!')
                print(f'Your current balance of Clothing is {self.amountFood}')
            elif Debit==3:
                self.amountEntertainment = self.amountEntertainment + Amount
                print(f'You have succesfully transfered {Amount}!')
                print(f'Your current balance of Clothing is {self.amountEntertainment}')

            else:
                exit()
        
         if Credit==3:
            if Debit==1:
                self.amountFood = self.amountFood + Amount
                print(f'You have succesfully transfered {Amount}!')
                print(f'Your current balance of Clothing is {self.amountFood}')
            elif Debit==2:
                self.amountClothing = self.amountClothing + Amount
                print(f'You have succesfully transfered {Amount}!')
                print(f'Your current balance of Clothing is {self.amountClothing}')

            else:
                exit()
        




          








person1= Budget(' Friedrice', 'blouse', 'Music')
person2 = Budget('Beans', 'Trouser', 'Drama')
person1.depos()
person1.wit()
person1.bal()
person1.trans()




    
