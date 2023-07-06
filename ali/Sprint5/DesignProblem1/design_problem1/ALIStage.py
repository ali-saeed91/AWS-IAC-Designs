from constructs import Construct
from aws_cdk import (
    Stage
)
from design_problem1.design_problem1_stack import DesignProblem1Stack

class ALIStage(Stage):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        self.stage = DesignProblem1Stack(self, "AliStage")
    