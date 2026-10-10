class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        # prefix length w str length and #
        for i in strs: 
            res += str(len(i))+ "#" + i 
        return res

    def decode(self, s: str) -> List[str]:
        res=[]
        i= 0

        while i < len(s) :
            j = i
             
            while s[j] != "#":
                j+= 1

            # extract str lenth and convert to int for word extraction
            strlen = int(s[i:j])

            # Extract word
            word = s[j+1:j+1+strlen]
            res.append(word)

            # jump i to next str prefix index
            i = j+1 + strlen

        return res



            

                

        
            