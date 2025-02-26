import inspect
import re
from datetime import date, datetime
from prompt_toolkit import prompt


def decodeParam(input_data, dataType):
    """
    list:   ["AUDCAD", "EURUSD", "AUDUSD"] -> "AUDCAD EURUSD AUDUSD"
    tuple:  ("AUDCAD", "EURUSD", "AUDUSD") -> '("AUDCAD", "EURUSD", "AUDUSD")'
    other:  1 -> '1'
    """
    if dataType == list:
        required_input_data = input_data.split(' ')
        if len(input_data) == 0:
            required_input_data = []
    elif dataType == tuple:
        required_input_data = eval(input_data)
    elif dataType == dict:
        required_input_data = eval(input_data)
    elif dataType == bool:
        required_input_data = False
        if input_data.upper() == 'TRUE' or input_data:
            required_input_data = True
    # as space/empty cannot int / float the transform
    elif dataType in (int, float) and (input_data == '' or input_data.isspace()):
        required_input_data = 0
    elif type(input_data) != dataType:
        required_input_data = dataType(input_data)  # __new__, refer: https://www.pythontutorial.net/python-oop/python-__new__/
    else:
        required_input_data = input_data
    return required_input_data

# convert dictionary parameter into raw string
def encodeParam(param):
    """
    list:   ["AUDCAD", "EURUSD", "AUDUSD"] -> "AUDCAD EURUSD AUDUSD"
    tuple:  ("AUDCAD", "EURUSD", "AUDUSD") -> '("AUDCAD", "EURUSD", "AUDUSD")'
    other:  1 -> '1'
    """
    if isinstance(param, list):
        encoded_param = " ".join([str(p) for p in param])
    elif isinstance(param, tuple):
        encoded_param = str(param)
    elif isinstance(param, dict):
        encoded_param = str(param)
    else:
        encoded_param = str(param)
    return encoded_param

# user input the param
def input_param(paramName, paramValue, dataTypeName, remark=''):
    # ask use input parameter and allow user to modify the default parameter
    if remark:
        print(f"Remark: {remark}")
    input_data = prompt(f"{paramName}({dataTypeName}): ", default=paramValue)
    # if no input, then assign default parameter
    if len(input_data) == 0:
        input_data = paramValue
    return input_data

def ask_param_fn(class_object, **overwrote_paramFormat):
    """
    :param class_object: class / function attribute
    :param overwrote_paramFormat: dict
    :return: obj, dict of param
    """
    # if it is none
    if not overwrote_paramFormat: overwrote_paramFormat = {}
    # params details from object
    signatures = inspect.signature(class_object)
    paramFormat = {}
    # looping the signature
    for sig in signatures.parameters.values():
        # argument after(*)
        if sig.kind == sig.KEYWORD_ONLY:
            # encode the param
            if sig.name in overwrote_paramFormat.keys():
                paramFormat[sig.name] = overwrote_paramFormat[sig.name]
            else:
                # has no default parameter
                if sig.default == sig.empty:
                    paramFormat[sig.name] = ['', sig.annotation]
                else:
                    paramFormat[sig.name] = [sig.default, sig.annotation]
    # ask user to input the param
    param = ask_param(paramFormat)
    return class_object, param

def ask_param(paramFormat):
    """
    purely to ask the param base on the dictionary
    :param params: dict, { name: [value, dataType, remark[optional] }
    :return:
    """
    params = {}
    for name, paramData in paramFormat.items():
        # getting the param data
        if len(paramData) == 3:
            value, dataType, remark = paramData
        else:
            value, dataType = paramData
            remark = ''
        # encode the param (for user input)
        encoded_param = encodeParam(value)
        # asking params
        input_data = input_param(name, encoded_param, dataType.__name__, remark)
        # decode the param
        decode_data = decodeParam(input_data, dataType)
        params[name] = decode_data
    return params