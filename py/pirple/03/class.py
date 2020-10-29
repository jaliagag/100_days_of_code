# click = False

# Like = 0

# click = True

# if click == True: ## mind you the double =; it's for checking
#     Like += 1
#     click = False

# print(Like)

# temperature = 15
# thermo = 15
# #print(thermo)

# #if temperature < 15:
# if temperature <= 15:
#     thermo += 5
    
# #print(thermo)

# if temperature >= 10:
#     thermo -= 3

#print(thermo)

time = 'morning'
sleepy = True
pajamos = 'off'

if time == 'night' and sleepy == True:
    pajamos = 'on'

print('and:', pajamos)

if time == 'night' or sleepy == True:
    pajamos = 'on'
elif time == 'morning':
    pajamos = 'on'
else:
    pajamos = 'off'

print('or:', pajamos)

a = "b"
if True or True:
     a = "a"
print(a * 2)