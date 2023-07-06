> SkipQ Sirius: Sprint 5
# Welcome to Design Problem #5!
### Design Problem - 5: 

Design & Develop - Suppose there are 10 files uploading to S3 bucket each day. For each file received on cloud storage, you have a mechanism to process the file. During the processing, your code parses the text and counts the number of times each word is repeated in the file. For example, in the following text: “Hello World and Hello There”, your code should be able to say that "hello" has been used twice, "world" has occurred once and so on. Then it will store the results in some storage and email to some email address after successful processing.


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
    
    * ### [S3 Bucket](#s3-bucket-screenshots)

    * ### [DynamoDB](#dynamodb-screenshots)

    * ### [SES](#ses-email-screenshots)

 * ### [References](#references-1)
 * ### [Useful Commands](#useful-commands-1)
 * ### [Author Contact](#author-contact-1)

<br />


>  ## Overview
 <br />

I have developed this project in order to build a mechanism to process daily uploaded files in S3, parse the file data for words, and frequencies so that i can store and email the parsed data.  
The upload of a file in S3 bucket triggers the S3 connected FN Lambda.
The FN Lambda is utilised to parse the incomming event and extract the **Filename** to read its content from S3. The data is parsed and decoded using **Regex**.The parsed data is converted to a dictionary containing the **Words & Frequencies** which are forwarded to a **User** email using **SES** service. The SES service perform identity verification to add user email and forwards the parsed data afterwards. The parsed data is then written to the DynamoDB **DB Table** using **batch_write** function along with the filename.

 * The event body contains the bucket and filename values which are extracted from event dictionary and passed to the parsing and email functions.
 
<br />
<br />

>  ## Design Diagram
<br />

![DesignDiagram5](https://user-images.githubusercontent.com/117926781/207477644-aecef61c-5fdd-4029-ab63-eff8e4e78a38.jpg)

<br />
<br />

 > ## Data Parsing
 <br />

 To perform data extraction from the incomming event, i have performed parsing in FNApp.py:
 <br /> 

 * **FN Lambda (Extract, Read, Parse, Email and Store to DynamoDB)**
<br />

The **FN Lambda** application stage performs data extraction in the following steps:
* Extract Bucket and File names from Event
* Read the File Contents
* Parse the File and Convert to Dictionary
* Verify Email first time only
* Send the File parsed data to Email
* Write the File parsed data to DB Table
<br /> 
<br />


> ## Objective
 <br />

 Main objective of this CDK application is to get a clear understanding of **How to build a mechanism to process daily uploaded files in S3, parse the file data for words, and frequencies so that i can store and email the parsed data.**. 
 

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

* #### S3 Bucket Screenshots
<br />

![image](https://user-images.githubusercontent.com/117926781/207487623-db1143ea-8fee-48ff-b8b2-221645db60c9.png)

<br/>

![image](https://user-images.githubusercontent.com/117926781/207488011-b6f2113b-fddc-48dd-843a-ce1d0153c0fc.png)

<br/>

![image](https://user-images.githubusercontent.com/117926781/207489897-9f222981-d79a-4cc3-bb53-7df19b0a575a.png)

<br/>

![image](https://user-images.githubusercontent.com/117926781/207489630-b17817c8-b12c-49a0-8b69-3326b7fabe12.png)

<br/>

![image](https://user-images.githubusercontent.com/117926781/207489057-86603f61-795e-4dbd-ae05-13dba7806044.png)



<br />

* #### DynamoDB Screenshots
<br />

![image](https://user-images.githubusercontent.com/117926781/207491504-97b61104-aed8-465d-8fbd-65bc650f63a6.png)
<br/>

![image](https://user-images.githubusercontent.com/117926781/207488353-27d82560-3646-4d77-9c67-d49f7e56c617.png)
<br/>

![image](https://user-images.githubusercontent.com/117926781/207490229-614b5027-adf4-4ccc-9ddb-508119e634fd.png)
<br/>

![image](https://user-images.githubusercontent.com/117926781/207491165-67481d77-9eea-4337-a096-b730593bd3da.png)


<br />

* #### SES Email Screenshots
<br />

![image](https://user-images.githubusercontent.com/117926781/207486507-de0bcf9c-1dc6-4b3b-8d8f-35d81311f18b.png)
<br/>

![image](https://user-images.githubusercontent.com/117926781/207486214-78f444a4-be9f-48d9-8a4e-78523c2aa30f.png)
<br/>

![image](https://user-images.githubusercontent.com/117926781/207488683-36d198a5-c1ee-4fda-bdba-51f98c67ff81.png)
<br/>

![image](https://user-images.githubusercontent.com/117926781/207490559-c01d1200-6a9f-42b0-bdbc-ddb123b85c9e.png)



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
