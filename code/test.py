from scc import scc
from user import User

#test case 1
a=User(0)
b=User(1)
c=User(2)
d=User(3)
e=User(4)

d.followOne(a)
e.followOne(d)
a.followOne(b)
b.followOne(c)
c.followOne(a)

s=scc([a,b,c,d,e])

print(s.solve())


huaxing=User(0)
sisi=User(1)
yuxiao=User(2)
yufei=User(3)

huaxing.followOne(sisi)
sisi.followOne(yuxiao)
yuxiao.followOne(yufei)

v=scc([huaxing,sisi,yuxiao,yufei])
print(v.solve())
