# value = input("Enter your text here having emoticons here:")
# value = value.replace(":)","🙂").replace(":(","🙁")
# print(value)

def convert(x):
    y = x.replace(":)","🙂").replace(":(","🙁")
    return y

z=input("Enter Text: ")
i = convert(z)
print(i)
