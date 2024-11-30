def print_params(a = 1, b = "строка", c = True):
    print(a, b, c)

print_params(100, 200)
print_params("one")
print_params()
print()
print_params(b = 25)
print_params(c = [1, 2, 3])
print()
values_list = ["one", False, [40, 50, 60]]
values_dict = {'a' : 15, 'b' : "some-text", 'c' : False}
print_params(*values_list)
print_params(**values_dict)
print()
values_list_2 = ["seven", 404]
print_params(*values_list_2, 42)


