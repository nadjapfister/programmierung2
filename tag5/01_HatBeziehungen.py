class Studiengang:
    def __init__ (self, hochschule, name):
        self.hochschule = hochschule
        self.name = ""

#------------------------------------------------------------------------------

class Prdogrammierkurs:
    def __init__ (self):
        self.name = "Programmieren"
        self.students = []

    def addStudent (self, student):
        self.students.append(student)

    def __str__ (self):
        s = ""
        for student in self.students:
            s += student.vorname + "" + student.nachname + "" + student.studiengang.name + "\n"
        return s


#------------------------------------------------------------------------------

class Student:
    def __init__ (self, vorname, nachname, geschlecht, studiengang):
        self.martikelnummer = ""
        self.vorname = vorname
        self.nachname = nachname
        self.adresse = ""
        self.studiengang = studiengang
        self.geschlecht = geschlecht

#------------------------------------------------------------------------------

geomatik = Studiengang("HABG", "Geomatik")
architektur = Studiengang("HABG", "Architektur")


student1 = Student("Hans", "Meier", "m", "geomatik")
student2 = Student("Petra", "Klein", "f", "geomatik")
student3 = Student("Nicola", "Sepp", "m", "architektur")

#------------------------------------------------------------------------------

prog = Prdogrammierkurs()

prog.addStudent(student1)
prog.addStudent(student2)
prog.addStudent(student3)

print (prog)

