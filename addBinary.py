class Solution(object):
    def addBinary(self, a, b):
        i = 0
        a = a[::-1]
        b = b[::-1]
        carry_num = 0
        stringer = ""
        while i < len(a) and i < len(b):
            if a[i] == '1' and b[i] == '1':

                if carry_num == 1:
                    stringer = '1' + stringer
                else:
                    stringer = '0' + stringer
                    carry_num = 1
            elif (a[i] == '0' and b[i] == '1') or (a[i] == '1' and b[i] == '0'):
                if carry_num == 1:
                    stringer = '0' + stringer
                else:
                    stringer = '1' + stringer
            elif a[i] == '0' and b[i] == '0':
                if carry_num == 1:
                    stringer = '1' + stringer
                else:
                    stringer = '0' + stringer
                carry_num = 0
            i += 1

        while i < len(a):
            # print carry_num
            print
            stringer
            if carry_num == 1 and a[i] == '1':
                stringer = '0' + stringer
                carry_num = 1
            elif carry_num == 0 and a[i] == '0':
                stringer = '0' + stringer
                carry_num = 0
            else:
                stringer = '1' + stringer
                carry_num = 0
            i += 1

        while i < len(b):
            if carry_num == 1 and b[i] == '1':
                stringer = '0' + stringer
                carry_num = 1
            elif carry_num == 0 and b[i] == '0':
                stringer = '0' + stringer

            else:
                stringer = '1' + stringer
                carry_num = 0
            i += 1
        if carry_num != 0:
            stringer = '1' + stringer
        return stringer
        """
        :type a: str
        :type b: str
        :rtype: str
        """
