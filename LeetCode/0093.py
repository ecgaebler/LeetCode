class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def get_ips(dots, digits, calc_d):
            if (dots, digits) in calc_d:
                return calc_d[(dots, digits)]
            
            if dots >= len(digits): #too short to fit remaining dots
                return []
            
            if dots == 0:
                if (len(digits) > 3 or int(digits) > 255 or 
                   (len(digits) > 1 and digits[0] == "0")):
                    calc_d[(dots, digits)] = []
                    return []
                    
                calc_d[(dots, digits)] = [digits]
                return [digits]
            result = []
            
            if len(digits) > 1:
                for ip in get_ips(dots - 1, digits[1:], calc_d):
                    result.append(digits[:1] + "." + ip)
                    
            if len(digits) > 2 and digits[0] != "0":
                for ip in get_ips(dots - 1, digits[2:], calc_d):
                    result.append(digits[:2] + "." + ip)
                    
            if len(digits) > 3 and digits[0] != "0" and int(digits[:3]) <= 255:
                for ip in get_ips(dots - 1, digits[3:], calc_d):
                    result.append(digits[:3] + "." + ip)
                    
            calc_d[(dots, digits)] = result
            return result
        
        dp_ips = {}
        return get_ips(3, s, dp_ips)
        
                
            
            