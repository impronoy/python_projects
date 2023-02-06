from datetime import datetime                                                                           # Importing datetime module to implement datetime class
import heapq                                                                                            # Importing heapq module to implement heap queue

# Start of class carRentalService
class carRentalService:

#############################################################################################################################################################################
    # function calculateCarsRequired to -
    # 1. read input values (start date and end date of rental) from file inputPS7.txt
    # 2. to extract the start date and end date of each car rental
    # 3. to create a single list with the extracted start date and end date & sort in ascending wise. 
    # 4. assuming we always have 1 car in hand, we check -
    #    - if new asked rental start date >= existing end date of prev. rental, then additional car req.
    #    - using properties of heap, we add a car if set condition is true
    # 5. write output values (no of cars required) into file outputPS7.txt
#############################################################################################################################################################################

    # Start of function calculateCarsRequired()
    def calculateCarsRequired():
        inputValues=[]                                                                                  # Array to store input values after reading from file
        cleanedInputValue=[]                                                                            # Array to store input values after removing trailing whitespaces from araay inputValues[]
        bookingPeriod=[]                                                                                # Array to store the input values after filtering any blank lines in the file, if encountered
        finalBookingPeriod=[]                                                                           # Array to store the input values in date format and not string in sorted order
        try:                                                                                            # try block to check for empty lines in file, if encountered
            inputFile = "inputPS7.txt"                                                                  # Accessing the input file
            with open(inputFile, 'r') as fileContents:                                                  # Opening the input file to read data feom inputFile
                inputValues = fileContents.readlines()                                                  # Reading the entire file and returning each line as a String element in a list
                for inputValue in inputValues:                                                          # Looping through 
                    val=inputValue.strip()                                                              # Trimming trailing whitespaces from each line
                    cleanedInputValue.append(val)                                                       # Storing the values in cleanedInputValue[] one after another
                    bookingPeriod=list(filter(''.__ne__,cleanedInputValue))                             # Making a list of the filtered & clean file cleanedInputValue[] in array bookingPeriod[]
        except FileNotFoundError:                                                                       # except block to catch error if exception FileNotFound occurs
            print("File Not Found")
            inputFile.close()                                                                           # File closed

        format = '%Y-%m-%d'                                                                             # '%Y-%m-%d' format to get the string to datetime

        for line in bookingPeriod:                                                                      # Iterating each line (time intervals) from the entire list
            """
            Description of dateStarted : stores the value of line.strip().split(',')[0]
            line.strip() - to remove all trailing white spaces from the beginning and end of the each line of the list
                    .split(',') - to split the string where delimeter ',' is encountered
                            [0] - line.strip().split(',') will only happen for the 1st index of every string
            """                                                                    
            try:                                                                                        # try block to check for escape sequences in startDate
                if(line!="/n"):
                    dateStarted = line.strip().split(',')[0]                                                                                                                              
                    extractedStartDate = datetime.strptime(dateStarted, format).date()                  # Converting string format to datetime by using the strptime() function
            except Exception:                                                                           # except block to catch exceptions, if generated in startDate and print message
                file = open("outputPS7.txt", "w")
                file.write("\nException generated while evaluating startDate.\n")
                file.write("\nProgram can't be executed further, please check and rectify input file inputPS7.txt.\n")
                file.close()
                exit(0)

            """
            Description of dateEnded : stores the value of line.strip().split(',')[1]
            line.strip() - to remove all trailing white spaces from the beginning and end of the each line of the list
                    .split(',') - to split the string where delimeter ',' is encountered
                            [1] - line.strip().split(',') will only happen for the 2st index of every string
            """ 
            try:                                                                                        # try block to check for escape sequences in endDate
                if(line!="/n"):
                    dateEnded = (line.strip().split(',')[1]).strip()
                    extractedEndDate = datetime.strptime(dateEnded, format).date()                      # Converting string format to datetime by using the strptime() function
            except Exception:                                                                           # except block to catch exceptions, if generated in endDate and print message
                file = open("outputPS7.txt", "w")
                file.write("\nException generated while evaluating endDate.\n")
                file.write("\nProgram can't be executed further, please check and rectify input file inputPS7.txt.\n")
                file.close()
                exit(0)

            finalBookingPeriod.append([extractedStartDate,extractedEndDate])                            # Adding elements to the list array finalBookingPeriod

        finalBookingPeriod.sort()                                                                       # Sorting the list array finalBookingPeriod in ascending order

        n=len(finalBookingPeriod)                                                                       # Length of the entire array-list/heap
        stackCreated = []                                                                               # Array to store the values in the form of a stack
        carCount = 1                                                                                    # Assuming we already have 1 car available with us in the beginning
        heapq.heappush(stackCreated,finalBookingPeriod[0][1])                                           # Pushing 1st end date element into stack array stackCreated

        for i in range(1,n):                                                                            # Looping through the list
            if stackCreated[0] >= finalBookingPeriod[i][0]:                                             # if existing value in stack >= startDate[i], then extra car req.
                carCount += 1
            else:                                                                                       # else, to pop the existing element in the stack
                heapq.heappop(stackCreated)
            heapq.heappush(stackCreated,finalBookingPeriod[i][1])                                       # Pushing subsequent elements into stack array StackCreated

        outputFile = open("outputPS7.txt", "w")                                                         # Opening the output file
        outputFile.writelines("Cars - "+ str(carCount))                                                       # Writing the result to the output file 
        outputFile.close()                                                                                    # Closing the output file
    # End of function calculateCarsRequired()

    # Start of main function
    if __name__ == "__main__" :
        calculateCarsRequired()                                                                         # Calling the function calculateCarsRequired() 
        print("\n\nCompleted. Check outputPS7.txt in the current directory for output.\n\n")
    # End of main function
# End of class carRentalService