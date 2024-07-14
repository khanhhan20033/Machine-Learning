import numpy as np
import matplotlib.pyplot as plt

N = 400


def _init_(x, k):
    return x[np.random.choice(N, k)]


def assign_label(X, centroids, k):
    result = np.zeros((X.shape[0], centroids.shape[0]))

    for i in range(X.shape[0]):
        for j in range(centroids.shape[0]):
            #print(np.sqrt((X[i] - centroids[j]) ** 2))
            t = np.sqrt(np.sum((X[i] - centroids[j]) ** 2))
            result[i,j]=t
    #print(result)
    return np.argmin(result,axis=1)


def find_centroids(X, labels, k):
    centers = np.zeros((k, X.shape[1]))
    for i in range(k):
        # centers[i] = np.mean(X[labels == i])
        temp = np.zeros((1, 2))
        count = 0
        for j in range(labels.size):

            if labels[j] == i:
                count += 1
                temp += X[j]
        temp /= count
        centers[i] = temp
    return centers


def has_converged(centers, new_centers):
    count = 0
    for i in centers:
        for j in new_centers:
            if set(i) == set(j):
                count += 1
                break
    return count == len(centers)

def plot_k_means(X,labels,k):
    lst=[]
    colors=['r','g','b']
    for i in range(k):
        temp=np.zeros((1,X.shape[1]))
        for j in range(len(labels)):
            if labels[j]==i:

                temp=np.concatenate((temp,[X[j]]))
        plt.plot(temp[1:].T[0],temp[1:].T[1],'o',mfc=colors[i],mec=colors[i],markersize=3,alpha=0.6)
    plt.show()
def K_means_algo(X,k):
    centers=_init_(X,k)
    while True:
        label=assign_label(X,centers,k)
        new_centers=find_centroids(X,label,k)
        if has_converged(centers,new_centers):
            return centers,label
        centers=new_centers
k=int(input('Moi ban nhap k:'))
diem_khoi_tao=np.random.random((k,2))

cov=np.eye(2)
print(cov)
x=[]
for i in range(k):
    x.append(np.random.multivariate_normal(diem_khoi_tao[i],cov,N))
X=x[0]
for i in range(1,len(x)):
    X=np.concatenate((X,x[i]))
#print(X.shape)
original_labels=[0]*N
for i in range(1,k):
    original_labels+=[i]*N
original_labels=np.array(original_labels)
plot_k_means(X,original_labels,k)
centers,labels=K_means_algo(X,k)
plot_k_means(X,labels,k)
print("Centers found:")
print(centers)