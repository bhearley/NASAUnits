# UnitConversion is a function for converting units consistent with the NASA GRC Granta MI Database
#
# INPUTS:
#    source_unit    the units to convert from
#    source_value   the value for conversion
#    target_unit    the units to convert to
#
# OUTPUTS:
#    target_value   the value after conversion
#    out_message    the output message

def UnitConversion(source_unit, source_value, target_unit):
    # Import Modules
    import requests
    import json

    # Load the units library
    url = 'https://raw.githubusercontent.com/bhearley/NASAUnits/refs/heads/main/unit_library.json'
    response = requests.get(url)

    # Check for valid file
    if response.status_code == 200:
        U = response.json()  # Parse the JSON response
    else:
        raise Exception("Error reading the material library.")
        U = None

    # Check for valid keys
    if source_unit not in U.keys():
        raise ValueError("Source Unit " + source_unit + " not found in material library.")
    if target_unit not in U.keys():
        raise ValueError("Target Unit " + target_unit + " not found in material library.")
        
    # Convert to Global Variable
    data = U[source_unit]
    val = eval(data[0].replace('x', str(source_value)))
    
    data = U[target_unit]
    target_value = eval(data[1].replace('x', str(val)))

    return target_value
