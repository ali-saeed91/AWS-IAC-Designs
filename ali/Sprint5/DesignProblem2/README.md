> SkipQ Sirius: Sprint 5
# Welcome to Design Problem #2!
### Design Problem - 2: 

Design & Develop - Consider that you are getting events in the format [{“event1”:{“attr1”: value }}] from different APIs.
1) How will you parse the event to get the value?
2) How will you return 10 latest events when required?



##### [Back-to-Top](#back-to-top)
---

## **Table of Contents:**

* ### [Overview](#overview-1)
* ### [Design Diagram](#design-diagram-1)
* ### [CD API Gateway](#crud-api-gateway-1)
* ### [Data Parsing](#cicd-pipeline)
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

    * ### [Lambda Tests](#wh-lambda-test-screenshots)

 * ### [References](#references-1)
 * ### [Useful Commands](#useful-commands-1)
 * ### [Author Contact](#author-contact-1)

<br />


>  ## Overview
 <br />

I have developed this project in order to build two API endpoints which are getting events in the format **[{“event1”:{“attr1”: value }}]** and store them in DynamoDB Table, so that i can parse the events to get 10 latest values when required.  
The CD (create and delete) operation is performed using the **Amazon API Gateway** service and "2" RESTFUL API's are created following the **HTTP** Protocol to perform the **POST** and **DELETE** methods. Upon method request and successful method operation an **HTTP statusCode:200** is sent in response and the data is modified in the DynamoDB table. To store the data in ARG DynamoDB table, i have utlised Api Lambda with custom **Parsing** functions on the incomming event: **[{“event1”:{“attr1”: value }}]**  to extract the **value**, **timestamp**, **id** and **apiId** using Python libraries i.e **boto3**, **datetime**, **uuid**, **ast** and **json**. The WH Lambda is utilised to do TEST requests from the **ARG DynamoDB table** to fetch the latest "10" records based on **timestamp**, to perform this i have used custom functions to **Parse** the data scanned from the ARG table and displayed the latest available records.

 * The attr1 dictionary value is extracted from event1 dictionary which is located inside a global Array.
 
<br />
<br />

>  ## Design Diagram
<br />

![image](https://user-images.githubusercontent.com/117926781/206271362-f1bb2a27-b416-46a1-ad1e-c0cdf38e65c2.png)

<br />

>  ## CD API Gateway
 <br />

 The RESTFUL CD API Gateway is implemented by using **AWS API Gateway** which uses the **HTTP** Protocol with the request and response messages to perform the RESTFUL API operations of Create, and Delete. From the **AWS API Gateway** i have used the Lambda invoked API Gateway to integrate the API Lambda with the RESTFUL endpoints to perform the following 2 methods:
 <br /> 

 * **POST**
 * **DELETE**
<br />


The **POST** method performs the functionality to send the data in the **request** body to the ARG DynamoDB table and upon successful put function an **HTTP statusCode:200** is sent and data is written in the DynamoDB table.
<br />


The **DELETE** method  performs the functionality to delete a record in the table by using the delete function. A key:value pair is sent the request body and upon successful delete operation an **HTTP statusCode:200** is sent and the respective data is deleted in the DynamoDB table.
<br />
<br />

 > ## Data Parsing
 <br />

 To perform data extraction from the incomming event, i have performed parsing in 2 stages:
 <br /> 

 * **API Lambda (Extract and Store to DynamoDB)**
 * **WH Lambda (Fetch and Parse)**
<br />

The **API Lambda** application stage performs data extraction in the following steps:
* Extract the **body** from the event
* Convert to JSON string
* Convert JSON string to Python Obj
* Convert String Dictionary to Dictionary
* Extract Value from Dictionary
* Generate unique Id
* Generate Timestamp
* Extract Api Id
* Performing CD Operations

The **WH Lambda** application stage perform fetch's data in the following steps:
* Executing functions to fetch DynamoDB Data
* Parsing the DynamoDB Data
* Create and Sort 2D attributes Array
* Fetch Latest 10 Records from 2D Array
* Printing Values wrt Timestamp (descending)
<br /> 
<br />


> ## Objective
 <br />

 Main objective of this CDK API Gateway application is to get a clear understanding of **How to Make API endpoints which are getting events in the format [{“event1”:{“attr1”: value }}] and store them in DynamoDB Table, along with parsng to get 10 latest values when required**. 
 
 * CD stands for (Create and Delete) in its base form, CRUD is a way of manipulating information, describing the function of an application.
 * REST is controlling data through HTTP commands. It is a way of creating, modifying, and deleting information for the user.
 * Parsing is the process of converting formatted text into a data structure. A data structure type can be any suitable representation of the information engraved in the source text.

<br />
<br />

> ## AWS-Services
 <br />

 Below is the list of AWS Services that i have used while deploying my application on AWS:

 * **AWS API Gateway**
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

* #### API Gateway Screenshots
<br />

![image](https://user-images.githubusercontent.com/117926781/206287678-48514320-4824-4e5d-80fa-1df4086f0ffc.png)

![image](https://user-images.githubusercontent.com/117926781/206288171-d5926246-c34d-45a5-9d4f-dee0a802a73e.png)

![image](https://user-images.githubusercontent.com/117926781/206288337-bf2a0a15-0622-45f0-aca1-76e0af4c0f4e.png)

![image](https://user-images.githubusercontent.com/117926781/206288801-b8879122-b89a-436c-9810-70b762a697a9.png)

![image](https://user-images.githubusercontent.com/117926781/206289167-58dc1fb2-3fb8-4b41-a2e1-c5d29023ae48.png)



<br />

* #### DynamoDB Screenshots
<br />

![image](https://user-images.githubusercontent.com/117926781/206289589-8218315f-d465-458d-aa78-ec0cfd93fa24.png)

![image](https://user-images.githubusercontent.com/117926781/206289926-6a93fdfc-1b9b-400d-b362-55f9d67ed7c0.png)

![image](https://user-images.githubusercontent.com/117926781/206290863-ba3c984e-1672-41ce-a522-ee398f301c40.png)

![image](https://user-images.githubusercontent.com/117926781/206291183-7bfca55b-28b8-4339-9215-b414214a77de.png)

<br />

* #### WH Lambda (TEST) Screenshots
<br />

![image](https://user-images.githubusercontent.com/117926781/206291600-ef99e148-918f-4b47-8289-1ef8047cc928.png)

![image](https://user-images.githubusercontent.com/117926781/206292047-14c820a5-4592-4171-a3e9-547f698d1a40.png)

![image](https://user-images.githubusercontent.com/117926781/206294147-a1f20018-31d8-452a-97cc-36d1d68aa216.png)

![image](https://user-images.githubusercontent.com/117926781/206294520-9cde1b3c-8144-4d54-9b8a-98af3d7771ed.png)

![image](https://user-images.githubusercontent.com/117926781/206295212-e9b01402-045c-4497-8823-2a0333eb2902.png)

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

* [AWS API Gateway](https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_apigateway/README.html)

* [AWS API Reference](https://docs.aws.amazon.com/cdk/api/v2/python/modules.html)

* [AWS DynamoDB](https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_dynamodb/Table.html)

* [AWS Lambda](https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_lambda.html)

* [Parsing Dictionary Data](https://www.pythonpool.com/dictionary-to-list-python/)

* [2D Array Sort](https://www.delftstack.com/howto/python/sort-2d-array-python/)

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
