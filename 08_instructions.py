# functions

# Checks that user has entered yes / no to a question
def yes_no(question):

    to_check = ["yes", "no"]

    valid = False
    while not valid:

        response = input(question).lower()

        for var_item in to_check:
            if response == var_item:
                return response
            elif response == var_item[0]:
                return var_item

        print("Please enter either yes or no...\n")


# show instructions
def show_instructions():

    print('''\n
***** Instructions *****

This program will ask you for...
- The name of the product you are selling
- How many items you plan on selling
- The cost for each component of the product
- How much money you want to make

It will then output an itemised list of the costs
with subtotals for the variable and fixed costs.
Finally it will tell you how much you should sell 
each item for to reach your profit goal.

The data will also be written to a text file which has
the same name as your product.

**** Program launched! ****''')


# Main routine
print("****** Welcome to the Fund Raising Calculator ******")
want_instructions = yes_no("\nHave you used this program before? ")

if want_instructions == "no":
    show_instructions()
else:
    print("\n**** Program launched! ****")
