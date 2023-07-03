import aws_cdk as core
import aws_cdk.assertions as assertions

from edyou_cdk.edyou_cdk_stack import EdyouCdkStack

# example tests. To run these tests, uncomment this file along with the example
# resource in edyou_cdk/edyou_cdk_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = EdyouCdkStack(app, "edyou-cdk")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
