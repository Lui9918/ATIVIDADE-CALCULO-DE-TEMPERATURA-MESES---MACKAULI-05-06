if __name__ == '__main__':

    months = ["January", "February", "March", "April", "May", "June", "Juiy", "August", "Septemper", "Octuber", "November", "Dezember"]

    i = 0

    temperature_month = []
    begin = 0
    print("Write temperature of month for sequence, for example: first: January, second: February...")
    while (begin <= 12):
        month = float(input("Write temperature from the month: "))
        temperature_month.append(month) #estou adiconando num ao vetor
        begin = begin + 1
        print ("Temperature registred!")

    i = 0

    temperature_sum = (temperature_month[0] + temperature_month[1] + temperature_month[2] + temperature_month[3] + temperature_month[4] + temperature_month[5] + temperature_month[6] + temperature_month[7] + temperature_month[8] + temperature_month[9] + temperature_month [10] + temperature_month [11])
    average = temperature_sum / 12

    print(f"The average is: {average}")

    while (i <= 11):

        if (temperature_month[i] > average):
            print(f"The {months[i]}, temperature is {temperature_month[i]}, higher than average")
        i = i + 1

