#9) located between iceland and norway what island relates to the country?

country_choice = [
    "A):Iceland",
    "B):Norway",
    "C):Denmark",
    "D):Finland",
]

print('located halfway between iceland and norway, the Faroe islands belong to which country?:')

choices = (country_choice)
print(*choices, sep = "\n")

answer = input()
if answer == "c" or answer == "C":
    print(answer, "is correct!")
elif answer == "denmark" or answer == "Denmark":
    print(answer, "is correct!")
else:
    print(answer, "is not correct!")

