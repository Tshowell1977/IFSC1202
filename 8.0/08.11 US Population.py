def main():
    yearly_change = []
    change=0.0
    total_change=0
    average_change=0
    greatest_increase=0
    smallest_increase=0
    greatest_year=0
    smallest_year=0
    BASE_YEAR=1950
    try:
        input_file = open("08.11 USPopulation.txt", "r")
        
        yearly_population= input_file.readlines()
       
        for i in range(len(yearly_population)):
            yearly_population[i] = float(yearly_population[i])
        
        for i in range(1,len(yearly_population)):
            change = yearly_population[i] - yearly_population[i-1]
            yearly_change.append(change) 

            
            if i==1:
                greatest_increase = change
                smallest_increase = change
                greatest_year = 1
                smallest_year = 1
           
            else:
                if change>greatest_increase:
                    greatest_increase = change
                    greatest_year = i
                elif change<smallest_increase:
                    smallest_increase = change
                    smallest_year = i
            total_change = float(sum(yearly_change))
            average_change = total_change/40
            print("The average annual change in population during the time period is",\
                  format(average_change, '.2f'))
            print("The year with the greatest increase in population was",
BASE_YEAR+greatest_year)
            print("The year with the smallest increase in population was",
BASE_YEAR+smallest_year)
            input_file.close()
    except IOError:
        print("The file could not be found")
    except IndexError:
        print("There was an indexing error")
    except:
        print("An error occurred")

main()