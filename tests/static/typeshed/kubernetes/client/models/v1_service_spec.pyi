# Stubs for kubernetes.client.models.v1_service_spec (Python 2)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class V1ServiceSpec:
    swagger_types: Any = ...
    attribute_map: Any = ...
    discriminator: Any = ...
    cluster_ip: Any = ...
    external_i_ps: Any = ...
    external_name: Any = ...
    external_traffic_policy: Any = ...
    health_check_node_port: Any = ...
    load_balancer_ip: Any = ...
    load_balancer_source_ranges: Any = ...
    ports: Any = ...
    publish_not_ready_addresses: Any = ...
    selector: Any = ...
    session_affinity: Any = ...
    session_affinity_config: Any = ...
    type: Any = ...
    def __init__(self, cluster_ip: Optional[Any] = ..., external_i_ps: Optional[Any] = ..., external_name: Optional[Any] = ..., external_traffic_policy: Optional[Any] = ..., health_check_node_port: Optional[Any] = ..., load_balancer_ip: Optional[Any] = ..., load_balancer_source_ranges: Optional[Any] = ..., ports: Optional[Any] = ..., publish_not_ready_addresses: Optional[Any] = ..., selector: Optional[Any] = ..., session_affinity: Optional[Any] = ..., session_affinity_config: Optional[Any] = ..., type: Optional[Any] = ...) -> None: ...
    @property
    def cluster_ip(self): ...
    @cluster_ip.setter
    def cluster_ip(self, cluster_ip: Any) -> None: ...
    @property
    def external_i_ps(self): ...
    @external_i_ps.setter
    def external_i_ps(self, external_i_ps: Any) -> None: ...
    @property
    def external_name(self): ...
    @external_name.setter
    def external_name(self, external_name: Any) -> None: ...
    @property
    def external_traffic_policy(self): ...
    @external_traffic_policy.setter
    def external_traffic_policy(self, external_traffic_policy: Any) -> None: ...
    @property
    def health_check_node_port(self): ...
    @health_check_node_port.setter
    def health_check_node_port(self, health_check_node_port: Any) -> None: ...
    @property
    def load_balancer_ip(self): ...
    @load_balancer_ip.setter
    def load_balancer_ip(self, load_balancer_ip: Any) -> None: ...
    @property
    def load_balancer_source_ranges(self): ...
    @load_balancer_source_ranges.setter
    def load_balancer_source_ranges(self, load_balancer_source_ranges: Any) -> None: ...
    @property
    def ports(self): ...
    @ports.setter
    def ports(self, ports: Any) -> None: ...
    @property
    def publish_not_ready_addresses(self): ...
    @publish_not_ready_addresses.setter
    def publish_not_ready_addresses(self, publish_not_ready_addresses: Any) -> None: ...
    @property
    def selector(self): ...
    @selector.setter
    def selector(self, selector: Any) -> None: ...
    @property
    def session_affinity(self): ...
    @session_affinity.setter
    def session_affinity(self, session_affinity: Any) -> None: ...
    @property
    def session_affinity_config(self): ...
    @session_affinity_config.setter
    def session_affinity_config(self, session_affinity_config: Any) -> None: ...
    @property
    def type(self): ...
    @type.setter
    def type(self, type: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any): ...
    def __ne__(self, other: Any): ...