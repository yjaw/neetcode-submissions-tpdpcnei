class Solution:
    def isPalindrome(self, s: str) -> bool:
        string_list = []
        for c in s:
            if c.isalnum():
                string_list.append(c.lower())
        
        new_string = "".join(string_list)
        print(new_string)
        return new_string == new_string[::-1]
         



        
        