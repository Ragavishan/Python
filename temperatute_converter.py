def temperature_converter(scale,temperature):
    if scale=='c_to_f':
        return(temperature*9/5)+32
    elif scale=='f_to_c':
        return(temperature-32)*5/9
    else:
        return"Invalid scale"
print(temperature_converter('c_to_f',0))
print(temperature_converter('f_to_c',32))
print(temperature_converter('k_to_c',273))

