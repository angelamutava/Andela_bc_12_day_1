def data_type(argument):
  if isinstance(argument, str):
    return len(argument)
  elif argument is None:
    return 'no value'
  elif isinstance(argument, bool):
    return argument
  elif isinstance(argument, int):
    if argument==100:
      return 'equal to 100'
    elif argument < 100:
      return 'less than 100'
    elif argument > 100:
      return 'more than 100'
  elif isinstance(argument, list):
    len_of_list = len(argument)-1
    if len_of_list >=2:
      return argument[2]
    else:
      return None