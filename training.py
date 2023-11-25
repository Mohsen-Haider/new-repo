# F2 : rename
#  Ctrl + ذ  :  Terminal 
# This is new comment at 9:52
x=[23,26,30,34,43,48,52,57,58] 
y=[651,762,856,1063,1190,1298,1421,1440,1518]

meanx=meany=0
for i in range(len(x)):
    meanx+=x[i]
    meany+=y[i]
meanx/=len(x)
meany/=len(y)

varx=vary=covxy=0
for i in range(len(x)):
    varx+=(x[i]-meanx)**2
    vary+=(y[i]-meany)**2
    covxy+=(x[i]-meanx)*(y[i]-meany)
varx/=(len(x)-1)
vary/=(len(y)-1)
covxy/=(len(y)-1)

beta=covxy/varx
a=meany-(beta*meanx)
Expectedy=[]
R2=Sumofresidual=sstotal=0
for i in range(len(y)):
    sstotal+=(y[i]-meany)**2
    Sumofresidual+=(y[i]- (beta*x[i]+a) )**2
R2=1-(Sumofresidual/sstotal)
print("R2: ",R2)

corrolation=covxy/( (varx)**(0.5) * (vary)**(0.5) )
print("corrolation: ",corrolation)

import math
corrolation=beta*(math.sqrt(varx)/math.sqrt(vary))
print("corrolation: ",corrolation)

#############  

# Confusion Metrics ( Model Evaluation metrics )
TP=142
FP=22
FN=29
TN=110
Total=TP+FP+FN+TN
accurcy=(TP+TN)/Total
precision=(TP)/(TP+FP)
recall=(TP)/(TP+FN)         # If we talk about Positive Recall But For Negative Recall recall=(TN)/(TN+FP)
F1Score=2/( (1/recall) + (1/precision) )
# Note: Sensitivity --> Positive Recall     AND   (Specifiaty) -->   Negative Recall

########  

# Normalization  
# We should normalized all The values To Make There values in the range (0 , 1) 
# NormXi=( Xi -MinX )/ ( Maxx - Minx )
X=2206
Minx=1800
Maxx=3000
NormalizedValueX= (X-Minx)/(Maxx-Minx)


############

#  Z-Score (Standrization) 
# Making the meanx=0 And STDx=1    
# Note: STDx = sqrt(varx) = sigmax
# We should Z-Score all The values To Make the properities in Stadard Normal Distirbution 
# by Making the meanx=0 And STDx=1     .        Zi = ( Xi - meanx)/math.sqrt(varx)

Z = ( X - meanx)/math.sqrt(varx)



#########

# optimizing the error--> finding better values for alpha and Beta.

# Gradient Descent:
# Gradient Descent: Our Goal is to find values for Alpha and Beta that Minimize the error

# note that the size ofthe step we take is determined by the learning rate.
#  N --> Learning Rate, 



# This is new update at 9:49 25/11/2023 