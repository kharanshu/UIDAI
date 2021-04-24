from adhaar.models import *


# Create Person
p1 = Person(name="ABC", email="abc@gmail.com", mobile="123412")
p1.save()

p2 = Person(name="PQR", email="pqr@gmail.com", mobile="789123")
p2.save()

#Person.objects.create(name="PQR", email="pqr@gmail.com", mobile="789123")

# Create Adhaar

a1 = Adhar(person=p1, signature="asdf234dsafuiq3&^$^GUJHVR", adhar_no="432198176354")
a1.save()

a2 = Adhar(person=p2, signature="adfpoiwruywqtrgmnb13241)*&^%$", adhar_no="2314928376")
a2.save()

# Person Object
person_obj = Person.objects.all()
print(person_obj)  #prints all person entries

# Adhaar Object
adhaar_obj = Adhar.objects.all()
print(adhaar_obj)  #prints all adhaar links

# exec(open("D:\\AI Course\\Code\\Django\\UIDAI\\adhaar\\db_shell.py").read())