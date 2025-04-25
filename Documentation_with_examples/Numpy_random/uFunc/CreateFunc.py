import numpy as np

# Create a uFunc that adds two arrays element-wise
def myadd(x, y):
    return x + y

# Create a uFunc from the function
myadd = np.frompyfunc(myadd, 2, 1)

print(myadd(np.array([1, 2, 3]), np.array([4, 5, 6])))

# Now we neeed to check if the function is a uFunc
print(type(myadd))
#This will print <class 'numpy.ufunc'>, indicating that myadd is a uFunc

#Now im gonna show you what is not a uFunc

print(type(np.concatenate))
#This will print <class 'function'>, indicating that np.concatenate is not a uFunc

if type(myadd) == np.ufunc:
    print("myadd is a uFunc")
else:
    print("myadd is not a uFunc")
#This will print "myadd is a uFunc"