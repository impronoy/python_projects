#############################################################################################################################################################################
#The program is developed using the Greedy Knapsack approach to calculate the 
#ratio value/weight for each type of fuel and sort the fuel on the basis of their ratio.
#Fuel with the highest ratio is taken first and added until as much as cylinder can accommodate 
#else add the next fuel until the full capacity of the cylinder utilized and 
#repeat the same process for each fuel w.r.t cylinder capacity.
#############################################################################################################################################################################
import sys
def max_power():  #Defining funtion
  values=[]   #assigning empty array to values
  fuelInfo=[]   #assigning empty array to fuelInfo   
  quantity=[]   #assigning empty array to quantity   
  power=[]    #assigning empty array to power    
  try:    #Handling exception
    inputFile = "inputPS07.txt"    #Fetching input file  
    with open(inputFile,'r') as fileContents:   
        inputValues= fileContents.readlines()   #Reading lines of input file
        for lines in inputValues[0:2]:    #Iterating through first two lines of input file
          try:    #Handling exception
            if(lines!="/n"):
              values.append(int(lines.strip().split(':')[1]))   #Storing Fuel and Max cylinder weight values as a list
          except:
            print('Fuel or Cylinder weight is missing!')
            outFile=open("outputPS07.txt", "w")
            outFile.write("Fuel or Cylinder weight is missing!\n")
            outFile.close()
            sys.exit()
        for info in inputValues[2:]:    #Iterating from 3rd line to rest lines of input file
          try:    #Handling exception
            if(lines!="/n"):
              if info.strip().split('/')[0]!= "":
                fuelInfo.append(info.strip().split('/')[0])   #Storing fuel names as a list
              else:
                fuelInfo.append("Missing Fuel Type ")   #Storing fuel names as a list
              quantity.append(int(info.strip().split('/')[1]))    #storing quantities(liter) as a list
              power.append(int(info.strip().split('/')[2]))   #Storing power per liter as a list
          except:
            print('Give input in right format!')
            outFile=open("outputPS07.txt", "w")
            outFile.write("Give input in right format!\n")
            outFile.close()
            sys.exit()
  except FileNotFoundError:
    print("File Not Found!")
    outFile=open("outputPS07.txt", "w")
    outFile.write("File Not Found!\n")
    outFile.close()
    sys.exit()
  '''
  Using knapsack methodology of Greedy algorithm below - 
  '''
  cylinderWeight=values[1]   #Assigning 2nd index of values(i.e.- Max cylinder weight)
  numOfFuel=len(quantity)   #assigning length of quantity in a variable
  selectionRatio=[0]*numOfFuel   #selectionRatio array with length n
  if numOfFuel==values[0]:    #comparison
    ratios=[powr/quant for powr,quant in zip(power,quantity)]   #calculating ratios of power/quantity
    index=list(range(numOfFuel))
    index.sort(key=lambda i : ratios[i], reverse=True)    #sorting index values
    max_value=0     #variable to store the total power
    for i in index:     #Iterating through to the total number of fuel quantity and comparing if quantity available for particular fuel <= Current Cylinder Capacity
      if quantity[i]<=cylinderWeight:   
        max_value+=power[i]*quantity[i]
        cylinderWeight-=quantity[i]
        selectionRatio[i]=1
      else:     #calculation selection ratio and adding calculated power to total power as max_value
        selectionRatio[i]=cylinderWeight/quantity[i]
        max_value+=power[i]*cylinderWeight
        break
    print("Total Power: "+ str(max_value))
    outputFile = open("outputPS07.txt", "w")
    outputFile.write("Total Power: "+ str(max_value)+'\n')
    outputFile.write('Fuel selection Ratio: \n')
    print('Fuel selection Ratio: ')
    for finfo,frac in zip(fuelInfo,selectionRatio):     #for printing fuelinfo and selection ratio
      h= (f'{finfo} : {frac}')
      outputFile.write(h+'\n')
      print(h)
    outputFile.close()
  else:     #If the No. of fuels are not matching with input fuel count
    print('No. of fuels are not matching with input fuel count!')
    outFile=open("outputPS07.txt", "w")
    outFile.write("No. of fuels are not matching with input fuel count!\n")
    outFile.close()

  # Start of main function
if __name__ == "__main__" :
  max_power() 
  print("\n***Check outputPS07.txt in the current directory for output.***\n")
  # End of main function