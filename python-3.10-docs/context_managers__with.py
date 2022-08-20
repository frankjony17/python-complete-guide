# Parenthesized Context Managers:
"""
with (CtxManager() as example):
    ...

with (
    CtxManager1(),
    CtxManager2()
):
    ...

with (CtxManager1() as example,
      CtxManager2()):
    ...

with (CtxManager1(),
      CtxManager2() as example):
    ...

with (
    CtxManager1() as example1,
    CtxManager2() as example2
):

# it is also possible to use a trailing comma at the end of the enclosed group:
with (
    CtxManager1() as example1,
    CtxManager2() as example2,
    CtxManager3() as example3,
):
"""
from x_utils import ContextManager, context

with open('data.txt') as f:
    data = f.readlines()
    print(int(data[0]))

# 1 --------------------------------------------------------------------------------------------------------------------

with context as ctx:
    # use the object
    pass
# context is cleaned up

# 2 --------------------------------------------------------------------------------------------------------------------

with ContextManager() as ctx:
    # do something
    pass
# done with the context
