# Ejemplo kwargs: ejemplo de función admitiendo pares de valores
# Como argumento de entrada utiliza **kwargs
def test_kwargs(**kwargs):
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))


mi_kwargs = {"tres": 3, "cinco": 5}

test_kwargs(**mi_kwargs)
