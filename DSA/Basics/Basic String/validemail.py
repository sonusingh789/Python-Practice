# email = "itsmesonu47@gmailcom"


# em_arr = []
# for ch in email:
#     em_arr.append(ch)
# freq = {}
# for ch in em_arr:
#     freq[ch] = freq.get(ch, 0) + 1
# if "@" not in em_arr or "." not in em_arr:
#     print("invalid email")
# elif freq["@"] > 1 or freq["."] > 1:
#     print("Remove Extra @ or .")
# else:
#     print("valid email continue")


email = "itsmesonu47@gmailcom"

freq = {}

for ch in email:
    freq[ch] = freq.get(ch, 0) + 1

if "@" not in freq or "." not in freq:
    print("Invalid email")

elif freq["@"] > 1 or freq["."] > 1:
    print("Invalid email")

elif email[0] == "@" or email[-1] == ".":
    print("Invalid email")

elif email.index("@") > email.index("."):
    print("Invalid email")

else:
    print("Valid email")
