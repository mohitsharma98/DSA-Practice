from collections import Counter
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if(len(s) < len(t)):
            return ""
        
        left, right = 0, 0
        s = list(s)
        t = Counter(t)
        min_list = -1
        deleted_vals = {}
        cur_list = {}
        while(right < len(s)):
            if(s[right] in t):
                if(s[right] in deleted_vals):
                    deleted_vals[s[right]] = deleted_vals[s[right]] + 1
                else:
                    deleted_vals[s[right]] = 1
                if(t[s[right]] == 1):
                    del t[s[right]]
                else:
                    t[s[right]] = t[s[right]] - 1
            
            if(s[right] in cur_list):
                cur_list[s[right]] = cur_list[s[right]] + 1
            else:
                cur_list[s[right]] = 1
            
            if(len(t) == 0):
                
                
                if(min_list == -1):
                    min_list = [left, right]
                else:
                    if(min_list[1]-min_list[0]+1 > right - left + 1):
                        min_list = [left, right]
                        
                while(left < right):
                    
                    if(cur_list[s[left]] == 0):
                        
                        cur_list.remove(s[left])
                    else:
                        cur_list[s[left]] = cur_list[s[left]] - 1
                    
                    if(s[left] in deleted_vals and deleted_vals[s[left]] > cur_list[s[left]]):
                        if(s[left] not in t):
                            t[s[left]] = 1
                        else:
                            t[s[left]] = t[s[left]] + 1
                        
                        
                        deleted_vals[s[left]] = deleted_vals[s[left]] - 1
                        
                        left += 1
                        break
        
                    left += 1
                    

                    if(len(t) == 0):
                        if(min_list[1]-min_list[0]+1 > right - left + 1):
                            min_list = [left, right]
                    else:
                        break
            right += 1
            
        if(min_list == -1):
            return ""
        
        return "".join(s[min_list[0]:min_list[1]+1])