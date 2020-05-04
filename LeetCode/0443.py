class Solution:
    def compress(self, chars: List[str]) -> int:
        if not chars:
            return 0
        char_count = 0
        write_idx = 0
        current_char = chars[0]
        
        for scan_idx in range(0, len(chars)):
            if chars[scan_idx] == current_char:
                char_count += 1
            else:
                if char_count > 1:
                    chars[write_idx] = current_char
                    write_idx += 1
                    temp = str(char_count)
                    for char in temp:
                        chars[write_idx] = char        
                        write_idx += 1
                else:
                    chars[write_idx] = current_char
                    write_idx += 1
                char_count = 1
                current_char = chars[scan_idx]
                
        if char_count > 1:
            chars[write_idx] = current_char
            write_idx += 1
            temp = str(char_count)
            for char in temp:
                chars[write_idx] = char       
                write_idx += 1
        else:
            chars[write_idx] = current_char
            write_idx += 1
        del chars[write_idx:]
        return len(chars)