x="hello my darling"
y=list(x)
y[0],y[1]=y[1],y[0]
swap=" ".join(y)
print(swap)