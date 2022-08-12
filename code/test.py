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
s.solve()

#test case 2
huaxing=User(0)
sisi=User(1)
yunxiao=User(2)
yufei=User(3)

huaxing.followOne(sisi)
sisi.followOne(yunxiao)
yunxiao.followOne(yufei)
yufei.followOne(huaxing)

g=[huaxing,sisi,yunxiao,yufei]
t=scc(g)
t.solve()


#test case 3
aa=User(0)
bb=User(1)
cc=User(2)
dd=User(3)
aa.followOne(bb)
bb.followOne(cc)
cc.followOne(dd)

v=scc([aa,bb,cc,dd])
v.solve()