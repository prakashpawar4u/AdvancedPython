# def f():
#     s ="local variable"
#     print(s)
#
# #driver code
# f()


# def f():
#     print("Inside Function",s)
#     print(s)
#
# #driver code
# #global scope
# s ="Global Variable"
# f()
# print("outside Function", s)





def f():
    global s
    s += 10
    print("Inside func :: ",s)
    s = "New value"
    print(s)
