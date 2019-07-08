import module1 as m1
import module2 as m2
# 导入module3时 不会执行模块中if条件成立时的代码 因为模块的名字是module3而不是__main__
# import module3

m1.foo()
m2.foo()
