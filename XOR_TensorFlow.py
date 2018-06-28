import numpy as np
import tensorflow as tf

#input data
x_data = np.array([[0,0],[0,1],[1,0],[1,1]])
y_data = np.array([[0],[1],[1],[0]])

#network architecture
n_input = 2
n_hidden = 10
n_output = 1

#learning rate and epochs number
learning_rate = 0.1
epoches = 10000

#use tf.placeholder for assigning X,Y later
X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

#network weights
W1 = tf.Variable(tf.random_uniform([n_input, n_hidden], -1.0, 1.0, seed=0))
W2 = tf.Variable(tf.random_uniform([n_hidden, n_output], -1.0, 1.0, seed=0))

#network biases
B1 = tf.Variable(tf.zeros([n_hidden], name='Bias1'))
B2 = tf.Variable(tf.zeros([n_output], name='Bias2'))

#each layer use sigmoid activation function
l2_out = tf.sigmoid(tf.matmul(X, W1) + B1)
y_hat = tf.sigmoid(tf.matmul(l2_out, W2) + B2)

#train network by gradient descent optimizer and "-Y*tf.log(y_hat) - (1-Y)*tf.log(1-y_hat)" cost function
cost = tf.reduce_mean(-Y*tf.log(y_hat) - (1-Y)*tf.log(1-y_hat))
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

init = tf.initialize_all_variables()

with tf.Session() as sess:
    sess.run(init)
    
    for i in range(epoches):
        sess.run(optimizer, feed_dict={X: x_data, Y: y_data})
        if(i%1000 == 0):
            print("Epoch: ", i,"  Cost :", sess.run(cost, feed_dict={X: x_data, Y: y_data}))
    answer = tf.equal(tf.floor(y_hat + 0.5), Y)
    accuracy = tf.reduce_mean(tf.cast(answer, tf.float32))
    
    print("Output of Network is :\n",sess.run(y_hat, feed_dict={X: x_data, Y: y_data}))
    print("Accuracy :", sess.run(accuracy, feed_dict={X:x_data, Y: y_data})*100,"%")
