ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
print()

ft_list[1] = "World!"

ft_tuple = ("Hello", "France!")

ft_set.remove("tutu!")
ft_set.add("Perpignan")

ft_dict["Hello"] = "42Perpignan!"

print(ft_list)
print(ft_tuple)
print(sorted(ft_set))
print(ft_dict)