def peso_ideal(h):
    peso_ideal = 0.0
    m_h = input("homem-h, mulher-m")
    if m_h == "h":
        peso_ideal=(h*72.7)-58
    elif m_h == "m":
        peso_ideal = (h*62.1) - 44.7
    else:
        print('invalido')

    return peso_ideal

print(peso_ideal(1.70))