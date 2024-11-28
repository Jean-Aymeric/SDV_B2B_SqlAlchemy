from database.model import Department, Employee, Bidule

print(Department.getById("d005").toDict())
print(Employee.getById(10043).toDict())
print(Bidule.getAll())

monBidule = Bidule()
monBidule.name = "Un nouveau truc"
monBidule.insert()
print(monBidule.toDict())