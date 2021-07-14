"""Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once."""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}
        for i in strs:
            if ("".join(sorted(i)) in m.keys()):
                m["".join(sorted(i))].append(i)
            else:
                m["".join(sorted(i))] = [i]
                
        return list(m.values())