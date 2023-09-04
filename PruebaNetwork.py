
import pickle
import mnist_loader
import network

training_data, test_data, _ = mnist_loader.load_data_wrapper()

net = network.Network([784,30,10])
net.SGD(training_data,30,10,0.01,test_data=test_data)
with open('miRed.pkl','wb') as file1:
    pickle.dump(net,file1)
n
exit()
