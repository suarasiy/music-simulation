def flatten(lists):
    flatlist = []
    # ['', '', ''] // [['', ''], '', '']
    if type(lists) == list:
        for elem in lists:
            if type(elem) == list:
                flatlist += flatten(elem)
            else:
                flatlist.append(elem)
        return flatlist

    if type(lists) == str:
        return lists


playlist = [
    "sakuzyo - Apathy",
    "sakuzyo - l'aventale",
    ['sakuzyo - trinity', 'sakuzyo - hoodie']
]
d = flatten(playlist)
print(d)
