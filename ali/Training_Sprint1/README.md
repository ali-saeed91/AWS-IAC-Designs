# Sprint1
## Hello World Lambda

This is a AWS CDK project for building a **"Hello World Lambda Function"**.

The application, tags, stack aliases and environment are defined in the `app.py` file.

The `app.py` file executes the stack which is defined in the `training_sprint1_stack.py` file.

The stack file contains the imports for the libraries: lambda, stack and constructs.

The **lambda function** is defined using the AWS API Reference: 
 https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_lambda/README.html

The lambda function calls the method (lambda_handler) from the resources directory.

The id , asset, handler are passed as arguments and are defined in the **create_lambda** defination.

The runtime environment is set to be "Python 3.9".

To synthesize the the application use the command `cdk synth`.

To deploy the application to AWS use the command `cdk deploy`.

The lambda function can be triggered using the Test button for event in the AWS console :lambda > function.

The output of the event based trigger will return **"Hello from Lambda!"** in Response. 


