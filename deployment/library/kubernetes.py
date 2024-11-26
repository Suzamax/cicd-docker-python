import kubernetes


class K8sLib:
    def __init__(self, f_config) -> None:
        """
        Creates a Kubernetes Library instance

        :param str f_config: The path to the kubeconfig.
        """
        kubernetes.config.load_kube_config(config_file=f_config)
        self.k8s_client = kubernetes.client.ApiClient()

    def apply(self, yaml_path):
        """
        Applies a file
        """
        kubernetes.utils.create_from_yaml(k8s_client=self.k8s_client, yaml_file=yaml_path)

    def create(self):
        """
        Creates a resource
        """
        pass

    def get(self):
        """
        Gets a list of resources
        """
        pass

    def delete(self):
        """
        Deletes a resource
        """
        pass

