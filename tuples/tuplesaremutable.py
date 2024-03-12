tuple=(1,2,3,['pthon','java'],(2,4,6,8))
# tuple[3]=[1,2,3,]      #TypeError: 'tuple' object does not support item assignment
tuple[3][1]=24
print(tuple)
tuple[3][0]=212003
print(tuple)