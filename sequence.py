def sequence_class(immutable):
    return tuple if immutable else list


    #if immutable:
    #    cls = tuple
    #else:
    #    cls = list
    #return cls
