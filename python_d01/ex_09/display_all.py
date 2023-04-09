def display_all(Dictionary):

    List = list(Dictionary.keys())

    for i, j in Dictionary.items():

        print(List.index(i),'->','(',str(type(i) .__name__),':',j,')')

