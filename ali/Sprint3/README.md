> SkipQ Sirius: Sprint 3
# Welcome to the Multistage CI/CD for Web Crawler Project!
#### An AWS CDK CI/CD to monitor the operational Health of Web Crawler by tracking the application metrics with Auto rollback upon metric Alarm.

##### [Back-to-Top](#back-to-top)
---

## **Table of Contents:**

* ### [Overview](#overview-1)
* ### [CI/CD](#cicd-pipeline)
* ### [Objective](#objective-1)
* ### [AWS Services](#aws-services-1)
* ### [Non AWS Services](#non-aws-services-1)
* ### [Getting Started](#getting-started-1)

    * ### [Environment Setup](#environment-setup-1)

    * ### [Project Setup](#project-setup-1)

    * ### [Project Deployment](#project-deployment-1)

* ### [Results](#results-1)

    * ### [CodePipeline](#codepipeline-screenshots)

    * ### [CloudWatch Alarms](#cloudwatch-alarm-screenshots)

    * ### [Unit Tests](#unit-tests-screenshots)

    * ### [Functional Tests](#functional-test-screenshots)

    * ### [Integration Tests](#integration-test-screenshots)

 * ### [References](#references-1)
 * ### [Useful Commands](#useful-commands-1)
 * ### [Author Contact](#author-contact-1)

<br />


>  ## Overview
 <br />

I have developed this project in order to perform multi-stage CI/CD pipeline with Unit , Functional and Integration tests and Emit CloudWatch metrics and alarms for the operational health of the web crawler so that i can Automate rollback to the last build if metrics are in alarm.

 * First metric that i have used to check health of Web Crawler is **Duration Metric**. Duration is basically the Bake Time for our Lambda Application being implemented for all pipeline stages. Duration is the maximum time for the Lambda to execute the application. This metric tracks the maximum duration or time allowed for the Lambda application and upon breach of the set threshold an Alarm **Duration Alarm** is raised which is further passed to the **Deployment Group** and an **Auto rollback** is initiated to the last build.

 * Second metric that i have used is **Invocation Metric**. This metric is the measure of the triggering of the Lambda or concurrent invocations. Invocation is the process to trigger the lambda for the application upon which the relevant tasks are performed. This metric tracks the number of invocations for the Lambda which is the compute resource for our application. Upon breach of a set threshold an Alarm **Invocation Alarm** is raised which is further passed to the **Deployment Group** and an **Auto rollback** is initiated to the last build.

 These metrics are triggered upon the execution of the  **Lambda Funtion**, which we have converted into a **Cron Job** by defining event rule, which will invoke Lambda after every 60 minutes. Also whenever we would push code changes to our Pipeline **Source** these metrics will be evaluated on each stage. These metrics will then check the values of **Duration** and **Invocation**. Against these 2 metrices, i have defined threshold i.e **20 seconds for Duration** and **2 for Invocation**. If any of these threshold is breached, An alarm will be triggered in **CloudWatch**. For the momment when alarm is triggered, it is passed to **Lambda Deployment Group** which starts an **Auto rollback** to the last successful build.
<br />
<br />

>  ## CI/CD Pipeline
 <br />

 The CI/CD Pipeline is implemented using **AWS CodePipeline** as the base, **Github** as a **Source**, **AWS CodeBuild** as the build service and **AWS CodeDeploy** for deployment.
 The multi-stage pipeline CI/CD is divided into 4 stages with unit, functional and integration tests being perfomed, also Manual approval is required in pre production stage:
 <br /> 

 * **Beta (Unit Tests and Functional Test #1)**
 * **Gamma (Functional Test #2)**
 * **Delta (Integration Test)**
 * **Prod (Manual Approval)**
<br />

The **Beta** stage performs the 5 Unit tests and 1 functional test using **Pytest** fixtures for resource count, resource properties and assertions match with stack templates and creation of dynamodb table in stack.
<br/>
The **Gamma** stage performs the functional test #2 on the web health function to get the **latency** and **availability** of the defined input using **try-except** blocks to raise an exception in case of error.
<br />
The **Delta** stage performs the Integration test to test the integration between two units, I am scanning the Beta Stage Alarm Table from DynamoDB to check that upon Lambda invocation the Alarms are being written in DynamoDB table.
<br /> 
The **Prod** stage performs the **Manual Approval** step, which requires the user to review and approve or reject the deployment to Production.
<br />
<br />

> ## Objective
 <br />

 Main objective of this Web Crawler App is to get a clear understanding of **How to develop a CI/CD Pipeline for cdk application from scratch and then How to deploy that application on AWS Cloud and then using different AWS Services as per the requirements and tracking the operational health of the Application with metrics for auto rollback**. 
 
 * CI/CD is the process of continuous integration and continuous delivery in the Software Development Life Cycle (SDLC).
 * Auto Rollback is the process of rolling back the application stack to its last successful build.

<br />
<br />

> ## AWS-Services
 <br />

 Below is the list of AWS Services that i have used while deploying my application on AWS:

 * **AWS CloudFormation**
 * **AWS Lambda**
 * **AWS CloudWatch**
 * **AWS SNS**
 * **AWS DynamoDB Table**
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

* #### CodePipeline Screenshots
<br />

![image](https://user-images.githubusercontent.com/117926781/204156300-11b20a90-2339-4730-a498-427c96027cb6.png)


![image](https://user-images.githubusercontent.com/117926781/204156837-ca240571-739f-43ca-8cd0-186e984dbb46.png)


![image](https://user-images.githubusercontent.com/117926781/204157270-c859e334-31d4-498b-baa9-d7699121842e.png)


![image](https://user-images.githubusercontent.com/117926781/204158788-c36f822c-640b-49c7-8934-4a3f2b5cbf56.png)


* #### CloudWatch Alarm Screenshots
<br />

![image](https://user-images.githubusercontent.com/117926781/204157535-07848a10-847b-4f16-a233-f9038c2e8d72.png)

![image](https://user-images.githubusercontent.com/117926781/204163231-c4ada7cf-015c-40ec-8768-72574f7055e2.png)

![image](https://user-images.githubusercontent.com/117926781/204157830-6c388887-3ade-40a3-ad9c-889aff47f4aa.png)

![image](https://user-images.githubusercontent.com/117926781/204158005-4d5c4910-b08c-4e97-b319-47670ebffdef.png)


* #### Unit Tests Screenshots
<br />

![image](https://user-images.githubusercontent.com/117926781/204158278-6a8dde12-c839-4442-bd1f-d29f3c176b84.png)


* #### Functional Test Screenshots

<br />

![image](https://user-images.githubusercontent.com/117926781/204158518-65c0aa2e-a8bf-49e0-8f0c-c54db1e15e10.png)

* #### Integration Test Screenshots

<br />

![image](https://user-images.githubusercontent.com/117926781/205003580-3edadda9-e6ff-4fa0-9fe5-f753c4e68eab.png)

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


* [AWS API Reference](https://docs.aws.amazon.com/cdk/api/v2/python/modules.html)

* [AWS SNS Notifications](https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_sns.html)

* [AWS Lambda](https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_lambda.html)

* [AWS CloudWatch](https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_cloudwatch.html)

* [AWS CodePipeline](https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_codepipeline.html)

* [AWS CodeBuild](https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_codebuild.html)

* [AWS CodeDeploy](https://docs.aws.amazon.com/cdk/api/v1/python/aws_cdk.aws_codedeploy/README.html)

* [AWS Lambda Deployment Groups](https://docs.aws.amazon.com/cdk/api/v1/python/aws_cdk.aws_codedeploy/LambdaDeploymentGroup.html)

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
