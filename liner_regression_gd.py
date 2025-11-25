import numpy as np
import matplotlib.pyplot as plt

x=np.array([1,2,3,4,5])    #input feature
y=np.array([100,150,200,250,300])  #target value

def cost_function(x,y,w,b):            #to calculate how well our model is performing,how close we choose the w and b to actural data
    m=x.shape[0]                       #number of training examples
    cost=0                               
    for i in range(m):                 #loop over all training examples
        f_wb=w*x[i]+b                   #linear function
        cost=cost+(f_wb-y[i])**2        #squared error
    cost=cost/(2*m)                    #mean squared error
    return cost
        
m=cost_function(x,y,50,50)
print(f"Initial cost at w=50,b=50 is {m}")     


def coumpute_gradient(x,y,w,b):    # to comptue the derivative of cost function with respect to w and b
    m=x.shape[0]                    # this functon was sovled the derivative of 1/m*sum((f_wb-y)*x[i]) and 1/m*sum(f_wb-y)
    dj_dw=0
    dj_db=0
    
    for i in range(m):
        f_wb=w*x[i]+b
        dj_dw+=(f_wb-y[i])*x[i]
        dj_db+=(f_wb-y[i])
    dj_dw=dj_dw/m
    dj_db=dj_db/m
    return dj_dw,dj_db    



def gradient_descent(x,y,w,b,rate,counter,cost_function,coumpute_gradient): #rate is learning rate,counter is number of iterations
    cost_history=[]                    #the history of cost function value
    param_history=[]                   #the history of parameter w and b
    for i in range(counter):
        dj_dw,dj_db=coumpute_gradient(x,y,w,b)  #compute the gradient
        w=w-rate*dj_dw                       #update w 
        b=b-rate*dj_db                       #update b
        if i<1000:                          #record the cost and parameter history for first 1000 iterations
            cost=cost_function(x,y,w,b)
            cost_history.append(cost)
            param_history.append([w,b])

    return w,b,cost_history,param_history

m=gradient_descent(x,y,2,3,0.01,1000,cost_function,coumpute_gradient)
print(f"w is {m[0]},b is {m[1]}")
plt.plot(m[2])
plt.xlabel("iterration")
plt.ylabel("cost")
plt.title("cost function history")
plt.show()

#example usage for many features of x and use dot product to compute the linear function
x=np.array([[500,1,2,35],[700,2,2,40],[800,3,3,45]])
y=np.array([150,200,250])
w_init=np.array([1,0.1,-0.1,-1])
b_init=20
def predict(x,w,b):
    m=x.shape[0]
    p=0
    for i in range(m):
       c=w[i]*x[i]
       p+=c
    p=p+b
    return p
x_input=x[0,:]

predicted_value=predict(x_input,w_init,b_init) 
print(f"predicted_value is {predicted_value}")      

#efficient way to predict for many samples
def predict2(x,w,b):
    m,n=x.shape
    predictions=[]
    for i in range(m):
        p=0
        for j in range(n):
            p+=w[j]*x[i,j]
        predictions.append(p+b)
    return np.array(predictions)       



#efficient way to predict using numpy dot product
def predict3(x,w,b):
    return np.dot(x,w)+b    


#or 
def predict4(x,w,b):
    return x @ w + b
predicted_values=predict2(x,w_init,b_init)