class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sn=len(s)
        tn=len(t)
        if sn!=tn:
            return False
        
        smap={}
        for i in range(sn):
            smap[s[i]]=smap.get(s[i],0)+1
        
        tmap={}
        for i in range(tn):
            tmap[t[i]]=tmap.get(t[i],0)+1

        if smap!=tmap:
            return False
        return True