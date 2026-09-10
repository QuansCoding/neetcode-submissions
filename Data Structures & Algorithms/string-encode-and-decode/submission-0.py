class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s))) # length of string
            res.append("#")
            res.append(s)
        return "".join(res) # joins result into a single string
        #formatted like 3#c3#a3#t as cat
    def decode(self, s: str) -> List[str]:
        res = []

        i = 0

        while i <len(s): 
            j = i
            while s[j] != '#': #moves j pointer until it reaches #
                j +=1
            # converts substring into an integer (since formatted as num# we will get num)
            length = int(s[i:j]) 

            i = j+1 #i becomes the char after the #
            j = i+ length #j moves past the word itself

            #appends substring starting at i (char after #) up until (but not including) j
            res.append(s[i:j]) 
            i=j #now sets current i to j
        
        return res
