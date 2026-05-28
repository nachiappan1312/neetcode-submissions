from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counter = Counter(s)
        t_counter = Counter(t)
        for ch,cnt in s_counter.items():
            print(ch, s_counter[ch], t_counter[ch])
            if ch not in t_counter or s_counter[ch]!=t_counter[ch]: return False
            del t_counter[ch]
        print( len(t_counter))
        return len(t_counter) == 0


        