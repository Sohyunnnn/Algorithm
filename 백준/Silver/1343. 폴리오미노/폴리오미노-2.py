pol= input()

if "XXXX" in pol:
  pol = pol.replace("XXXX", "AAAA")
if "XX" in pol:
  pol = pol.replace("XX", "BB")
if "X" in pol: 
  pol = -1

print(pol)
