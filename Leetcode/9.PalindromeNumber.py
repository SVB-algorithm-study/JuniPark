def isPalindrome(self, x: int) -> bool:
        # 배열 뒤에서부터 세기
        # if str(x)[::-1] == str(x) : 
        #     return ('true')
        return str(x)[::-1] == str(x)