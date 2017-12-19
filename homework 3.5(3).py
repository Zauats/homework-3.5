import osa


def lenght_value_list():
    lenght_value_str_list = list()
    with open("travel.txt") as f:
        for line in f:
            lenght_value_str_list.append(line.strip().split()[1])

    lenght_value_int_list = list()
    for lenght in lenght_value_str_list:
        s = lenght.split(",")
        if len(s) > 1:
            s = s[0] + s[1]
        else:
            s = s[0]
        lenght_value_int_list.append(s)
        return lenght_value_int_list





def translation_of_length(lenght_value):
    client = osa.Client("http://www.webservicex.net/length.asmx?WSDL")
    killometers_value = client.service.ChangeLengthUnit(lenght_value, "Miles", "Kilometers")
    return killometers_value

killometers_value_list = list()
for Mils_value in lenght_value_list():
    killometers_value = translation_of_length(Mils_value)
    killometers_value_list.append(killometers_value)

print(round(sum(killometers_value_list), 2))






