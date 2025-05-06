def triple(para):
    para['value'] = 3 * para['value']
    return para['value']

num = { 'value': 2 }

print("Value before function invocation:", num['value'])
print("Value multiplied in function:", triple(num))
print("Value after function invocation:", num['value'])
