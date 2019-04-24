import operator as op

a = 5
b = 3

print('add : ',op.add(a,b))
print('sub : ',op.sub(a, b))
print('mul : ',op.mul(a, b))
print('true div : ',op.truediv(a,b))   # a/b
print('floor div : ',op.floordiv(a,b)) # a//b
print('pow : ',op.pow(a,b))  # a**b
print('MOD : ',op.mod(a,b))


#lt () : less than
# using lt() to check if a is less than b
if(op.lt(a,b)):
    print (str(a)+" is less than "+str(b))
else :
    print (str(a)+" is not less than "+str(b))

#le () : less than or equal
# using le() to check if a is less than or equal b
if(op.le(a,b)):
    print (str(a)+" is less than or equal to "+str(b))
else :
    print (str(a)+" is not less than or equal to "+str(b))

#eq () : equal
#using eq() to check if a is equal to b
if (op.eq(a,b)):
    print (str(a)+" is equal to "+str(b))
else :
    print (str(a)+" is not equal to "+str(b))


#Similarly goes for :
# gt() : greater than
# ge() : greater than or equal to
# ne() : not equal 