def ft_filter(function, word):
    """
    Apply a filtering function to a list of words.

    This function behaves like Python's built-in filter: it returns
    an iterator containing only the elements for which `function`
    returns True. If function is None, all truthy elements are returned.

    Args:
        function (callable or None): A function applied to each element.
        word (iterable): A sequence of strings to filter.

    Returns:
        iterator: An iterator of the filtered elements.
    """
    # generator expression
    if function is None:
        return (index for index in word if index)
    return (index for index in word if function(index))
