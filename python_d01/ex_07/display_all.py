def display_all(Dictionary):

    List_values = list(Dictionary.values())

    for i in List_values:

      print('(',str(type(i) .__name__),':',i,')')
