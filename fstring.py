name = "Min Khaung"
gf = 3
#
# print("\n" +name + " has " + str(gf)+ " girlfriends who love him.")
#
# statment = "\n%s has %s girlfriends who love him." %(name,gf)
# print(statment)
#
# statment= "\n{} has {} girlfriends who love him.".format(name,gf)
# print(statment)
# #
# statment= "\n{} has {} girlfriends who love him.".format("Min Khaung", 3)
# print(statment)
#
ppl = {'name':'Min Khaung', 'gf':4}
# statment = "\n{name} has {gf} girlfirends who love him.".format(**ppl)
# print(statment)


########### fstring! ##############
text = f"\n{name} has {gf} girlfriends who love him."
print(text)
#
text = f"\n{name} has {4.44*4.44} girlfriends who love him."
print(text)
#
text = f"\n{name.lower()} has {gf} girlfriends who love him."
print(text)
#
text = f"\n{ppl['name']} has {ppl['gf']} girlfriends who love him."
print(text)
#
# #################formating option#####################
#
for num in range(1,11):
    print(f"\n 3.145 times {num} is {3.145*num:.2f} .", end="")

for num in range(1,11):
    print(f"\n{num} divided by 3.145 is {num / 3.145:.2%}")
#
#
def outer_function():
    x = 10

    def inner_function():
        nonlocal x
        x = 20



# print(outer_function())


# def non():
#     print("y is ",name)
#
#     def inn_non():
#         print("y is ", name2)
#
# (inn_non(12))
