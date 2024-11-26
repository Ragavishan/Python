zork=0
sum=0
print('Before',sum,zork)
for thing in[6,32,67,88,12,17]:
    zork=zork+1
    sum=sum+thing
    print(zork,sum,thing)
    print('After',sum,zork,zork/sum)