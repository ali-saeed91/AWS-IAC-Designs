> SkipQ Sirius: Sprint 5
# Welcome to Design Problem #1!
#### Design Problem - 1: 

<Design & Develop>
Consider that you are getting an event response as {“arg1”: 10} from an API.
Make an AWS app that generates an alarm if arg1 > 10.
When the alarm is raised, send an email to a dummy account.

What will you do if there is no lambda invocation even though the code is working fine and there is no error generated?


##### [Back-to-Top](#back-to-top)
---

## **Table of Contents:**

* ### [Overview](#overview-1)
* ### [Design Diagram](#design-diagram-1)
* ### [CRUD API Gateway](#crud-api-gateway-1)
* ### [CI/CD](#cicd-pipeline)
* ### [Objective](#objective-1)
* ### [AWS Services](#aws-services-1)
* ### [Non AWS Services](#non-aws-services-1)
* ### [Getting Started](#getting-started-1)

    * ### [Environment Setup](#environment-setup-1)

    * ### [Project Setup](#project-setup-1)

    * ### [Project Deployment](#project-deployment-1)

* ### [Results](#results-1)
    
    * ### [API Gateway](#api-gateway-screenshots)

    * ### [DynamoDB](#dynamodb-screenshots)

    * ### [SNS Notifications](#sns-notifications-screenshots)

    * ### [CloudWatch Alarms](#cloudwatch-alarm-screenshots)

    * ### [CodePipeline](#codepipeline-screenshots)

    * ### [Unit Functional & Integration Tests](#unit-functional-and-integration-tests)


 * ### [References](#references-1)
 * ### [Useful Commands](#useful-commands-1)
 * ### [Author Contact](#author-contact-1)

<br />


>  ## Overview
 <br />

I have developed this project in order to build a CRUD API Gateway endpoint for the CDK app to populate a ARG DynamoDB table using REST API CRUD operations, so that i can monitor the arg1 values sent by the API Gateway and whenever the arg1 value is greater then 10 an Alarm is raised and SNS based email is sent to my email account.  
In addition i have implemented CI/CD with CRUD business logic. The CRUD operation is performed using the **Amazon API Gateway** service and an RESTFUL API is created following the **HTTP** Protocol to perform the **GET**, **POST**, **UPDATE** and **DELETE** methods. Upon method request and successful method operation an **HTTP statusCode:200** is sent in response and the data is modified in the DynamoDB table, which is further sent to the WH app to check the arg1 value metric and raise **Alarms** and actions in **CloudWatch** using **Python boto3 SDK**.

 * The ARG1 value metric that i have used to check the integer value sent by API Gateway and is **ARG1 Value Metric**.

 The ARG1 value metric is defined using boto3 SDK and is triggered by a **Lambda Funtion**, which i have converted into a **Cron Job** by defining event rule, which will invoke Lambda after every 60 minutes. This Lambda will then check the values of **ARG1 Values**. Against this metric, i have defined threshold i.e **10 for arg1_value**. If the threshold is breached, An alarm will be triggered in **CloudWatch**. For the momment when alarm is triggered, i have used **AWS SNS Service** to send a detailed notification on subscriber's **Email**, also this SNS will trigger a **Lambda Funtion** which will then save that alarm information in a **DynamoDB Table**.
 
<br />
<br />

>  ## Design Diagram
<br />

![DesignProblem1](https://user-images.githubusercontent.com/117926781/205742355-ddcb4256-668a-41c8-b197-8107f7ed8ab3.png)

<br />

>  ## CRUD API Gateway
 <br />

 The RESTFUL CRUD API Gateway is implemented by using **AWS API Gateway** which uses the **HTTP** Protocol with the request and response messages to perform the RESTFUL API operations of Create, Read, Update and Delete. From the **AWS API Gateway** i have used the Lambda invoked API Gateway to integrate the API Lambda with the RESTFUL endpoint to perform the following 4 methods:
 <br /> 

 * **GET**
 * **POST**
 * **PATCH**
 * **DELETE**
<br />

The **GET** method performs the functionality to extract all available records using the scan function on the ARG1 DynamoDB table. In case the records are found an **HTTP statusCode:200** is sent along with the scanned data in the body of the **response**. 
<br/>

The **POST** method performs the functionality to send the data in the **request** body to the ARG1 DynamoDB table and upon successful put function an **HTTP statusCode:200** is sent and data is written in the DynamoDB table.
<br />

The **PATCH** method performs the functionality to send a key and reference value to update the existing records value with the sent value using the update function, in response an **HTTP statusCode:200** is sent and data is overwritten in the DynamoDB table for the respective field.
<br />

The **DELETE** method  performs the functionality to delete a record in the table by using the delete function. A key:value pair is sent the request body and upon successful delete operation an **HTTP statusCode:200** is sent and the respective data is deleted in the DynamoDB table.
<br />
<br />

 > ## CI/CD Pipeline
 <br />

 The CI/CD Pipeline is implemented using **AWS CodePipeline** as the base, **Github** as a **Source**, **AWS CodeBuild** as the build service and **AWS CodeDeploy** for deployment.
 The multi-stage pipeline CI/CD is divided into 2 stages with unit, functional and integration tests being perfomed, also Manual approval is required in pre production stage:
 <br /> 

 * **Beta (Unit, Functional and Integration Tests)**
 * **Prod (Manual Approval)**
<br />

The **Beta** stage performs the 5 Unit tests and 1 functional test using **Pytest** fixtures and for resource count, resource properties and assertions match with stack templates and creation of dynamodb table in stack.
For the Integration test i am testing the integration between two units, and scanning the Alarm Table from DynamoDB to check that upon breach of threshold the ARG1 alarms are populated in the Alarm DynamoDB table.
<br /> 

The **Prod** stage performs the **Manual Approval** step, which requires the user to review and approve or reject the deployment to Production.
<br />
<br />
> ## Objective
 <br />

 Main objective of this CRUD API Gateway application is to get a clear understanding of **How to Make an AWS app that generates an alarm if arg1 > 10 and When the alarm is raised, send an email to a dummy account**. 
 
 
 * CRUD stands for (Create, Update, Read and Delete) in its base form, CRUD is a way of manipulating information, describing the function of an application.
 * REST is controlling data through HTTP commands. It is a way of creating, modifying, and deleting information for the user.
 * CI/CD is the process of continuous integration and continuous delivery in the Software Development Life Cycle (SDLC).

<br />
<br />

> ## AWS-Services
 <br />

 Below is the list of AWS Services that i have used while deploying my application on AWS:

 * **AWS API Gateway**
 * **AWS CloudFormation**
 * **AWS Lambda**
 * **AWS CloudWatch**
 * **AWS SNS**
 * **AWS DynamoDB**
 * **AWS CodePipeline**
 * **AWS CodeBuild**
 * **AWS CodeDeploy**
 * **AWS CodePipeline**
 * **AWS SecretsManager**

<br />
 <br />

> ## Non AWS Services
 <br />

Below is the list of the Non AWS Services that i have used while deploying my application on AWS:

 * **GitHub**
 * **Pytest**
 
<br />

> ## Getting Started
 <br />

* >### Environment setup
In order to use **VS Code** in order to write our code in CDK, first i have setup my environment using below mentioned commands:

```
wsl --install >> To install wsl
```

```
sudo apt udate  >> To update python
sudo apt install python3 python-zip >> To install python
pyhton3 --version >> To check python version
```

```
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -0 "awscliv2.zip"
sudo apt install unzip >> To install aws package
unzip awscliv2.zip >> To unzip install package
sudo ./aws/install >> To install aws
aws-version >> To check aws version
```
* >### Project setup
Once the environment setup is done, I ran these commands to run project in my local AWS environment:
```
git clone "url-to-github-repo" >> To clone the forked repo
python3 -m venv .venv && source .venv/bin/activate >> To setup virtual environment
pip install -r requirements.aws.txt >> To install requirements
```
* >### Project Deployment
Once the complete code is written and all the requiremnents are fullfilled, i used **CDK Synth** and **CDK Deploy** to create a stack file in Cloud Formation template and then deploying that Cloud Fomation template respectively.

* **CDK Synth:**

    The cdk synth command executes your app, which causes the resources defined in it to be translated into an AWS CloudFormation template. The displayed output of cdk synth is a YAML-format template. The cdk synth command from the CDK CLI generates and prints the CloudFormation equivalent of the CDK stack we've defined.

* **CDK Deploy:**

    The CDK deploy command deploys our CDK stack(s) as CloudFormation template(s). CDK is just an abstraction level above CloudFormation. The whole idea behind CDK is to improve developer experience by allowing us to use a programming language, rather than a configuration language like json or yaml.

* **git add . && git commit -m "" && git push:**

    The **git add .** command adds the current changes to the staging layer, we can revert back if needed from this stage. The **git commit -m ""** command adds the changes from staging to history. The **git push** command pushes the changes from history to github and once the changes are deployed, the AWS stack pipeline will fetch the changes from the **source** and starts to update the entire pipeline automatically.
<br />
<br />


>## Results
In order to display the GUI of multiple services which i have used in my project, my final results and detailed information about the project and end results, please check below-pasted screenshots:


<br />

* #### API Gateway Screenshots
<br />

![image](https://user-images.githubusercontent.com/117926781/205743279-e518dd24-a4a7-41f1-a5bf-1c6de670408e.png)

![image](https://user-images.githubusercontent.com/117926781/205743550-2284c702-14b0-4bdd-a0c2-0866b418feb9.png)

![image](https://user-images.githubusercontent.com/117926781/205467159-dec1047e-8235-4d46-9d1a-6f2bd4be8f6b.png)

![image](https://user-images.githubusercontent.com/117926781/205743811-89c9255a-c744-4480-b1df-1a18f27b1ce2.png)

![image](https://user-images.githubusercontent.com/117926781/205744110-836246e5-b65e-41d9-b952-e9fc7c6f826a.png)

<br />

* #### DynamoDB Screenshots
<br />

![image](https://user-images.githubusercontent.com/117926781/205744491-9f4e76e3-9d88-479a-9e1e-c79d2870bfa1.png)

![image](https://user-images.githubusercontent.com/117926781/205745208-b29696f4-cfec-4828-905d-a894f502bfb1.png)

<br />

* #### SNS Notifications Screenshots
<br />

![image](https://user-images.githubusercontent.com/117926781/205745420-e1d27d61-86a7-4397-8f1e-ed107210c3da.png)

<br />

* #### CloudWatch Alarm Screenshots
<br />

![image](https://user-images.githubusercontent.com/117926781/205745683-8cd69eb4-cd81-4257-8492-246af0bbf09a.png)

![image](https://user-images.githubusercontent.com/117926781/205745855-1424ea8b-f197-4b1e-8153-1b58580e94af.png)

![image](https://user-images.githubusercontent.com/117926781/205745993-66ede15b-b5d1-496d-9ab3-7d1783056389.png)

![image](https://user-images.githubusercontent.com/117926781/205746378-3dd7df53-66f3-486c-9b42-b5d9f8f98c0f.png)

![image](https://user-images.githubusercontent.com/117926781/205746599-ccedfe9c-4e9b-4bbf-a5dc-fe4624f36878.png)

<br />

* #### CodePipeline Screenshots
<br />

![image](https://user-images.githubusercontent.com/117926781/205747367-73effac4-a039-4bd2-baac-c1fc62e27520.png)

<br />

* #### Unit Functional and Integration Tests
<br />

![image](https://user-images.githubusercontent.com/117926781/205747021-fdbb8152-26a1-42f7-9882-9107ee640ccf.png)



> ## Useful Commands

 <br />
Below list contains some of the most handy commands that were used freuently during this project:

```
git add . >> Adds the current changes to staging
git commit -m "" >> Adds the change set in git history
git push >> Pushes the changes to Github Repository
CDK DOC >> Opens cdk documentation
CDK DIFF >> Compare deployed stack with current stack
CDK LS >> List all stacks in the app
CDK DEPLOY >> Deploy the stack on the Cloud
CDK SYNTH >> Emits the synthesized CloudFormation template
```
<br />

> ## References
 <br />

 Below list contains the link for all the references and resources that i have used to build my project:

* [AWS API Gateway](https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_apigateway/README.html)

* [AWS API Reference](https://docs.aws.amazon.com/cdk/api/v2/python/modules.html)

* [AWS SNS Notifications](https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_sns.html)

* [AWS Lambda](https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_lambda.html)

* [AWS CloudWatch](https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_cloudwatch.html)

* [AWS CodePipeline](https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_codepipeline.html)

* [AWS CodeBuild](https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_codebuild.html)

* [AWS CodeDeploy](https://docs.aws.amazon.com/cdk/api/v1/python/aws_cdk.aws_codedeploy/README.html)

* [AWS Lambda Deployment Groups](https://docs.aws.amazon.com/cdk/api/v1/python/aws_cdk.aws_codedeploy/LambdaDeploymentGroup.html)

* [Boto3 Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/cw-example-using-alarms.html)

* [Pytest](https://docs.pytest.org/en/6.2.x/fixture.html)

<br />

> ## Author Contact
* Name :: Ali Saeed
* Email :: ali.saeed.sirius@gmail.com
* GitHub :: https://github.com/alisaeed2022skipq
* Phone :: +92-344-5512351

 <br />

Thanks for Reading 👍
##### [Back-to-Top](#back-to-top)
