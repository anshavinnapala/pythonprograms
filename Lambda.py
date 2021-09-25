from functools import reduce

nums=[3,2,8,9,6,7,4,5,3,2]

even=list(filter(lambda n:n%2==0, nums))

doubles=list(map(lambda n:n*2, even))

print(doubles)

sum=reduce(lambda a,b:a+b, doubles)
print(sum)
