global_var = 1
def my_vars():
    print('global variable:', global_var)
    local_var = 2
    print('local variable:', local_var)
global inner_var
inner_var = 3

my_vars()
print('coerced global:', inner_var)
