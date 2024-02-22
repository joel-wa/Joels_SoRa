def convert_string_to_tuple(input_string):
    # Remove the outer square brackets and split the string into pairs
    pairs_str = input_string.strip('[]')
    pairs_list = pairs_str.split('), ')

    mainTuple = ()
    for pair in pairs_list:
        pair=pair.split(",")
        
        pair[0] = pair[0].split("(")[1]
        # print(pair)
        lists = []
        customTuple = ()
        for value in pair:
            value = value.strip(")")
            v = int(value)
            # print(v)
            lists.append(v)
            customTuple = customTuple + (v,)
        # print(customTuple)
        mainTuple = mainTuple + (customTuple,)

    print(mainTuple)
    return mainTuple

# Example usage
input_string = "[(0, 1), (1, 2), (2, 3), (3, 0), (0, 4), (1, 4), (2, 4), (3, 4)]"
resulting_tuple = convert_string_to_tuple(input_string)
# print(resulting_tuple)
