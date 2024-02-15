print("--------------------------------Welcome--------------------------------")

#Periodic Table
thisdict = {

   "hydrogen" : "H",
   "weight_H" : 1.0,
   "helium" : "He",
   "weight_He" : 4.0,
   "lithium" : "Li",
   "weight_Li" : 6.94,
   "beryllium" : "Be",
   "weight_Be" : 9.01,
   "boron" : "B",
   "weight_B" : 10.8,
   "carbon" : "C",
   "weight_C" : 12.01,
   "oxygen" : "O",
   "weight_O" : 16.0,

}

#Setting up the Equation
amount_of_reactant = int(input("How many reactants are present in the equation?: "))
amount_of_product = int(input("How many products are present in the equation?: "))

#Askings for reactants
if (amount_of_reactant is 1):

   first_reactant_coefficent = int(input("What is the coefficent on your first reactant?: "))
   first_reactant = (input("What compound is your first reactant?: "))
   print(str(first_reactant_coefficent) + "(" +first_reactant+ ").")


if (amount_of_reactant is 2):

   first_reactant_coefficent = int(input("What is the coefficent on your first reactant?: "))
   first_reactant = (input("What compound is your first reactant?: "))
   second_reactant_coefficent = int(input("What is the coefficent on your second reactant?: "))
   second_reactant = (input("What compound is your second reactant?: "))

if (amount_of_reactant is 3):

   first_reactant_coefficent = int(input("What is the coefficent on your first reactant?: "))
   second_reactant_coefficent= int(input("What is the coefficent on your second reactant?: "))
   third_reactant_coefficent = int(input("What is the coefficent on your third reactant?: "))

if (amount_of_reactant is 4):

   first_reactant_coefficent = int(input("What is the coefficent on your first reactant?: "))
   second_reactant_coefficent = int(input("What is the coefficent on your second reactant?: "))
   third_reactant_coefficent = int(input("What is the coefficent on your third reactant?: "))
   fourth_reactant_coefficent = int(input("What is the coefficent on your fourth reactant?: "))
  
#Askings for products
if (amount_of_product is 1):

   first_product_coefficent = int(input("What is the coefficent on your first product?: "))
   first_product = (input("What compound is your first product?: "))

if (amount_of_product is 2):

   first_product_coefficent = int(input("What is the coefficent on your first product?: "))
   first_product = (input("What compound is your first product?: "))
   second_product_coefficent = int(input("What is the coefficent on your second product?: "))
   second_product = (input("What compound is your second product?: "))

if (amount_of_product is 3):

   first_product_coefficent = int(input("What is the coefficent on your first product?: "))
   second_product_coefficent= int(input("What is the coefficent on your second product?: "))
   third_product_coefficent = int(input("What is the coefficent on your third product?: "))

if (amount_of_product is 4):

   first_product_coefficent = int(input("What is the coefficent on your first product?: "))
   second_product_coefficent = int(input("What is the coefficent on your second product?: "))
   third_product_coefficent = int(input("What is the coefficent on your third product?: "))
   fourth_product_coefficent = int(input("What is the coefficent on your fourth product?: "))

