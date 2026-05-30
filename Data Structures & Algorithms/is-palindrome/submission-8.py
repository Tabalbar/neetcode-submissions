class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r = 0,len(s)-1
        js = "".join(s.lower())
        while(l < r):
            print(js[l], js[r])
            if not js[l].isalnum():
                l += 1
                continue
            elif not js[r].isalnum():
                r -= 1
                print("continue")
                continue
            elif js[l] != js[r]:
                return False
            else:
                l+=1
                r-=1
            
        return True