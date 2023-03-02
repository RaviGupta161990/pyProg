finals = ""
s = "aaabbccaad"
i = 0

while i < len(s)-1:

    if s[i] == s[i + 1]:
        s = s[:i]+s[i+2:]

    else:
        i += 1
    print(f"s:{s} and finals:{final}")

