class MinStack:

    def __init__(self):
        self.st=[]
        self.mini=[]

    def push(self, val: int) -> None:
        if len(self.st)==0:
            self.m=val
        self.st.append(val)
        if val<self.m:
            self.m=val
        self.mini.append(self.m)
    def pop(self) -> None:
        self.st.pop()
        self.mini.pop()
        if len(self.st)>0:
            self.m=self.mini[-1]

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.mini[-1]
