import os
import datetime
def logger(old_function):
    data_old_function = {}
    parametr_old_function = {}
    def new_function(*args, **kwargs):
        start_old_function = datetime.datetime.now()
        parametr_old_function['arg_args'] = args
        parametr_old_function['kwargs'] = kwargs
        parametr_old_function['data'] = str(start_old_function)
        result = old_function(*args, **kwargs)
        name_old_function = str(old_function.__name__)
        data_old_function[f"{name_old_function}"] = parametr_old_function, {"result": result}
        with open("main.log", 'a', encoding='utf-8') as file:
            file.write(str(data_old_function))
            file.write("\n")
        return result
    return new_function
