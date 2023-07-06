import aws_cdk as core
import aws_cdk.assertions as assertions

from design_problem2.design_problem2_stack import DesignProblem2Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in design_problem2/design_problem2_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = DesignProblem2Stack(app, "design-problem2")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
