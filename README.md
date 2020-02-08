# AWS Lambda sample codes

A  few of the sample AWS Lambda function codes for common use-cases with [Amazon EC2](https://github.com/shreyasgaonkar/aws-lambda-code-samples#ec2), [AWS Lambda](https://github.com/shreyasgaonkar/aws-lambda-code-samples#lambda) & [Amazon SNS](https://github.com/shreyasgaonkar/aws-lambda-code-samples#sns).

## EC2

1. Start/Stop EC2 instances using CloudWatch Event Trigger  - [start_stop_ec2_instances_with_cloudwatch_event.py](ec2-samples/start_stop_ec2_instances_with_cloudwatch_event/start_stop_ec2_instances_with_cloudwatch_event.py)

2. Describe EC2's metadata in a region - Associated subnets, Instance ID & NACL-ID for a target VPC - [describe_ec2_securitygroup.py](ec2-samples/describe_ec2_securitygroup/describe_ec2_securitygroup.py)

3. Describe all AMIs for your account across all regions - [describe_ami.py](ec2-samples/describe_ami/describe_ami.py)


## Lambda

1. Get underlying Lambda's CPU hardware, /tmp storage, os-release and it's contents  - [get_cpu_info.py](lambda-samples/get_cpu_info/get_cpu_info.py)

2. Create "Memory Used" Metrics for your Lambda functions - [lambda_memory_plot.py](lambda-samples/lambda_memory_plot/lambda_memory_plot.py)

3. List all Lambda layers and it's info  - [list_layer_info.py](lambda-samples/list_layer_info/list_layer_info.py)

4. List code storage for all Lambda functions in a region - [lambda_code_size.py](lambda-samples/lambda_code_size/lambda_code_size.py)

5. Get all functions using reserved or provisional concurrency in a region - [reserved_concurrency.py](lambda-samples/reserved_concurrency/reserved_concurrency.py)

6. Test HTTP connection for your Lambda function inside VPC - [http_connection_test.py](lambda-samples/http_connection_test/http_connection_test.py)

7. Check Async queue congestions and delays in processing async events - [get_async_invoke_delay.py](lambda-samples/get_async_invoke_delay/get_async_invoke_delay.py)

8. List Lambda function version(s) using an ENI - [lambda_hyperplane_eni_checker.py](lambda-samples/lambda_hyperplane_eni_checker/lambda_hyperplane_eni_checker.py)

## SNS

1. List all subscriptions tied to a topic in an account  - [list_account_topic_subscriptions.py](sns-samples/list_account_topic_subscriptions/list_account_topic_subscriptions.py)

2. Programmatically create subscription filters for SNS  - [set_subscription_filters.py](sns-samples/set_subscription_filters/set_subscription_filters.py)

3. Programmatically set SenderID while sending SMS text messages  - [sender_id.py](sns-samples/sender_id/sender_id.py)

4. Programmatically set max price while sending SMS text messages - [set_max_price.py](sns-samples/set_max_price/set_max_price.py)

## Additional Information

- Refer to the individual .md files for additional information.

## Built with
- [Python3](https://www.python.org/downloads/)
- [AWS](https://aws.amazon.com/)
- [Boto3 SDK](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)

## Missing Info / Bugs

- :cold_sweat: Something broken? [Open an issue](https://github.com/shreyasgaonkar/aws-lambda-code-samples/issues) with a few sample inputs where it breaks. Screenshots help!

- More additional services/use-cases, [open a new issue](https://github.com/shreyasgaonkar/aws-lambda-code-samples/issues)

## Contributing

This is an iterative repository, I'll keep adding more sample codes for more use-cases as I come across them. I have tested all scripts using ```Python3.6``` runtime inside Lambda under ```us-west-2``` region, and most of this should work for all ```Python3``` runtimes (Python 2.7 EOL: :dizzy_face:).

- Fork repo
- Set runtime as ```Python3``` (```Python3.6``` preferred)
- Send your awesome :raised_hands: [Pull Request](https://github.com/shreyasgaonkar/aws-lambda-code-samples/pulls) with code/.md changes
    - Follow Python's [PEP8](https://www.python.org/dev/peps/pep-0008/) coding standards.
    - Commit repo using the [Seven Rules](https://chris.beams.io/posts/git-commit/#seven-rules)
- Your PR gets merged :white_check_mark: and a shoutout :loudspeaker:


#### Repo structure:

```bash
$ tree
.
|-- CODE_OF_CONDUCT.md
|-- LICENSE
|-- README.md
|-- ec2-samples
|   |-- describe_ami
|   |   |-- README.md
|   |   `-- describe_ami.py
|   |-- describe_ec2_securitygroup
|   |   |-- README.md
|   |   `-- describe_ec2_securitygroup.py
|   `-- start_stop_ec2_instances_with_cloudwatch_event
|       |-- README.md
|       `-- start_stop_ec2_instances_with_cloudwatch_event.py
|-- lambda-layer
|   |-- README.md
|   |-- boto3.zip
|   |-- pandasnumpy.zip
|   |-- psycopg2.zip
|   `-- requests.zip
|-- lambda-samples
|   |-- get_async_invoke_delay
|   |   |-- README.md
|   |   `-- get_async_invoke_delay.py
|   |-- get_cpu_info
|   |   |-- README.md
|   |   `-- get_cpu_info.py
|   |-- http_connection_test
|   |   |-- README.md
|   |   `-- http_connection_test.py
|   |-- lambda_code_size
|   |   |-- README.md
|   |   `-- lambda_code_size.py
|   |-- lambda_hyperplane_eni_checker
|   |   |-- README.md
|   |   `-- lambda_hyperplane_eni_checker.py
|   |-- lambda_memory_plot
|   |   |-- README.md
|   |   `-- lambda_memory_plot.py
|   |-- list_layer_info
|   |   |-- README.md
|   |   `-- list_layer_info.py
|   `-- reserved_concurrency
|       |-- README.md
|       `-- reserved_concurrency.py
|-- sns-samples
|   |-- list_account_topic_subscriptions
|   |   |-- README.md
|   |   `-- list_account_topic_subscriptions.py
|   |-- sender_id
|   |   |-- README.md
|   |   `-- sender_id.py
|   |-- set_max_price
|   |   |-- README.md
|   |   `-- set_max_price.py
|   `-- set_subscription_filters
|       |-- README.md
|       `-- set_subscription_filters.py
`-- tmp
    `-- images
        |-- AWSLambdaCloudWatchAsyncDelay.png
        `-- AWSLambdaCloudWatchMetric.png
```
