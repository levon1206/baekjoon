string = input()
string_len = len(string)
part_set = set()

for i in range(string_len) :
    for j in range(i, string_len) :
        part_set.add( string[ i : j + 1 ] )

print(len(part_set))
