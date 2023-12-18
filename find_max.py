def find_max(value):
    if not isinstance(value, str):
        return "Please provide string that contains only numbers seperated by commas. E.g: 2,4,33,1,3,7,9"
    else:
        value_list = list(map(str, value.split(",")))
        result = max(value_list)
        try:
            result = int(result)
            return result
        except ValueError:
            return "Your string must contain numbers only with comma seperated. String is not acceptable"
        

number_list = [4, 7, 71, 9.9, 3, 11, 8]
number_list = "4,5,6,7,8,9,3,"
print(find_max(number_list))