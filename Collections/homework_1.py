import random


def generate_random_dicts():
    list_of_dicts = []
    num_dicts = random.randint(2, 10)

    for i in range(1, num_dicts + 1):
        num_keys = random.randint(1, 100)
        rand_dict = {}
        for j in range(num_keys):
            key = chr(random.randint(97, 122))
            value = random.randint(0, 100)
            rand_dict[key] = value
        list_of_dicts.append(rand_dict)

    return list_of_dicts


def key_exists(d, target_key):
    return target_key is not None and any(key.startswith(target_key) for key in d.keys())


def select_keys_with_prefix(common_dict, prefix):
    for key, value in common_dict.items():
        if key.startswith(prefix):
            return key


def create_common_dict(list_of_dicts):
    common_dict = {}
    indexed_dict = {}
    for i, dict in enumerate(list_of_dicts):
        for key, value in dict.items():
            if key_exists(common_dict, select_keys_with_prefix(common_dict, key)):
                if value >= common_dict[select_keys_with_prefix(common_dict, key)]:
                    common_dict[f"{key}_{i + 1}"] = value
                    del common_dict[select_keys_with_prefix(common_dict, key)]
                elif key in common_dict and value < common_dict[key]:
                    key_lengths = {key: len(key) for key in common_dict.keys()}
                    for key_kl, length_kl in key_lengths.items():
                        if key_kl == key and length_kl == 1:
                            for key_id, value_id in indexed_dict.items():
                                if key_id == key:
                                    common_dict[f"{key}_{value_id}"] = common_dict[key]
                                    del common_dict[key]

            else:
                common_dict[key] = value
                indexed_dict[key] = i+1
    return common_dict


def main():
    # random_dicts = generate_random_dicts()
    random_dicts = [{'a': 2, 'b': 75, 'c': 40, 'j': 87}, {'a': 27, 'b': 9, 'c': 41, 'd': 87},
                {'a': 27, 'b': 71, 'c': 39, 'e': 87}]
    print("List of random dicts:")
    for i, dict in enumerate(random_dicts, start=1):
        print(f"Dict {i}: {dict}")

    common_dict = create_common_dict(random_dicts)
    print("\nCommon dictionary:")
    print(common_dict)


if __name__ == "__main__":
    main()
