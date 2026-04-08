class Solution:

    def encode(self, strs: List[str]) -> str:
        e=""
        for s in strs:
            e+=str(len(s))+'#'+s
        return e
    def decode(self, s: str) -> List[str]:
        res=[]
        p=0
        while p<len(s):
            j=p
            while s[j]!="#":
                j+=1
            l=int(s[p:j])
            res.append(s[j+1:j+1+l])
            p=j+1+l
        return res
    

    