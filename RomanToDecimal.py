class Solution(object):
    def romanToInt(self, s):
        index = len(s)
        list = []
        ans = []
        result=0
        for a in s:
            if s[index-1] == 'M':
                list.append(1000)
            if s[index-1] == 'D':
                list.append(500)
            if s[index-1] == 'C':
                list.append(100)
            if s[index-1] == 'L':
                list.append(50)
            if s[index-1] == 'X':
                list.append(10)
            if s[index-1] == 'V':
                list.append(5)
            if s[index-1] == 'I':
                list.append(1)
            index-=1
        index = 0
        for a in list:
            if index == len(list)-1:
                ans.append(list[index])
                break
            elif list[index] < list[index+1]:
                ans.append(list[index])
                if index < len(list)-1:
                    index+=1
            elif list[index] == list[index+1]:
                ans.append(list[index])
                index+=1
            else:
                ans.append(list[index]-list[index+1])
                if index < len(list)-2:
                    index+=2
                else:
                    break

        for a in ans:
            result+=a
        return result

converter = Solution()
print(converter.romanToInt("IV"))