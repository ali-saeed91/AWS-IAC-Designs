from constructs import Construct
from aws_cdk import (
    Stage
)
from sprint6.sprint6_stack import Sprint6Stack

class ALIStage(Stage):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        self.stage = Sprint6Stack(self, "AliStage")
    