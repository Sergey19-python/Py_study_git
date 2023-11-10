s = "Hello world, Русский"
sb = b"Hello world"

print(s[0:3])
print(sb[0:3])


sb = s.encode("utf-8")
print(sb)
s = sb.decode("utf-8")
print(s)