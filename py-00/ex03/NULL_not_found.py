def NULL_not_found(object: any) -> int:
	#your code here
	match object:
		case None:
			print("Nothing:", object, type(object))
		case "":
			print("Empty:", object, type(object))
		case False:
			print("Fake:", object, type(object))
		case 0:
			print("Zero:", object, type(object))
		case _ if isinstance(object, float):
			if object != object:
				print("Cheese: nan", type(object))
			else:
				return (0)
		case _:
			print("Type not Found")
			return (1)
	return (0)