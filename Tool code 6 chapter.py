text = "X-DSPAM-Confidence:    0.8475";

print(text.find('0.8475'))
x=float(text[23:])
print(x)
print(type(x))