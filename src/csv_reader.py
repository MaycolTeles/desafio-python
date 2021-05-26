#!/usr/bin/env python
# coding: utf-8

# In[57]:


import csv

class File():
    '''
    Class to represent a generic file.
    '''
    
    __FILE_PATH = None
    
    __PARAMETERS = None
    
    __DATA = []
    
    __FINAL_DATA = {}
    
    
    def __init__(self, file_name="transportadoras.csv"):
        '''
        Constructor.
        '''
        
        self.__FILE_PATH = file_name
        
        
    def execute(self):
        '''
        Method to execute all the script functions.
        '''
        
        # DOING THE SETUP
        self.__open_file()
        
        
        # GETTING USER INPUT
        city, weight = self.__get_user_input()
        
        
        # DOING THE ANALYSIS
        self.__analyze_data(city, weight)
        
        
        # PRINTING THE INFORMATIONS
        self.__print_infos()
        
        
        
        
    def __open_file(self):
        '''
        Method to open the csv file.
        '''
        
        
        # OPENING THE FILE
        with open(self.__FILE_PATH, "r") as csv_file:
            
            csv_reader = csv.reader(csv_file)


            for line in csv_reader:
                
                # Saving the parameters
                if self.__PARAMETERS is None:
                    self.__PARAMETERS = line      

                    
                # Saving the data
                else:
                    dictionary = {}

                    for idx in range( len(line) ):    
                        dictionary[ self.__PARAMETERS[idx] ] = line[idx]

                    self.__DATA.append(dictionary)
                    
                    
    
    def __get_user_input(self):
        '''
        Method to get the input from the user and return it.
        @Return: The city to be delivered; The package's weight.
        '''
    
        city_id = self.__PARAMETERS[3]
    
        found_city = False

        while found_city is False:
            city = input("Which city would you like to send your package to? ").lower()

            for dictionary in self.__DATA:
                if dictionary[ city_id ] == city.title():
                    found_city = True



        weight = input("How much is the weight of your package? ")

        return city.title(), weight
    
    
    
    
    def __analyze_data(self, city, weight):
        '''
        Method to analyze the readed data from the csv file.
        @Receive: The city; The weight.
        '''
        
        city_id = self.__PARAMETERS[3]
    
        # FLAGS
        lowest_price = 999
        fastest_time = 999

        weight = int(weight)
        
        for dictionary in self.__DATA:

            if city in dictionary.values():

                if weight < 100:
                    price_for_distance = float( dictionary[ self.__PARAMETERS[1] ].replace("R$ ", "") )
                
                else:
                    price_for_distance = float( dictionary[ self.__PARAMETERS[2] ].replace("R$ ", "") )


                price = weight * price_for_distance
                
                carrier = dictionary[ self.__PARAMETERS[0] ]
                destiny = city
                time = int( dictionary[ self.__PARAMETERS[4] ].replace("h", "") )

                    
                if price < lowest_price:
                    self.__FINAL_DATA["LOWEST"] = {"Carrier": carrier, "City": destiny, "Weight": weight, "Time": time, "Price": price}
                    lowest_price = price
                    
                    
                if time < fastest_time:
                    self.__FINAL_DATA["FASTEST"] = {"Carrier": carrier, "City": destiny, "Weight": weight, "Time": time, "Price": price}
                    fastest_time = time
                    
                    
    def __print_infos(self):
        '''
        Method to print all the gotten informations.
        '''
        
        print("\n***********************************\n")
        
        # PRINTING THE LOWEST COST
        for data in self.__FINAL_DATA:

            print()
            print("To ship your package, the ", data, " option is: ")
            print()
            print("Carrier: ", self.__FINAL_DATA[data]["Carrier"], ";")
            print("Destination city is: ", self.__FINAL_DATA[data]["City"], ";")
            print("Your package's weight is: ", self.__FINAL_DATA[data]["Weight"], " [Kg];")
            print("The shipment time is about: ", self.__FINAL_DATA[data]["Time"], " hours;")
            print("And the price is: R$", self.__FINAL_DATA[data]["Price"])
            print()


# In[58]:


csv_file = File()

csv_file.execute()


# In[ ]:




