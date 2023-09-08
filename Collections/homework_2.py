import random


# Generate a list of random dictionaries
def generate_random_dicts():
    list_of_dicts = []  # initialize an empty list
    num_dicts = random.randint(2, 10)  # generate a random integer between 2 and 10 and assign it to the variable

    for i in range(1, num_dicts + 1):  # loop will iterate from 1 to num_dicts(inclusive)
        num_keys = random.randint(1, 100)  # generate a random integer between 1 and 100 and assign it to the variable
        rand_dict = {}  # initialize an empty dictionary
        for j in range(num_keys):
            key = chr(random.randint(97, 122))  # generate a random lowercase letter and assign it to the variable
            value = random.randint(0, 100)  # generate a random integer between 0 and 100 and assign it to the variable
            rand_dict[key] = value  # add a key-value pair to a 'rand_dict' dictionary
        list_of_dicts.append(rand_dict)  # append the 'rand_dict' dictionary to the 'list_of_dicts' list

    return list_of_dicts  # return the contents of the 'list_of_dicts' variable as its result


# Create common dictionary
def create_common_dict(list_of_dicts):
    common_dict = {}  # initialize an empty dictionary
    for i, dict in enumerate(list_of_dicts):  # obtain both the index (i) and the value (dict) of each element in the iteration
        for key, value in dict.items():  # iterate through the key-value pairs within a dictionary
            if key in common_dict:
                if value > common_dict[key]:  # check whether the value is greater than the value currently associated with the same key in common_dict
                    # Rename the existing key with the dict number of the max value
                    common_dict[f"{key}_{i + 1}"] = value  # enumerate() function starts indexing from 0 by default, which is why we add 1 to i to correspond to the dictionary's position in the list
                    del common_dict[key]  # delete a key-value pair from the dictionary
            else:
                common_dict[key] = value  # add a new key-value pair with the specified key and value

    return common_dict  # return the contents of the 'common_dict' variable as its result


# Main function
def main():
    # random_dicts = generate_random_dicts()
    random_dicts = [{'a':2,'b':75,'c':40,'j':87},{'a':27,'b':9,'c':40,'d':87}]
    print("List of random dicts:")
    for i, dict in enumerate(random_dicts, start=1):  # start=1 argument specifies that the index should start at 1 instead of the default value of 0
        print(f"Dict {i}: {dict}")

    common_dict = create_common_dict(random_dicts)
    print("\nCommon dictionary:")
    print(common_dict)


if __name__ == "__main__":
    main()
