#referencia para mahle: (Aros de rectificación, recambio e hidráulicos)
def ref_mahle_aros(ref):
        switch = {
            '1': ['STD.'],
            '2': ['STD', '025.'],
            '3': ['STD', '04.'],
            '4': ['STD', '04', '06.'],
            '5': ['STD', '04','06','08', '10.'],
            '6': ['STD', '05'],
            '7': ['STD', '05', '10.'],
            '8': ['STD', '020', '030', '040.'],
            '9': ['STD', '020', '030', '040', '060.'],
            '10': ['STD', '010', '020', '030', '040.'],
            '11': ['STD', '020', '040.'],
            '12': ['STD', '020.'],
            '13': ['STD', '025', '050.', '100.'],
            '14': ['STD', '025', '050.'],
            '15': ['STD', '010', '020.'],
            '16': ['STD', '10.'],
            '17': ['STD', '0,65'],
            '18': ['030'],
            '19': ['STD', '04', '06', '10.'],
            '20': ['STD', '050', '075.'],
            '21': ['STD', '06.'],
            '22': ['STD', '0,25', '0,50', '0,75', '1,00.'],
            '23': ['STD', '0,50', '0,75', '1,00.'],
            '24': ['STD', '0,30', '0,60', '0,90.'],
            '25': ['STD', '0,40', '0,80.'],
            '26': ['STD', '0,60', '1,00.'],
            '27': ['STD', '0,30', '0,60.'],
            '28': ['STD', '0,30', '0,40.'],
        }

        return switch.get(ref, 'N/A')   