

# For loop

towns = ('Nakuru','Kisumu','Nairobi','Eldoret','Nanyuki','Meru', 'Kitale',
         'Machakos','Busia','Nyeri','Narok','Embu','Mombasa','Kisumu')


print(towns)
for town in towns:
    print(town)
    if town == "Nanyuki":
        print("My Home Town")
        break
    else:
        print("Its not my home town!")