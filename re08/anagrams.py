# -*- coding: utf-8 -*-
"""
Created on Dom Nov 25 20:30:31 2018

@author: laureano
"""
def anagrams(alist):
    result=[]
    cont=0
    for i in alist:
        result.append([])
        result[cont].append(i)
        resul=[]
        for j in alist:
            if i!=j:
                dx= list(i.lower().replace(" ",""))
                dx.sort()
                print(dx)
                dy= list(j.lower().replace(" ",""))
#                print(dy)
                dy.sort()
                if dx==dy:
                    resul.append(i)
                    resul.append(j)
                    alist.remove(j)
        for k in resul:
            if k not in result[cont]:
                result[cont].append(k)
        result[cont]=sorted(result[cont])
        cont+=1
    result=sorted(result, key=lambda r:r[0].lower())            
    return result
    
alist = ["sentence", "lives", "ten scene", "bat", "Elvis", "CE sennet"]
print(anagrams(alist))






