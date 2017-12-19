import osa


def middle_temperature():
    temperature_list = list()
    with open("Temps.txt",) as file:
        for line in file:
            temperature_list.append(int(line.split()[0]))

    middle_temperature = sum(temperature_list) / len(temperature_list)
    return middle_temperature


def Convert_temperature(Temperature_value, FromUnit = "degreeFahrenheit", ToUnit = "degreeCelsius"):
    client = osa.Client("http://www.webservicex.net/ConvertTemperature.asmx?WSDL")
    print (round(client.service.ConvertTemp(Temperature_value, FromUnit, ToUnit), 2))


def temperature_calculator():
    command = input('Введите "1", если хотите увидеть решение 1 задачи. '
                    'Для открытия калькулятора введите что-нибудь другое: ')
    if command == "1":
        Convert_temperature(middle_temperature())
    else:
        fromUnit = input("Введите то, что будете переводить: ")
        toUnit = input("Ведите то на что будете переводить:" )
        temperature_value = int(input("Введите значение температуры: "))
        Convert_temperature(temperature_value, fromUnit, toUnit)


temperature_calculator()


