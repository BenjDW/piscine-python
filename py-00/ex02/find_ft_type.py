from enum import Enum

def all_thing_is_obj(object: any) -> int:
	#your code here
	class switch(Enum):
		List = 1
		Tuple = 2
		Set = 3
		Dict = 4
		Str = 5
	
	result = type(object)

	mapping = {
        list: switch.List,
        tuple: switch.Tuple,
        set: switch.Set,
        dict: switch.Dict,
        str: switch.Str
    }

	match mapping.get(result, None):
		case switch.List:
			print("List :", result)
		case switch.Tuple:
			print("Tuple :", result)
		case switch.Set:
			print("Set :", result)
		case switch.Dict:
			print("Dict :", result)
		case switch.Str:
			print(object, "is in the kitchen :", result)
		case default:
			print("Type not found")
	return (42)

# other way without using enum
# match type(obj):
#     case list:
#         print("List :", type(obj))
#     case tuple:
#         print("Tuple :", type(obj))
#     case set:
#         print("Set :", type(obj))
#     case dict:
#         print("Dict :", type(obj))
#     case str:
#         print(obj, ":", type(obj))
#     case _:
#         print("Type not found")