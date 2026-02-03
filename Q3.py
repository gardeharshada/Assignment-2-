# convert distance given in feet and inches into meters and centimeters:
def feet_inches_to_meters(feet, inches):
    total_inches = (feet * 12) + inches
    meters = total_inches * 0.0254
    centimeters = (meters - int(meters)) * 100
    return int(meters), round(centimeters)
feet = 5 
inches = 8
meters, centimeters = feet_inches_to_meters(feet, inches)
print(f"{feet} feet {inches} inches = {meters} meters {centimeters} centimeters")