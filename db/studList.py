from ntpath import join
import openpyxl
import os
from student import Stud




class ListStud():
    def __init__(self):
        self.content = os.listdir("C:/Users/DDaova/Desktop/src/отчет посещаемости/files")
        self.content = "C:/Users/DDaova/Desktop/src/отчет посещаемости/files/"+("".join(self.content))
        self.db = Stud()
        
    def getter(self):
        return self.id

    def vlparss(self):
        book = openpyxl.open(self.content, read_only = True)
        sheet = book.active

        self.cells = sheet['A2':'M200']

        for Fam, Name, SecondName, Id, group, curs, spec, state, form, rpd, technolog, recovery, transferred in self.cells:
            Fam = Fam.value
            Fam = Fam.split(" ")
            Name = str(Name.value)
            SecondName = str(SecondName.value)
            
            self.id = Id.value
            self.group = group.value
            self.fn = Fam[0] + " " + Name + " " + SecondName
            self.state = state.value

            print(self.id, "--------",  self.fn, "--------", self.group)

            self.db.creat_db(id = self.id, fn = self.fn, group = self.group, state = self.state)

            # print(Fam.value, Name.value, SecondName.value, Id.value, group.value, curs.value, spec.value, 
            #         state.value, form.value, rpd.value, technolog.value, recovery.value, transferred.value)






if __name__ == "__main__":
    
    date = ListStud()
    print(date.vlparss())
    print()

    


