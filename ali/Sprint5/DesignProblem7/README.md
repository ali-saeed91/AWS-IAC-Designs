> SkipQ Sirius: Sprint 5
# Welcome to Design Problem #7!
### Design Problem - 7: 

Design & Develop - What if we have a 15MB file that we have to upload on S3 using API gateway. We have the limitation that our API gateway has the maximum payload capacity of 10MB. How will you solve this problem?



##### [Back-to-Top](#back-to-top)
---

## **Table of Contents:**

* ### [Overview](#overview-1)
* ### [Design Diagram](#design-diagram-1)
* ### [Objective](#objective-1)
* ### [AWS Services](#aws-services-1)
* ### [Non AWS Services](#non-aws-services-1)
* ### [Getting Started](#getting-started-1)

    * ### [Environment Setup](#environment-setup-1)

    * ### [Project Setup](#project-setup-1)

    * ### [Project Deployment](#project-deployment-1)

* ### [Results](#results-1)
    
    * ### [API Gateway](#api-gateway-screenshots)

    * ### [POSTMAN](#postman-screenshots)

    * ### [S3 BUCKET](#s3-bucket-screenshots)

 * ### [References](#references-1)
 * ### [Useful Commands](#useful-commands-1)
 * ### [Author Contact](#author-contact-1)

<br />


>  ## Overview
 <br />

I have developed this project in order to build a cdk application to upload files of 10MB+ on S3 using API gateway, so that i can overcome the limitation of API gateway having maximum payload capacity of 10MB.
To solve the payload capacity issue, I have designed the application utilising the **Presigined URL** function from **Boto3** SDK. The user sends the filename utilising the API Gateway endpoint and in response the **FN Lambda** generetes a Pre signed Post url along with the necessary headers and authenticaton signatures and send them in response back to the user. The user will use the **URL** and the security information to send the respective file using any **Frontend** application client, In this case i have utilised **POSTMAN**. A **POST** request is sent on the generated url using the authentication **AccessID**, **key**, **policy**, **signatures** and **file to upload** using the form-data option in request body, in response a status code **204** is sent along with the integer **1** to indicate that the file has been uploaded to target **S3 Bucket**.

 * The maximum payload capacity of API Gateway is of 10MB.
 
<br />
<br />

>  ## Design Diagram
<br />

![Design-Diagram7](https://user-images.githubusercontent.com/117926781/208171387-c1afe356-76d0-4550-a0be-78d7b4920544.jpg)

<br />
<br />


> ## Objective
 <br />

 Main objective of this CDK application is to get a clear understanding of **How to build a cdk application to upload files of 15MB+ on S3 using API gateway, so that to overcome the limitation of API gateway having maximum payload capacity of 10MB.**. 
 
 A presigned URL is a URL that you can provide to your users to grant temporary access to a specific S3 object. Using the URL, a user can either READ the object or WRITE an Object (or update an existing object). The URL contains specific parameters which are set by your application. A pre-signed URL uses three parameters to limit the access to the user;

* Bucket: The bucket that the object is in (or will be in)
* Key: The name of the object
* Expires: The amount of time that the URL is valid

<br />


> ## AWS-Services
 <br />

 Below is the list of AWS Services that i have used while deploying my application on AWS:

 * **AWS API Gateway**
 * **AWS CloudFormation**
 * **AWS Lambda**
 * **AWS S3**
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

![image](https://user-images.githubusercontent.com/117926781/208176012-0686e3a8-468d-4e22-8024-3f857edf1837.png)

![image](https://user-images.githubusercontent.com/117926781/208176439-e74bad46-a8ce-40ef-ad39-7781611ff832.png)

![image](https://user-images.githubusercontent.com/117926781/208178939-9d1e59e4-4203-47de-a5ef-031440ef2cf8.png)

<br/>


* #### POSTMAN Screenshots
<br />

![image](https://user-images.githubusercontent.com/117926781/208178258-39d559b2-d62d-409b-b35d-051e74db5354.png)
<br/>

![image](https://user-images.githubusercontent.com/117926781/208179339-891da147-a760-4229-950a-6ea3f4954401.png)
<br/>

* #### S3 Bucket Screenshots
<br />

![image](https://user-images.githubusercontent.com/117926781/208178461-fbbc2a58-42d0-4364-a36a-dbf597fbe049.png)
<br/>

![image](https://user-images.githubusercontent.com/117926781/208178704-47e7d3e9-4ee6-4a9b-901e-5d071877ea2d.png)
<br/>

![image](https://user-images.githubusercontent.com/117926781/208179618-57a33b9f-101f-4b05-9d64-41eb865ec1f1.png)
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

* [AWS Lambda](https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_lambda.html)

* [API Gateway](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html)

* [Pre Signed URL](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-presigned-urls.html)

* [Boto3 Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#bucket)


<br />

> ## Author Contact
* Name :: Ali Saeed
* Email :: ali.saeed.sirius@gmail.com
* GitHub :: https://github.com/alisaeed2022skipq
* Phone :: +92-344-5512351

 <br />

Thanks for Reading 👍
##### [Back-to-Top](#back-to-top)
