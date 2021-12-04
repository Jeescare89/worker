
class Workers:
    
    # This is the class varaible
    count_of_workers=0
    
    # this initiazilates the data members
    def __init__(self, ID, name):
        # creating instant variables
        self.__ID= ID
        self.__name= name
        Workers.count_of_workers += 1
    
    # method to get the ID
    def get_ID(self):
        return self.__ID
    
    # method that returns the name
    def get_name(self):
        return self.__name
    
    # method that returns the ID
    def set_ID(self, ID):
        self.__ID= ID
        
    # method to get the name
    def set_name(self, name):
        self.__name= name
        
    # displays the method to print out the workers ID
    def display_info(self):
        print("Workers ID:", self.get_ID())
        print("Workers Name:", self.get_name())
        
    # displays the method to print out the number of workers
    def print_number_of_workers(self):
        print("The total number of Workers:", Workers.count_of_workers)



# main function
def main():
    
    # creates the two working object (Joshua) and (Sam)
    e1= Workers(1, 'Joshua')
    e2= Workers(2, 'Sam')
    
    # prints the name of the first worker
    print("Workers ID of e1:", e1.get_ID())
    
    # sets the Id using a setter method for 1
    e1.set_ID(3)
    
    # prints the id of 1 again
    print("Workers ID of e1:", e1.get_ID())
    
    # prints the information of the first worker
    print("\n**Info of w1**")
    e1.display_info()
    
    print() # prints new line
    
    # printing the total number of employees
    e1.print_number_of_workers()
    
main()