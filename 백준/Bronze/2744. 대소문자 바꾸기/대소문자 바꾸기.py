sent = list(input())

for i in range(len(sent)):
    if sent[i] == sent[i].upper():
        sent[i] = sent[i].lower()
    else:
        sent[i] = sent[i].upper()

print(''.join(sent))