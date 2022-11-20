# Flower_client_selection_implement
Implementing client selection function in Flower(federal learning framework).

Strategies decide how to sample clients, how to configure clients for training, how to aggregate updates, and how to evaluate models.
[Implementing strategies](https://flower.dev/docs/implementing-strategies.html)

The configure_fit function in Strategy randomly sample clients originally. We will change the configure_fit function and get the client properties by get_properties function.
