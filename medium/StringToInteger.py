class Solution:
    def myAtoi(self, s: str) -> int:
        num = ["0"]
        negpos = 1
        index = 0
        exp = 0

        while (index < len(s) - 1 and s[index] == " "):
            index += 1

        if (index < len(s) - 1 and s[index] == "-"):
            negpos = -1
            index += 1
            if index < len(s) - 1 and s[index] == "+":
                return 0
        if (index < len(s) - 1 and s[index] == "+"):
            index += 1
        if (index < len(s) - 1 and s[index] == "0"):
            index += 1

        start = index
        while (start <= len(s) - 1):
            if (s[start].isnumeric()):
                exp += 1
                start += 1
            else:
                break

        mult = 10 ** (exp - 1)
        mult = int(mult)
        
        while (index <= len(s) - 1 and s[index].isnumeric()):
            num.append(s[index])
            index += 1

        num = int(''.join(num))
        if int(num * negpos) < (2147483648 * -1):
            return (2147483648 * -1)
        if int(num * negpos) > 2147483647:
            return 2147483647
        return int(num * negpos)


        