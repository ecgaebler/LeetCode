def remove_duplicates(string):
    seen = set()
    read_index, write_index = 0, 0
    while read_index < len(string):
        if string[read_index] not in seen:
            seen.add(string[read_index])
            string[write_index] = string[read_index]
            write_index += 1
        read_index += 1
    while len(string) > write_index:
        string.pop()
    return string
