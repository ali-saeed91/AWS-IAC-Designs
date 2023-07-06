from constructs import Construct
from aws_cdk import (
    Stage
)
from sprint3.sprint3_stack import Sprint3Stack

class ALIStage(Stage):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        self.stage = Sprint3Stack(self, "AliStage")
    