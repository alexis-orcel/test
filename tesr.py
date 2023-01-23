def convert(self):
    ent = self.entry.get()
    if ent == '':
        ent = 0
    else:
        ent = float(ent)
    a = 1.24
    b = 0.79
    c = 146.04
    d = 17.04
    e = 655.62
    f = 106.81
    g = 58.22
    h = 7.64
    i = 77.04
    j = 3.16
    if self.sens.get() == 's1':
        if self.monnaie.get() == 'Dollars US':
            o = ent * a
            self.error.set('')
        elif self.monnaie.get() == 'Livres Sterling':
            o = ent * b
            self.error.set('')
        elif self.monnaie.get() == 'Yen':
            o = ent * c
            self.error.set('')
        elif self.monnaie.get() == 'Pesos mexicains':
            o = ent * d
            self.error.set('')
        elif self.monnaie.get() == 'Francs CFA':
            o = ent * e
            self.error.set('')
        elif self.monnaie.get() == 'Dinars algeriens':
            o = ent * f
            self.error.set('')
        elif self.monnaie.get() == 'Roubles russes':
            o = ent * g
            self.error.set('')
        elif self.monnaie.get() == 'Yuan':
            o = ent * h
            self.error.set('')
        elif self.monnaie.get() == 'Roupies indiens':
            o = ent * i
            self.error.set('')
        elif self.monnaie.get() == 'Reals bresiliens':
            o = ent * j
            self.error.set('')
        else:
            self.error.set('Veuillez entrer toutes les informations necessaires a* la conversion')
            print('Probleme')
        monnaie_arrivee = self.monnaie.get()
    elif self.sens.get() == 's2':
        if self.monnaie.get() == 'Dollars US':
            o = ent / (a + 0.0)
            self.error.set('')
        elif self.monnaie.get() == 'Livres Sterling':
            o = ent / (b + 0.0)
            self.error.set('')
        elif self.monnaie.get() == 'Yen':
            o = ent / (c + 0.0)
            self.error.set('')
        elif self.monnaie.get() == 'Pesos mexicains':
            o = ent / (d + 0.0)
            self.error.set('')
        elif self.monnaie.get() == 'Francs CFA':
            o = ent / (e + 0.0)
            self.error.set('')
        elif self.monnaie.get() == 'Dinars algeriens':
            o = ent / (f + 0.0)
            self.error.set('')
        elif self.monnaie.get() == 'Roubles russes':
            o = ent / (g + 0.0)
            self.error.set('')
        elif self.monnaie.get() == 'Yuan':
            o = ent / (h + 0.0)
            self.error.set('')
        elif self.monnaie.get() == 'Roupies indiens':
            o = ent / (i + 0.0)
            self.error.set('')
        elif self.monnaie.get() == 'Reals bresiliens':
            o = ent / (j + 0.0)
            self.error.set('')
        else:
            print('probleme')
            self.error.set('Veuillez entrer toutes les informations necessaires a* la conversion')
        monnaie_arrivee = 'Euros'
    else:
        self.error.set('Veuillez entrer toutes les informations necessaires a* la conversion')
        print('pb')
    self.output.set('Vous avez ' + str(o) + ' ' + monnaie_arrivee)
