> SkipQ Sirius: Sprint 2
# Welcome to the Web Health Monitoring Project!
#### An AWS CDK application to monitor the Health of Web Resources by tracking the availability and latency metrics.

##### [Back-to-Top](#back-to-top)
---

## **Table of Contents:**

* ### [Overview](#overview-1)
* ### [Objective](#objective-1)
* ### [AWS Services](#aws-services-1)
* ### [Getting Started](#getting-started-1)

    * ### [Environment Setup](#environment-setup-1)

    * ### [Project Setup](#project-setup-1)

    * ### [Project Deployment](#project-deployment-1)

* ### [Results](#results-1)

    * ### [CloudWatch Screenshots](#cloudwatch-screenshots-1)

    * ### [Alarm Screenshots](#alarm-screenshots-1)

    * ### [SNS Email Screenshots](#sns-email-screenshots-1)

    * ### [DynamoDB Table Screenshots](#dynamodb-table-screenshots-1)

 * ### [References](#references-1)
 * ### [Useful Commands](#useful-commands-1)
 * ### [Author Contact](#author-contact-1)

<br />


>  ## Overview
 <br />

I have developed this projectin order to examine the webhealth of Websites using using Availability and Latency as metrics, then published those metrics on CloudWatch, bind threshold against these alarms and then used SNS to generate notifications if an alarm breaches the threshlod.

 * First metric that i have used to check health of websites is **Availability Metric**. Availability is a simple percentage based on the uptime divided by the total time span. This metric tells the availability status of a website be returning a **HTTP 200** OK Code when a **GET** Request is sent, indicating that the site is up and running.
 * Second metric that i have used is **Latency Metric**. This metric is the combined values of domain lookup time, connect time and response time. Latency: Putting the application, the server and the DNS response times aside for a moment, obviously the network can be a big factor when measuring performance. This metric calculates the amount of delay on a network. **Low latency** or **High latency** depends upon the performance of that specific website.

 These metrics are triggered by a **Lambda Funtion**, which we have converted into a **Cron Job** by defining event rule, which will invoke Lambda after every 60 minutes. This Lambda will then check the values of **Availability** and **Latency**. Against these 2 metrices, i have defined threshold i.e **0.6 for Latency** and **1 for Availability**. If any of these threshold is breached, An alarm will be triggered in **CloudWatch**. For the momment when alarm is triggered, i have used **AWS SNS Service** to send a detailed notification on subscriber's **Email**, also this SNS will trigger a **Lambda Funtion** which will then save that alarm information in **DynamoDB Table**.

<br />
<br />

> ## Objective
 <br />

 Main objective of this Web Health App deployment is to get a clear understanding of **How to develop an application from scratch and then How to deploy that application on AWS Cloud and then using different AWS Services as per the requirements**. 
 
 * Software deployment is the process of making software available to be used on a system by users and other programs
 * Software development refers to a set of computer science activities dedicated to the process of creating, designing, deploying and supporting software.

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

<br />
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
Once the complete code is written and all the requiremnents are fullfilled, i used **CDK Synt** and **CDK Deploy** to create a stack file in Cloud Formation template and then deploying that Cloud Fomation template respectively.

* **CDK Synth:**

    The cdk synth command executes your app, which causes the resources defined in it to be translated into an AWS CloudFormation template. The displayed output of cdk synth is a YAML-format template. The cdk synth command from the CDK CLI generates and prints the CloudFormation equivalent of the CDK stack we've defined.

* **CDK Deploy:**

    The CDK deploy command deploys our CDK stack(s) as CloudFormation template(s). CDK is just an abstraction level above CloudFormation. The whole idea behind CDK is to improve developer experience by allowing us to use a programming language, rather than a configuration language like json or yaml.

<br />
<br />

>## Results
In order to display the GUI of multiple services which i have used in my project, my final results and detailed information about the project and end results, please check below-pasted screenshots:


<br />

* #### CloudWatch Screenshots
<br />

![image](https://user-images.githubusercontent.com/117926781/202865731-c541ec41-9f4b-4f2c-aec7-c5b79a00793f.png)


![image](https://user-images.githubusercontent.com/117926781/202865559-320d641a-4cfe-4066-812e-a0ec08ec29d9.png)


* #### Alarm Screenshots
<br />

![image](https://user-images.githubusercontent.com/117926781/202866069-59ff2954-d2f6-44b9-997e-139d7d7d178e.png)

![image](https://user-images.githubusercontent.com/117926781/202866100-b9c4a0ab-e0d8-47dd-b684-01364656d11c.png)


* #### SNS Email Screenshots
<br />

![image](https://user-images.githubusercontent.com/117926781/202865954-97ef6fec-6c58-40c7-932b-ea3ec395ce71.png)

![image](https://user-images.githubusercontent.com/117926781/202865981-320c21a2-0ecc-4c4c-9638-f561fddbe0a3.png)


* #### DynamoDB Table Screenshots

<br />

![image](https://user-images.githubusercontent.com/117926781/202866189-c5b36fbb-8549-4881-90b4-87fbd0e03f81.png)

![image](https://user-images.githubusercontent.com/117926781/202866220-a365a209-d85c-4010-b836-6c2f160a6742.png)


> ## Useful Commands

 <br />
Below list contains some of the most handy commands that were used freuently during this project:

```
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

* [AWS SNS](https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_sns.html)

* [AWS Events](https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_events.html)


<br />

> ## Author Contact
* Name :: Ali Saeed
* Email :: ali.saeed.sirius@gmail.com
* GitHub :: https://github.com/alisaeed2022skipq
* Phone :: +92-344-5512351

 <br />

Thanks for Reading 👍
##### [Back-to-Top](#back-to-top)
