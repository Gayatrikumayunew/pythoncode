# def funargs(*args):
#     for item in args:
#         print(item)
#
#
# har = ["harry", "skills", "hekko", "gia"]
# funargs(*har)
# print(type(har))

"""for sending normal argument the sequence is (normal , args , kwargs)"""


def funargs(normal, *args, **kwargs):
    print(normal)
    for item in args:
        print(item)
    print("\n our heros")
    for key, value in kwargs.items():
        print(f"(key) is a (value)")


har = ["harry", "rji", "ueb", "ubs"]
normal = "ho"
kw = {
    "ksjfd"" moniter", "harry" " coder", "gayu" " learner"
}
funargs(normal, *har, *kw)






