def shape_area(shape,diamension):
    if shape=='circle':
        return 3.14*(diamension**2)
    elif shape=='square':
        return diamension**2
    elif shape=='triangle':
        return 0.5*diamension[0]*diamension[1]
    else:
        return"Invalid shape"
print(shape_area('circle',5))
print(shape_area('square',4))
print(shape_area('triangle',(3,4)))                                                                        
print(shape_area('hexagon',5))
        