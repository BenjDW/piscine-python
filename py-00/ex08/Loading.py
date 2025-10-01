import os


def ft_tqdm(lst: range) -> None:
    """
    A simplified reimplementation of the tqdm progress bar.

    This function iterates over a given iterable, displaying a textual
    progress bar in the terminal. For each element, it shows the
    percentage completed, the progress bar, and the current index.

    Args:
        lst (iterable): The sequence or range to iterate over.

    Yields:
        element: The current element from the iterable.

    Example:
        >>> for i in ft_tqdm(range(5)):
        ...     time.sleep(0.2)
        20%|[==>...]| 1/5
        40%|[====>..]| 2/5
        ...
    """
    total = len(lst)
    if total == 0:
        pass

    cols = os.get_terminal_size().columns
    bar_len = max(10, cols - 42)

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
