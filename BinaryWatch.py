# A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59).

# Each LED represents a zero or one, with the least significant bit on the right.

# Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible times the watch could represent.

# Example:

# Input: n = 1
# Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
# Note:
# The order of output does not matter.
# The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".
# The minute must be consist of two digits and may contain a leading zero, for example "10:2" is not valid, it should be "10:02".

# 位运算（Bit Manipulation）
# 10盏灯泡的燃亮情况可以通过0-1024进行表示，然后计数二进制1的个数即可。
# 利用位运算将状态拆分为小时和分钟。

class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        ans = []
        for x in range(1024):
            if bin(x).count('1') == num:
                h, m = x >> 6, x & 0x3F
                if h < 12 and m < 60:
                    ans.append('%d:%02d' % (h, m))
        return ans

# 另一种解法，参考LeetCode Discuss：https://discuss.leetcode.com/topic/59374/simple-python-java
# 枚举小时h和分钟m，然后判断二进制1的个数是否等于num

class Solution2(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        ans = []
        for h in range(12):
            for m in range(60):
                if (bin(h)+ bin(m)).count('1') == num:
                    ans.append('%d:%02d' % (h, m))
        return ans


# 方法3

class Solution3(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        # hh_summary, mm_summary = self.get_summary()
        hh_summary = {
            0: [0],
            1: [1, 2, 4, 8],
            2: [3, 5, 6, 9, 10],
            3: [7, 11],
        }
        mm_summary = {
            0: [0],
            1: [1, 2, 4, 8, 16, 32],
            2: [3, 5, 6, 9, 10, 12, 17, 18, 20, 24, 33, 34, 36, 40, 48],
            3: [7, 11, 13, 14, 19, 21, 22, 25, 26, 28, 35, 37, 38, 41, 42, 44,
                49, 50, 52, 56],
            4: [15, 23, 27, 29, 30, 39, 43, 45, 46, 51, 53, 54, 57, 58],
            5: [31, 47, 55, 59],
        }

        valid_time = []
        for hh in range(num + 1):
            mm = num - hh
            valid_hh = hh_summary.get(hh, [])
            valid_mm = mm_summary.get(mm, [])
            for h in valid_hh:
                for m in valid_mm:
                    valid_time.append('{0}:{1:02d}'.format(h, m))
        return valid_time