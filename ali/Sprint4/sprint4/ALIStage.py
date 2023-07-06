from constructs import Construct
from aws_cdk import (
    Stage
)
from sprint4.sprint4_stack import Sprint4Stack

class ALIStage(Stage):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        self.stage = Sprint4Stack(self, "AliStage")
    