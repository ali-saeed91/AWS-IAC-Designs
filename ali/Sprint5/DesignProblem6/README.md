> SkipQ Sirius: Sprint 5
# Welcome to Design Problem #6!
### Design Problem - 6: 

Design & Develop - Client needs a Notification System – that notifies the Admins about report summaries, users about operations within the system, and notifies clients/users about any changes. What AWS service(s) would you use for such a system?



##### [Back-to-Top](#back-to-top)
---

## **Table of Contents:**

* ### [Overview](#overview-1)
* ### [Design Diagram](#design-diagram-1)
* ### [Data Parsing](#cicd-pipeline)
* ### [Objective](#objective-1)
* ### [AWS Services](#aws-services-1)
* ### [Non AWS Services](#non-aws-services-1)
* ### [Getting Started](#getting-started-1)

    * ### [Environment Setup](#environment-setup-1)

    * ### [Project Setup](#project-setup-1)

    * ### [Project Deployment](#project-deployment-1)

* ### [Results](#results-1)
    
    * ### [CloudWatch](#cloudwatch-screenshots)

    * ### [SES](#ses-email-screenshots)

 * ### [References](#references-1)
 * ### [Useful Commands](#useful-commands-1)
 * ### [Author Contact](#author-contact-1)

<br />


>  ## Overview
 <br />

I have developed this project in order to build a Notification System – that notifies the Admins about report summaries, users about operations within the system, and notifies clients/users about any changes.  
The Parsing is done using FN Lambda.
The FN Lambda is utilised to parse the incomming event and extract the data from the incomming sources for Reports data and send the Operations Data to Client and Summary Reports to the Admin on Daily basis.

 * The respective emails are sent after parsing the data and sent via AWS SES service.
 
<br />
<br />

>  ## Design Diagram
<br />

![DesignDiagram6 (1)](https://user-images.githubusercontent.com/117926781/207837557-34a68412-1c31-4a83-84e2-cda48fad2f2b.jpg)

<br />
<br />

 > ## Data Parsing
 <br />

 To perform data extraction from the incomming event, i have performed parsing in FNApp.py:
 <br /> 

 * **FN Lambda (Extract, Read, Parse, Email and Store to DynamoDB)**
<br />

The **FN Lambda** application stage performs data extraction in the following steps:
* Extract CloudWatch Logs
* Adding to Dictionary
* Converting Timestamp
* Extract Number of Operations, Passed, Failed and Warnings
* Send the Operations parsed data to Client Email
* Send the Report Summary parsed data to Admin Email
<br /> 
<br />


> ## Objective
 <br />

 Main objective of this CDK application is to get a clear understanding of **How to build a Notification System – that notifies the Admins about report summaries, users about operations within the system, and notifies clients/users about any changes.**. 
 

 * Parsing is the process of converting formatted text into a data structure. A data structure type can be any suitable representation of the information engraved in the source text.

<br />


> ## AWS-Services
 <br />

 Below is the list of AWS Services that i have used while deploying my application on AWS:

 * **AWS SES**
 * **AWS CloudFormation**
 * **AWS Lambda**
 * **AWS DynamoDB**
 * **AWS CDK**
 * **AWS IAM**

<br />
 <br />

> ## Non AWS Services
 <br />

Below is the list of the Non AWS Services that i have used while deploying my application on AWS:

 * **Python Boto3 SDK**
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

    The **git add .** command adds the current changes to the staging layer, we can revert back if needed from this stage. The **git commit -m ""** command adds the changes from staging to history. The **git push** command pushes the changes from history to github and the changes are deployed to repository.
<br />
<br />


>## Results
In order to display the GUI screenshots of the multiple services that i have used in my project, with my final results and detailed information about the project and end results, please check below-pasted screenshots:


<br />

* #### CloudWatch Screenshots
<br />

![image](https://user-images.githubusercontent.com/117926781/207838405-50054b39-9465-4524-ab7f-036f1dd7071d.png)

<br/>

![image](https://user-images.githubusercontent.com/117926781/207838564-78489d54-96b4-49c0-b882-50a689a00918.png)

<br/>



* #### SES Email Screenshots
<br />

![image](https://user-images.githubusercontent.com/117926781/207838966-cf2fba93-6442-4dc2-813c-33c3b46c0226.png)
<br/>

![image](https://user-images.githubusercontent.com/117926781/207839089-e74fde2f-4e3b-49fb-b316-3e2e5cceb659.png)
<br/>

![image](https://user-images.githubusercontent.com/117926781/207839303-2992356e-11bb-453f-909e-69701187dfbc.png)
<br/>


<br />

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

* [AWS DynamoDB](https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_dynamodb/Table.html)

* [AWS Lambda](https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_lambda.html)

* [Parsing Dictionary Data](https://www.pythonpool.com/dictionary-to-list-python/)

* [2D Array Sort](https://www.delftstack.com/howto/python/sort-2d-array-python/)

* [Boto3 Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#bucket)

* [AWS SES](https://www.learnaws.org/2020/12/18/aws-ses-boto3-guide/)

<br />

> ## Author Contact
* Name :: Ali Saeed
* Email :: ali.saeed.sirius@gmail.com
* GitHub :: https://github.com/alisaeed2022skipq
* Phone :: +92-344-5512351

 <br />

Thanks for Reading 👍
##### [Back-to-Top](#back-to-top)
