> SkipQ Sirius: Sprint 4
# Welcome to the RESTFUL CRUD API Gateway Project for Web Crawler Application!
#### An AWS CRUD API Gateway application for the Web Crawler app to populate a URL DynamoDB table to perform REST API CRUD operations and monitor the resource web health.

##### [Back-to-Top](#back-to-top)
---

## **Table of Contents:**

* ### [Overview](#overview-1)
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

I have developed this project in order to build a CRUD API Gateway endpoint for the Web Crawler app to populate a URL DynamoDB table to perform REST API CRUD operations, so that i can monitor the web health of the URL resources and implement CI/CD with CRUD business logic. The CRUD operation is performed using the **Amazon API Gateway** service and an RESTFUL API is created following the **HTTP** Protocol to perform the **GET**, **POST**, **UPDATE** and **DELETE** methods. Upon method request and successful method operation an **HTTP statusCode:200** is sent in response and the data is modified in the DynamoDB table, which is further sent to the web health app to calculate the web health metrics and raise **Alarms** and actions in **CloudWatch** using **Python boto3 SDK**.

 * First metric that i have used to check the health of websites is **Availability Metric**. Availability is a simple percentage based on the uptime divided by the total time span. This metric tells the availability status of a website be returning a **HTTP 200** OK Code when a **GET** Request is sent, indicating that the site is up and running.
 * Second metric that i have used is **Latency Metric**. This metric is the combined values of domain lookup time, connect time and response time. Latency: Putting the application, the server and the DNS response times aside for a moment, obviously the network can be a big factor when measuring performance. This metric calculates the amount of delay on a network. **Low latency** or **High latency** depends upon the performance of that specific website.

 These metrics are defined using boto3 SDK and are triggered by a **Lambda Funtion**, which we have converted into a **Cron Job** by defining event rule, which will invoke Lambda after every 60 minutes. This Lambda will then check the values of **Availability** and **Latency**. Against these 2 metrices, i have defined threshold i.e **0.4 for Latency** and **1 for Availability**. If any of these threshold is breached, An alarm will be triggered in **CloudWatch**. For the momment when alarm is triggered, i have used **AWS SNS Service** to send a detailed notification on subscriber's **Email**, also this SNS will trigger a **Lambda Funtion** which will then save that alarm information in a **DynamoDB Table**.
 
<br />
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

The **GET** method performs the functionality to extract all available records using the scan function on the URL DynamoDB table. In case the records are found an **HTTP statusCode:200** is sent along with the scanned data in the body of the **response**. 
<br/>

The **POST** method performs the functionality to send the data in the **request** body to the URL DynamoDB table and upon successful put function an **HTTP statusCode:200** is sent and data is written in the DynamoDB table.
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
For the Integration test i am testing the integration between two units, and scanning the URL Table from DynamoDB to check that upon API Gateway invocation of **GET**, **POST**, **UPDATE** and **DELETE** methods the URL's are populated in the URL DynamoDB table.
<br /> 

The **Prod** stage performs the **Manual Approval** step, which requires the user to review and approve or reject the deployment to Production.
<br />
<br />
> ## Objective
 <br />

 Main objective of this CRUD API Gateway application is to get a clear understanding of **How to build a CRUD API Gateway endpoint for the Web Crawler app to populate a URL DynamoDB table to perform REST API CRUD operations, so that we can monitor the web health of the URL resources and implement CI/CD with CRUD business logic**. 
 
 
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

![image](https://user-images.githubusercontent.com/117926781/205467065-42fde43e-ffdf-48eb-9c80-7a532d2d6c05.png)

![image](https://user-images.githubusercontent.com/117926781/205467123-a465ecbe-3468-48ea-8f8f-fbe76f11aa84.png)

![image](https://user-images.githubusercontent.com/117926781/205467159-dec1047e-8235-4d46-9d1a-6f2bd4be8f6b.png)

![image](https://user-images.githubusercontent.com/117926781/205467219-a79e9f78-8ceb-4bc1-ae83-91abc7e48ac6.png)

![image](https://user-images.githubusercontent.com/117926781/205467391-bd7507d7-c662-471e-895e-387b4f28651a.png)

<br />

* #### DynamoDB Screenshots
<br />

![image](https://user-images.githubusercontent.com/117926781/205467315-7b13c613-d95a-497a-bfef-d394408dc6e6.png)

![image](https://user-images.githubusercontent.com/117926781/205467462-735536b0-7ebb-494e-a696-e5da4085b589.png)

![image](https://user-images.githubusercontent.com/117926781/205467572-7729e42f-6ba0-4770-a0cc-bf32589dc7f0.png)

<br />

* #### SNS Notifications Screenshots
<br />

![image](https://user-images.githubusercontent.com/117926781/205468428-65c19878-03f6-4f0b-bd76-5ef3d1c8ff20.png)

<br />

* #### CloudWatch Alarm Screenshots
<br />

![image](https://user-images.githubusercontent.com/117926781/205468597-acbb02fb-f69b-45ca-b9a5-070cba290474.png)

![image](https://user-images.githubusercontent.com/117926781/205468783-a7f4a82e-7354-4fc9-a394-a5b5c845cda3.png)

![image](https://user-images.githubusercontent.com/117926781/205469329-11e66ad3-be39-4293-af1e-14133132c3f2.png)

![image](https://user-images.githubusercontent.com/117926781/205468985-1ea81e48-e141-4bab-af9c-43f02b02420f.png)

![image](https://user-images.githubusercontent.com/117926781/205469267-7497c18a-e39b-4a71-a691-0e59befff418.png)

<br />

* #### CodePipeline Screenshots
<br />

![image](https://user-images.githubusercontent.com/117926781/205467911-b1d884bc-a562-43a1-b628-62ed875d8cd1.png)

<br />

* #### Unit Functional and Integration Tests
<br />

![image](https://user-images.githubusercontent.com/117926781/205468102-3ae53de6-50cb-4b1e-88d0-873aed3e04c5.png)



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
