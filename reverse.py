text = input("Enter a string: ")
reverse_text = ""
for i in range(len(text) - 1, -1, -1):
    reverse_text = reverse_text + text[i]
print("Reversed string:", reverse_text)
