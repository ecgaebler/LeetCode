class Solution:
    def decodeString(self, s: str) -> str:
        """ decode a string """
        def decode_chars(char_list):
            """ decode a list of chars """
            result = []
            digits = set(str(_) for _ in range(10))
            count_list = []
            bracket_num = 0 #+1 for open brackets, -1 for close brackets
            temp = []
            for char in char_list:
                if char == "[":
                    if bracket_num > 0:   #we still have unclosed brackets
                        temp.append(char) #include bracket in temp string
                    bracket_num += 1
                elif char == "]":
                    bracket_num -= 1
                    if bracket_num > 0:   #brackets still not closed
                        temp.append(char) #keep adding to substring
                    else: #this bracket closes a substring
                        decoded_substring = decode_chars(temp) #recurse on substring
                        count = int(''.join(count_list))
                        count_list = [] #reset count_list
                        temp = []       #reset temp substring
                        result.extend(count*(decoded_substring))
                else:
                    if bracket_num > 0:
                        temp.append(char)
                    else:
                        if char in digits:
                            count_list.append(char) #build char list representing an int
                        else:
                            result.append(char)
            return result
        
        return ''.join(decode_chars(list(s)))
                    