# python format_ft_time.py | cat -e
# Seconds since January 1, 1970: 1,666,355,857.3622 or 1.67e+09 in scientific notation$
# Oct 21 2022$

import time, datetime

def print_date():
	date = datetime.date.today()

	print("Seconds since January 1, 1970:", format(time.time(), ",.4f"), "or", format(time.time(), ".2e"), "in scientific notation")
	print(date.strftime("%b %d %Y"))

print_date()