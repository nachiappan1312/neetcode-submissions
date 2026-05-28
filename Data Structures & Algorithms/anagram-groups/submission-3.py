from collections import defaultdict, Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output_dict = defaultdict(list)
        for word in strs:
            w_ctr = ''.join(sorted(word))
            output_dict[w_ctr].append(word)
        return list(output_dict.values())



        