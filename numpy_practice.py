import numpy as np
import matplotlib.pyplot as plt
import time

a=np.zeros(4)   
print(f"np.zeros(4): a={a}","a shape= ",{a.shape},"datatype=",{a.dtype}) #the shape is (4,)

a=np.zeros(4,)
print(f"np.zeros(4,):a={a}","a shape=",{a.shape},"datatype=",{a.dtype}) #same as above

a=np.random.random(4)
print(f"np.random.random(4):a={a}","a shape=",{a.shape},"datatype=",{a.dtype}) #the shape is (4,)

a=np.arange(4.)
print(f"np.arange(4.):a={a}","a shape=",{a.shape},"datatype=",{a.dtype}) #the shape is (4,)  arange(start,stop,step)

a=np.random.random(4)
print(f"np.random.random(4):a={a}","a shape=",{a.shape},"datatype=",{a.dtype}) #the shape is (4,) it means 4 random number between 0 and 1

a=np.array([5,4,3,2,1])
print(f"np.array([5,4,3,2,1]):a={a}","a shape=",{a.shape},"datatype=",{a.dtype}) #the shape is (5,)

a=np.array([5.,4,3,2,1])
print(f"np.array([5.,4,3,2,1]):a={a}","a shape=",{a.shape},"datatype=",{a.dtype}) #the shape is (5,) 5.0 means float

a=np.arange(10)
print(f"np.arange(10):a={a}","a shape=",{a.shape},"datatype=",{a.dtype}) #the shape is (10,)

#to access element in numpy array
print(f"a[6].shape=",{a[6].shape},"datatype=",a[6].dtype,"a[6]={a[6]}") #access the 6th 

print(f"a[-1]={a[-1]}")   #access the last element

try:
    c=a[10]
except IndexError as e:
    print("IndexError:",e)

#practice slicing
a=np.arange(10)
print(f"a={a}")

c=a[2:5:1] #slicing from index 2 to 5(not include 5) with step 1
print(f"c=a[2:5:1]: c={c}")

c=a[2:5:2] #slicing from index 2 to 5(not include 5) with step 2
print(f"c=a[2:5:2]: c={c}")

c=a[4:] #slicing from index 4 to the end
print(f"c=a[4:]: c={c}")

c=a[:4] #slicing from the sart to index 4(not include 4)
print(f"c=a[:4]: c={c}")

c=a[:]  #slicing the whole array
print(f"c=a[:]: c={c}")

#vector operations
a=np.array([1,2,3,4,5])

b=-a
print(f"b=-a: b={b}")  #negation all elements

b=sum(a)
print(f"b=sum(a): b={b}")  #sum of all elements

b=np.mean(a)
print(f"b=np.mean(a): b={b}")  #mean of all elements equal to sum(a)/len(a)

b=a**2
print(f"b=a**2: b={b}")  #square each element

a=np.array([1,2,3,4,5,6])
b=np.array([-1,-2,-3,4,5,6])
c=a+b
print(f"c=a+b: c={c}")  #element wise addition

d=np.array([1,2])

try:                        #   this will raise ValueError because the two arrays shapes are not compatible for broadcasting
    e=a+d
except ValueError as e:
    print("ValueError:",e)    # shapes (6,) and (2,) not aligned: 6 (dim 0) != 2 (dim 0)


a=np.array([1,2,3,4,5])
b=5*a
print(f"b=5*a: b={b}")  #scalar multiplication

def my_dot(a,b):         # Compute the dot product of two vectors
    x=0
    for i in range (a.shape[0]):
       x=x+a[i]*b[i]
    return x
                                 
a=np.array([1,2,3])   #assume both a and b are 1-D arrays
b=np.array([4,5,6])                                         
c=my_dot(a,b)
print(f"c=my_dot(a,b): c={c}")  #dot product using custom function


a=np.array([1,2,3])
b=np.array([4,5,6])
c=np.dot(a,b)                     #that is very efficient to use in linear algebra computation especially for large arrays and many features
                                  #it very fast because it is implemented in C language internally
print(f"c=np.dot(a,b): c={c},c.shape={c.shape}")  #dot product using numpy function


np.random.seed(0)   #set the random seed for reproducibility
a=np.random.random((1000000))  
b=np.random.random((1000000))
start=time.time()  
c=np.dot(a,b)      #element wise multiplication
end=time.time()
print(f"c=np.dot(a,b): c={c:4f}" and f"Time taken using np.dot: {end-start:4f} seconds")  #dot product using numpy function


start=time.time()
c=my_dot(a,b)
end=time.time()
print(f"c=my_dot(a,b): c={c:4f}" and f"Time taken using my_dot: {end-start:4f} seconds")  #dot product using custom function




#about matrix
a=np.zeros((1,5))# 2D array with 1 row and 5 columns
print(f"np.zeros((1,5)): a={a}","a shape=",{a.shape},"datatype=",{a.dtype}) #the shape is (1,5)

a=np.zeros((3,4)) # 2D array with 3 rows and 4 columns
print(f"np.zeros((3,4)): a={a}","a shape=",{a.shape},"datatype=",{a.dtype}) #the shape is (3,4)

a=np.random.random_sample((1,1))    # 2D array with 1 row and 1 column ((1,1))is tuple ((1,))is 1D array 
print(f"np.random.random_sample((1,1)): a={a}","a shape=",{a.shape},"datatype=",{a.dtype}) #the shape is (1,1)

a=np.array([[1],[2],[3]])   # 2D array with 3 rows and 1 column
print(f"np.array[[1],[2],[3]]: a={a}","a shape=",{a.shape},"datatype=",{a.dtype}) #the shape is (3,1)

a=np.array([[1],
            [2],
            [3]]
)   # 2D array with 3 rows and 1 column
print(f"np.array[[1],[2],[3]]: a={a}","a shape=",{a.shape},"datatype=",{a.dtype}) #the shape is (3,1)

a=np.arange(6).reshape(-1,2) # reshape 1D array to 2D array with 1 row and 2 columns or 2 elements per row,the -1 means automatically calculate the number of rows based on the number of elements and columns
print(f"np.array(6).reshape(-1,2): a={a}","a shape=",{a.shape}) #the shape is (1,2)
#access element in 2D array
print(f"a[0,2]: a[0,2]={a[0,1]}") # access element at row 0,column 2      
                                  #  0  1
                                  #  2  3   
                                  #  4  5           
print(f"a[2,0]: a[2,0]={a[2,0]}") # access element at row 2,column 0   
      
a=np.arange(20).reshape(-1,10)  # reshape 1D array to 2D array with 2 rows and 10 columns

#access 5 consecutive elements (start:stop:step)
print("a[0, 2:7:1] = ", a[0, 2:7:1], ",  a[0, 2:7:1].shape =", a[0, 2:7:1].shape, "a 1-D array")
        #0th row, from index 2 to 7 (not include 7) with step 1
        # 0  1  2  3  4  5  6  7  8  9
        #10 11 12 13 14 15 16 17 18
       #  result=[2 3 4 5 6]
print("a[:, 2:7:1] = \n", a[:, 2:7:1], ",  a[:, 2:7:1].shape =", a[:, 2:7:1].shape, "a 2-D array") # all rows, from index 2 to 7 (not include 7) with step 1
       # all rows, from index 2 to 7 (not include 7) with step 1
         #  0  1  2  3  4  5  6  7  8  9
            #10 11 12 13 14 15 16 17 18
         #  result=[[ 2  3  4  5  6]
x=np.arange(10)
y=2*x+3            #linear function y=2x+3
plt.scatter(x,y,label="Data points")   # scatter plot and label
plt.plot(x,y,label="Linear function",linewidth=2)       #line plot and label
plt.title("y=2x+3") #title
plt.xlabel("x-axis") #x-axis label
plt.ylabel("y-axis") #y-axis label
plt.legend()  #show legend
plt.show() 
plt.savefig("linear_function.png")  #save the plot as png file