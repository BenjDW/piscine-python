import os

def ft_tqdm(lst: range) -> None:
    total = len(lst)
    if total == 0:
        pass

    cols = os.get_terminal_size().columns
    # print(cols)
    bar_len = max(10, cols - 42)#142

    for i, elem in enumerate(lst, 1):
        ratio = i / total
        filled = int(ratio * bar_len)

        if filled <= 0:
            bar = ">" + "." * (bar_len - 1)
        elif filled >= bar_len:
            bar = "=" * (bar_len - 1) + ">"
        else:
            bar = "=" * (filled - 1) + ">" + "." * (bar_len - filled)

        percent = int(ratio * 100)
        line = f"\r{percent:3d}%|[{bar}]| {i}/{total}"

        print(line, end="", flush=True)
        yield elem

    print()

# def test(rng):
# 	for jk in rng:
# 		yield jk ** 2

# for i in test(range(10)):
# 	print(i)
# 	time.sleep(0.5)	