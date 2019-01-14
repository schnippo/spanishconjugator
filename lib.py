class endungen:
    ar_pr = ["o", "as", "a", "amos", "aís", "an"]
    ir_pr = ["o", "is", "e", "imos", "ís", "en"]
    er_pr = ["o", "es", "e", "emos", "eís", "en"]

    ar_in = ["é", "aste", "ó", "amos", "asteis", "aron"]
    ir_in = ["í", "iste,", "ó", "imos", "isteis", "eron"]
    er_in = ["í", "iste,", "ó", "imos", "isteis", "ieron"]

    ar_im = ["aba", "abas", "aba", "àbamos", "abais", "abian"]
    ir_im = ["ía", "ías", "ía", "íamos", "íais", "ían"]
    er_im = ["ía", "ías", "ía", "íamos", "íais", "ían"]

    hilfs_verben_cp = ['he', 'has', 'ha', 'hemos', 'habeís', 'han']
    hilfs_verben_fu = ['voy', 'vas', 'va', 'vamos', 'vais', 'van']

class wort:
    verb_conjugated = []

    def eingabe(self):
        self.wort = input("Verb:")
        if self.wort.isalpha():
            return self.wort
        elif self.wort == '':
            self.eingabe()
        elif len(self.wort) < 2:
            self.eingabe()
        else:
            self.eingabe()

    # Checkt, ob das Wort reflexiv ist -> Damit man weiss, wieviel man vom Stamm wegnehmen muss, um den Stamm zu
    # bekommen
    def temp_eingabe(self):
        print('''Choose Temp:
              presente - pr
              compuesto - cp
              indicativo - in
              imperfecto - im
              futuro - fu''')
        self.temp = input('Which temp: ')

        if self.temp == 'present' or self.temp == 'pr' or self.temp == 'presente':
            self.temp = 'present'
            return
        elif self.temp == 'indicativo' or self.temp == 'in':
            self.temp = 'indicativo'
            return
        elif self.temp == 'imperfecto' or self.temp == 'im':
            self.temp = 'imperfecto'
            return
        elif self.temp == 'compuesto' or self.temp == 'cp':
            self.temp = 'compuesto'
            return
        elif self.temp == 'futuro' or self.temp == 'fu':
            self.temp = 'futuro'
        else:
            self.temp_eingabe()

    def refl_check(self):
        if self.wort[len(self.wort) - 2:] == 'se':
            return True
        else:
            return False

    # Loest den Stamm aus dem Wort
    def remove_refl(self):
        if self.refl_check():
            self.wort_ohne_refl = self.wort[:len(self.wort) - 2]
        else:
            self.wort_ohne_refl = self.wort

    def set_ending_type(self):
        if self.wort_ohne_refl[len(self.wort_ohne_refl) - 2:] == "ir":
            self.ending = 'ir'
        elif self.wort_ohne_refl[len(self.wort_ohne_refl) - 2:] == "er":
            self.ending = 'er'
        elif self.wort_ohne_refl[len(self.wort_ohne_refl) - 2:] == "ar":
            self.ending = 'ar'
        else:
            print("Error: No ending found")

    def get_stamm(self):

        if self.refl_check():
            return self.wort[:len(self.wort) - 4]
        else:
            return self.wort[:len(self.wort) - 2]

    def conjugate(self):
        if self.temp == 'present':
            if self.ending == 'ar':
                for ending in endings.ar_pr:
                    self.verb_conjugated.append(self.stamm + ending)
                return self.verb_conjugated

            elif self.ending == 'er':
                for ending in endings.er_pr:
                    self.verb_conjugated.append(self.stamm + ending)
                return self.verb_conjugated

            elif self.ending == 'ir':
                for ending in endings.ir_pr:
                    self.verb_conjugated.append(self.stamm + ending)
                return self.verb_conjugated

        elif self.temp == 'indicativo':
            if self.ending == 'ar':
                for ending in endings.ar_in:
                    self.verb_conjugated.append(self.stamm + ending)
                return self.verb_conjugated

            elif self.ending == 'er':
                for ending in endings.er_in:
                    self.verb_conjugated.append(self.stamm + ending)
                return self.verb_conjugated

            elif self.ending == 'ir':
                for ending in endings.ir_in:
                    self.verb_conjugated.append(self.stamm + ending)
                return self.verb_conjugated
        elif self.temp == 'imperfecto':
            if self.ending == 'ar':
                for ending in endings.ar_im:
                    self.verb_conjugated.append(self.stamm + ending)
                return self.verb_conjugated

            elif self.ending == 'er':
                for ending in endings.er_im:
                    self.verb_conjugated.append(self.stamm + ending)
                return self.verb_conjugated

            elif self.ending == 'ir':
                for ending in endings.ir_im:
                    self.verb_conjugated.append(self.stamm + ending)
                return self.verb_conjugated
        elif self.temp == 'compuesto':
            for hilfsverb in endings.hilfs_verben_cp:
                self.verb_conjugated.append(hilfsverb + ' ' + self.compuesto)
        elif self.temp == 'futuro':
                    for hilfsverb in endings.hilfs_verben_fu:
                        self.verb_conjugated.append(hilfsverb + ' a ' + self.wort_ohne_refl)

    def props(self):
        # print(self.stamm)
        for word in self.verb_conjugated:
            print(word)

    def get_compuesto(self):
        if self.ending == 'ir' or self.ending == 'er':
            self.compuesto = self.stamm + 'ido'
        elif self.ending == 'ar':
            self.compuesto = self.stamm + 'ado'

    def __init__(self):
        self.wort = self.eingabe()
        self.temp_eingabe()
        self.stamm = self.get_stamm()
        self.remove_refl()
        self.set_ending_type()
        self.get_compuesto()
        self.conjugate()

endings = endungen()