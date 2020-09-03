n = int(input("Enter the length of the sequence: ")) # Do not change this line
r_1 = 1
r_2 = 2
r_3 = 3
print(r_1)
print(r_2)
print(r_3) #fyrstu þrjú númer í rununni
for i in range(1, n-2):
    r = r_1 + r_2 + r_3 #fundið næsta númer í rununni
    print(r)
    r_1= r_2
    r_2 = r_3
    r_3 = r #endurskráð fyrsti númerin til að vera *nýjustu* þrjú stökin