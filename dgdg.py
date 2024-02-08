def palindrom(s):
    s = s.lower().replace(" ","")
    return s == s[::-1]
user_input = input("tell words")
if palindrom(user_input):
    print("palindrom")
else:
    print("it isnt palindrome")
    #2
def text(input_text, register):
    words = input_text.split()
    for i in range(len(words)):
        if words[i].lower() in register:
            words[i] = words[i].upper()
            return ''.join(words)
input_text = input("write text")
register = input("write words").split()
processed = (input_text,register)
print(processed)
#3
def cont(text):
    sentencese = 0
    for chat in text:
        if chat in ['.','!','?']:
            sentencese += 1
    a = "this is exampe.f.d..f.f"
    print(cont(a))