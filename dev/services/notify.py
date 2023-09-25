import file


def snake_to_sentence_case(string):
    return string.replace("_", " ").lower().capitalize()


def present_str_obj_mapping(m):
    for key, value in m:
        print(snake_to_sentence_case(key), ":", value)


def loaded_config(conf_vars):
    present_str_obj_mapping(conf_vars)
