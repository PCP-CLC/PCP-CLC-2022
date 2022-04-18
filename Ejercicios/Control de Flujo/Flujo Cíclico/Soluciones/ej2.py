for item in range(5):
    p_original = 3990 * item + 3990
    descuento = p_original * 0.60
    p_final = p_original / 100 * 40

    print("Precio original: ${} | Descuento: ${} | Precio final: ${} ".format(int(p_original), int(descuento), int(p_final)))

