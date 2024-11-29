import kubernetes
from library.logs import LogsLib


class K8sLib(LogsLib):
    def __init__(self, f_config, loglevel) -> None:
        super().__init__(loglevel)
        """
        Creates a Kubernetes Library instance

        :param string f_config: The path to the kubeconfig.
        """
        kubernetes.config.load_kube_config(config_file=f_config)
        self.k8s_client = kubernetes.client.ApiClient()

    def apply(self, yaml_path):
        """
        Applies a file
        
        :param string yaml_path: The path to the YAML file to load.
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

