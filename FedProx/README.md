# Flower FedProx implement
[Paper](https://arxiv.org/abs/1812.06127)

I use FedAvg strategy in flower because FedProx is still use average way to aggregate client's model. FedProx change client's training procedure by adding penality on loss function.

There are some things defined by client (e.g. Adam optimizer), but if you want the server to define, just let the server pass it on config. In this example we just let the server define FedProx hyperparameter.