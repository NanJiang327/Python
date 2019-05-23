# hannao
def fun(n, x, y, z):
    if n == 1:
        print(x, ' -->', z)
    else:
        fun(n-1, x, z, y)  # 前n - 1个盘子从x移动到y上
        print(x, ' --> ', z)  # 将最底下的最后一个盘子从x移动到z上
        # 将前y上的n-1歌盘子移动到z上
        fun(n-1, y, x, z)

# 0.
# num to bin
def numtobim(num):
    num % 2


def get_digits(n):
