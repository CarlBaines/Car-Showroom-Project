from json import dump, load  #imports
from time import sleep


makes = {'Mercedes', 'BMW', 'Ford', 'Mini'}                     #creates lists of car makes, models and colours that the car showroom will have in stock.
models = {'320D', 'Mustang', 'Focus', 'Cooper', 'A Class'}
colours = {'Red', 'Yellow', 'Black', 'Blue', 'White'}



try:
    with open('details.json', 'r') as file:    #opens a JSON file called 'details' and dumps the dictionary, still with its empty values, that was created above. This line of code is tested for errors.
        details = load(file)

except FileNotFoundError:
    details = {                 #executes this line of code which creates a dictionary with empty values except if the file cannot be found.
    "CustomerName": "",
    "CarMake": "",
    "CarModel": "",
    "CarColour": "",
}

    



#menu function.
def systemMenu():

    #display stock for the car showroom.
    print('')
    print('------------STOCK------------')
    print('Car Make  | Model   | Price ')
    print('')
    print('Mercedes  | A Class | £26,000')
    print('BMW       | 320D    | £30,000')
    print('Ford      | Focus   | £40,000')
    print('Mini      | Cooper  | £35,000')
    print('Ford      | Mustang | £45,000')
    print('------------------------------')
    print('')
    sleep(1.5)
    print('------------------------------Welcome to the Car Showroom system ------------------------------')
    print('Car Showroom System Menu\n 1. Input customer details into the system.\n 2. Search for existing customers. \n 3. Exit. ')
    print('---------------------------------------------')
    option = int(input('Please choose an option '))
    
    while option == 1 or option == 2 or option == 3:



        if option == 1:
           
           sleep(.5)

           while True:
                customerName = input('\nPlease enter the name of the customer ')

                if customerName.strip(): #I took this line of code from Google. This checks if the user input is not empty after it strips all whitespace.

                    details["CustomerName"] = customerName  #writes the user input to the empty value under the key 'CustomerName' in the dictionary made above.
                    break #exits the loop if a valid input is provided.
                else:
                    print('Please enter a valid customer name')

           sleep(.5)
           carMake = input('\nPlease enter the make of the car that the customer wants ')

           while carMake not in makes:  #the piece of code below loops until the user input is equal to something that is in the 'makes' list.
               print('The make you have entered is not in stock :(')
               carMake = input('\nPlease enter the make of the car that the customer wants ')
           else:
               details['CarMake'] = carMake
               
           sleep(.5)
           carModel = input('\nPlease enter the model of the car that the customer wants ')

           while carModel not in models:
                print('The model you have entered is not in stock or available :(')               #the same happens in these pieces of code for their to check that the user inputs are within the corresponding lists.
                carModel = input('\nPlease enter the model of the car that the customer wants ')
           else:
                details['CarModel'] = carModel

           sleep(.5)
           carColour = input('\nPlease enter the colour of the car that the customer wants ')

           while carColour not in colours:
                print('The colour you have entered is not in stock :(')
                carColour = input('\nPlease enter the colour of the car that the customer wants ')
           else:
                details['CarColour'] = carColour

           sleep(.5)



           with open('details.json', 'w') as file:
                dump(details, file, indent = 3)


           print('The summary below has been added to the database \n' + str(details))

           break #exits loop.

           


        #Part of the code that allows the user to search for details.
        if option == 2:
            print('--------------------------------------------------------------')
            print('')
            print('Car Showroom Search System \n\n 1. Search by customer details. \n 2. Search by car model \n 3. Display all data. \n 4. Exit.')
            print('')
            option2 = input('Please choose an option ')

            if option2 == "1":
                customerName = input('\nPlease enter the name of the customer you want to search for ')


                if details["CustomerName"] == customerName:
                    print('')     
                    print('This is the summary for ' + customerName + ':\n' + str(details))         #checks to see if the customer name value in the 'details' dictionary is equal to the one just inputted from the user.
                    break
                else:
                    print('No details found. Please search again')
    
    

            if option2 == '2':
                carMake = input('\nPlease enter the make of the car you want to search for the customer by ')
                if details["CarMake"] == carMake:
                    print('')
                    print('These are all of the details that are associated with the car model, ' + carMake + ':\n' + str(details)) 
                    print(details)
                    break
                else:
                    print('No details found. Please search again')
            


            if option2 == '3':
                with open('details.json', 'r') as file:
                    data = load(file)
                print(data)  #these lines of code open and read the JSON file with the modified dictionary and then output the data.
                break

            if option2 == '4':
                quit()





        if option == 3:
            quit()

    else:
        print('Please enter a valid option number')  #loops the code until a valid option number is entered on the starting menu.
        sleep(2)
        print('')
        print('')
        systemMenu()

systemMenu()