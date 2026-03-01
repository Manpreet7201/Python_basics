# Take 5 names from user and store only unique ones.
myset = set()
sub_len = 5
for i in range(0, sub_len):
    take_ip = input("Write any name- ")
    myset.add(take_ip)

print(myset)