import csv

def generate_schema():
    # Gather information interactively
    function_name = input("Enter the name of the function: ")
    function_description = input("Describe the function: ")
    
    num_parameters = int(input("How many parameters does the function have? "))
    
    function_parameters = {}
    
    # Collect information for each parameter
    for _ in range(num_parameters):
        param_name = input("Parameter name: ")
        param_description = input("Parameter description: ")
        param_type = input("Parameter type: ")

        # Ask if the parameter should be an enum
        is_enum = input("Should this parameter be an enum? (y/n): ").lower() == 'y'
        
        if is_enum:
            enum_values = input("Enter enum values (comma-separated): ").split(',')
            param_enum = [value.strip() for value in enum_values]
            param_info = {"type": "string", "description": param_description, "enum": param_enum}
        else:
            param_info = {"type": param_type, "description": param_description}
        
        function_parameters[param_name] = param_info
    
    # Generate and return the schema
    schema = {
        "name": function_name,
        "description": function_description,
        "parameters": {
            "type": "object",
            "properties": function_parameters,
        },
        "required": list(function_parameters.keys())
    }
    
    return schema

def save_to_csv(schema_list, csv_filename):
    with open(csv_filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        
        # Write header
        writer.writerow(["name", "description", "parameters", "required"])
        
        # Write data
        for schema in schema_list:
            writer.writerow([schema["name"], schema["description"], schema["parameters"], schema["required"]])

# Example usage
schema_list = []

while True:
    user_input = input("Do you want to generate a schema? (y/n): ").lower()
    
    if user_input != 'y':
        break
    
    resulting_schema = generate_schema()
    schema_list.append(resulting_schema)

csv_filename = input("Enter the CSV filename to save: ")
save_to_csv(schema_list, f"serverSide/gptFunctions/{csv_filename}")
