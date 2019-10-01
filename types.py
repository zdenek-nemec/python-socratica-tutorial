number_integer = 7
print(number_integer)
print(type(number_integer))

number_float = 7.0
print(number_float)
print(type(number_float))

number_complex = 7+4j
print(number_complex)
print(type(number_complex))
print(number_complex.real)
print(number_complex.imag)

print(type(True))
print(type(False))

my_set = set()
print(type(my_set))
my_set.add(42)
my_set.add(False)
my_set.add(3.14156)
my_set.add("Thorium")
print(my_set)

my_list = []
print(type(my_list))
my_list.append(1)
my_list.append("Hello")
print(my_list)

my_dictionary = {"user_id":209, "message":"D5 E5 C5 C4 G4", "language":"English"}
print(type(my_dictionary))
print(my_dictionary.keys())
print(my_dictionary.values())
