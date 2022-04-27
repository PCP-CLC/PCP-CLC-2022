kms_por_milla = 1.609344
pies_por_metro = 3.2808399
cms_por_pulgada = 2.54

def millas_a_kms(mi):
    return mi * kms_por_milla

def kms_a_millas(km):
    return km / kms_por_milla

def pies_a_mts(pies):
    return pies / pies_por_metro

def mts_a_pies(mt):
    return mt * pies_por_metro

def pulgadas_a_cms(p):
    return p * cms_por_pulgada

def cms_a_pulgadas(cm):
    return cm / cms_por_pulgada

