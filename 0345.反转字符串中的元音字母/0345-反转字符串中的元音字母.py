class Solution:
    def reverseVowels(self, s: str) -> str:
        VOWELS = set("aeiouAEIOU")
        l = [char for char in s]
        left, right = 0, len(s) - 1
        while 1:
            while left < right and l[left] not in VOWELS:
                left += 1
            
            while left < right and l[right] not in VOWELS:
                right -= 1

            if left >= right:
                break

            l[left], l[right] = l[right], l[left]
            left += 1
            right -= 1
        return "".join(l)

            
