def ft_filter(function, word):
    if function is None:
        return (index for index in word if index)
    return (index for index in word if function(index))