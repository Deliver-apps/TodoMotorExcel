#Referencias de MAHLE CL (Conjuntos, sub-conjuntos, y camisas)

def ref_mahle_cl(ref):
    switch = {
        'A': ['STD.'],
        'A/1': ['STD - Entrega condicionada.'],
        'B': ['STD', '0.50.'],
        'C': ['STD', '0.50', '1.00.'],
        'D': ['STD', '0.25', '0.50', '0.75', '1.00.'],
        'E': ['STD', '04', '06.'],
        'F': ['STD', '0.25', '0.50', '1.00.'],
        'F/1': ['1.25', '1.50', '2.00.'],
        'G': ['0.50.'],
        'H': ['STD', '0.25', '0.50', '1.00.'],
        'I': ['Ø ext. camisa: 93,7; 94,5; 95,5; 96,2 mm..'],
        'J': ['STD', '06.'],
        'K': ['0.50', '1.00.'],
        'L': ['STD', '0.50', '0.75', '1.00.'],
        'M': ['STD', '04.'],
        'N': ['STD', '010', '020.'],
        'P': ['STD = 98,76 mm.', '+030', '-030', '-060.'],
        'Q': ['STD', '025.'],
        'R': ['STD con altura de compresión STD (HC 71,685)', 'STD, 0,5 y 1 con altura reducida en -0,1 mm (HC 71,585).'],
        'E.O.': ['Nº. de equipo original.'],
        'AC': ['Altura de Compresión reducida'],
        'WS': ['con aros de vedación (with seal)'],
        '1': ['Camisas con pestaña.'],
        '2': ['Se proveen sin bujes de bielas y sin  anillos de camisas.'],
        '3': ['Se proveen sin bujes de bielas y con anillos de camisas.'],
        '4': ['Se proveen con bujes de biela.'],
        'A.C': ['Altura de compresión.'],
    }

    return switch.get(ref, "N/A")
