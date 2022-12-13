class Firma:
    def __init__(self,name):
        self.name = name
        self.abteilungen = []


    def getAnzMitarbeiterAbteilung(self,abteilung):
            if abteilung in self.abteilungen:
                return abteilung.getAnzMitarbeiter()
            else:
                return -1

    def getAnzMitarbeiter(self):
        anz = 0
        for a in self.abteilungen:
            anz += a.getAnzMitarbeiter()

        return anz

    def getAnzAbteilungsleiter(self):
        anz = 0
        for a in self.abteilungen:
            for m in a.mitarbeiter:
                if isinstance(m,Abteilungsleiter):
                    anz+=1

        return anz

    def getAnzAbteilungen(self):
        return len(self.abteilungen)

    def getAbteilungMitMaxMitarbeiter(self):
        anz = 0
        for a in self.abteilungen:
            if anz < a.getAnzMitarbeiter():
                anz = a.getAnzMitarbeiter()

        result = []
        print(anz)
        for a in self.abteilungen:
            if a.getAnzMitarbeiter() == anz:
                result.append(a.name)

        return result

    def getProzentFzuM(self):
        anzF = 0
        for a in self.abteilungen:
            for m in a.mitarbeiter:
                if m.geschlecht == "Frau":
                    anzF+=1
        anzM = 0

        for a in self.abteilungen:
            for m in a.mitarbeiter:
                if m.geschlecht == "Mann":
                    anzM+=1

        anzO = self.getAnzMitarbeiter()-anzF-anzM
        ges = self.getAnzMitarbeiter()

        return {"GesamtAnz":ges,"Frau":anzF/ges,"Mann":anzM/ges, "Other":anzO/ges}

class Abteilung:
    def __init__(self,name, firma):
            self.name = name
            self.mitarbeiter = []
            self.firma = firma

    def getAnzMitarbeiter(self):
        return len(self.mitarbeiter)


class Person:
    def __init__(self, vName,nName,alter,geschlecht):
        self.vName = vName
        self.nName = nName
        self.alter = alter
        self.geschlecht = geschlecht


class Mitarbeiter(Person):
    def __init__(self,vName,nName,alter,geschlecht,abteilung ):
        super().__init__(vName,nName,alter,geschlecht)
        self.abteilung = abteilung

class Abteilungsleiter(Mitarbeiter):
    def __init__(self,vName,nName,alter,geschlecht,abteilung):
        super().__init__(vName,nName,alter,geschlecht,abteilung)


if __name__ == "__main__":

    firma = Firma("HTL")
    abteilung1 = Abteilung("ab1",firma)
    firma.abteilungen.append(abteilung1)
    abteilung2 = Abteilung("ab2", firma)
    firma.abteilungen.append(abteilung2)

    abteilung1.mitarbeiter.append(Mitarbeiter("Fabian","Lintner",3,"Mann",abteilung1))
    abteilung1.mitarbeiter.append(Abteilungsleiter("Sisi","Mayr",5,"Frau",abteilung1))
    abteilung2.mitarbeiter.append(Mitarbeiter("Luli","Lala",12,"Frau",abteilung2))
    abteilung2.mitarbeiter.append(Mitarbeiter("Hans","Hans",21,"Mann",abteilung2))
    abteilung2.mitarbeiter.append(Abteilungsleiter("Franz","Franz",22,"Mann",abteilung2))

    #print(firma.getAnzMitarbeiter())
    #print(firma.getAnzAbteilungsleiter())
    #print(firma.getAnzMitarbeiterAbteilung(abteilung1))
    #print(firma.getAbteilungMitMaxMitarbeiter())
    #print(firma.getAnzAbteilungsleiter())
    #print(firma.getAnzAbteilungen())
    #print(firma.getProzentFzuM())