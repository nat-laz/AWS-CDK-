from constructs import Construct
from aws_cdk import (
    Duration,
    Stack,
    aws_iam as iam,
    aws_sqs as sqs,
    aws_sns as sns,
    aws_sns_subscriptions as subs,
    aws_lambda as lambda_,
    aws_lambda_event_sources as lambda_event_sources,
)


class SqslambdademoStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create our Queue
        queue = sqs.Queue(
            self,
            "SqslambdademoQueue",
            visibility_timeout=Duration.seconds(300),
        )

        # Create our lambda Fucntion
        sqs_lambda = lambda_.Function(
            self,
            "SQSLambda",
            handler="lambda_handler.handler",
            runtime=lambda_.Runtime.PYTHON_3_11,
            code=lambda_.Code.from_asset("lambda"),
        )

        # create our event source
        sqs_event_source = lambda_event_sources.SqsEventSource(queue)

        # Add SQS event source to Lambda
        sqs_lambda.add_event_source(sqs_event_source)
