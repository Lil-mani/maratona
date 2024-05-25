s = input()
c = 0
for i in range(len(s)):
    if i  != " ":
        c+=1

if c<=140:
    print("TWEET")
else:
    print("MUTE")