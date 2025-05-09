def UnitConversion(source_unit, source_value, target_unit):
    
    # Import Modules
    import requests
    import json

    # Load the library
    url = 'https://raw.githubusercontent.com/bhearley/NASAUnits/refs/heads/main/unit_library.json'
    response = requests.get(url)
    
    if response.status_code == 200:
        U = response.json()  # Parse the JSON response
    else:
        U = None
        
    if U is not None:

        # Convert to Global Variable
        data = U[source_unit]
        val = eval(data[0].replace('x', str(source_value)))
        
        data = U[target_unit]
        target_val = eval(data[1].replace('x', str(val)))
    
        return target_val

    else:
        print('Error opening the unit library.')
        return None
