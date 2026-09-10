class Solution:
    def read(self, buf, n):
        result = []

        while len(result) < n:
            temp = [''] * 4
            count = read4(temp)

            if count == 0:
                break

            for i in range(min(count, n - len(result))):
                result.append(temp[i])

        for i in range(len(result)):
            buf[i] = result[i]

        return len(result)
