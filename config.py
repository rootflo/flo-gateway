import json

from typing import List
from dataclasses import dataclass

@dataclass
class Providers():
    name: str
    endpoint: str
    type: str
    
@dataclass
class GatewayConfig():
    version: str
    providers: List[Providers]


with open('./gateway.json', 'r') as file:
    data = json.load(file)

providers_list = [Providers(**provider) for provider in data['providers']]
data['providers'] = providers_list

gateway_config = GatewayConfig(**data)

print(gateway_config)