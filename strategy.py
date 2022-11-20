class Client_selection_RAM_strategy(Strategy):

    def configure_fit(
        self, server_round: int, parameters: Parameters, client_manager: ClientManager
    ) -> List[Tuple[ClientProxy, FitIns]]:
        """Configure the next round of training."""
        weights = parameters_to_ndarrays(parameters)
        self.pre_weights = weights
        parameters = ndarrays_to_parameters(weights)
        config = {}
        if self.on_fit_config_fn is not None:
            # Custom fit config function provided
            config = self.on_fit_config_fn(server_round)
        fit_ins = FitIns(parameters, config)

        # Sample clients
        sample_size, min_num_clients = self.num_fit_clients(
            client_manager.num_available()
        )
        all_clients = client_manager.all() # Dict[str, ClientProxy], Return all available clients
        selected_clients = []
        for client in all_clients.values(): # look all clients
            client_properties = client.get_properties() # get each client properties
            if client_properties.RAM > 3:
                selected_clients.append(client)

        if(selected_clients.empty()):
            print("No client has be selected")
        # Return client/config pairs
        return [(client, fit_ins) for client in selected_clients]      