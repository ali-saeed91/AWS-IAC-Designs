> SkipQ Sirius: Sprint 6
# Welcome to the, Use docker to build API test clients using pyresttest Project!
#### An AWS CDK application to implement Docker containerization for Functional Tests using Pyresttest library in a CI/CD Pipeline for the Web Crawler application which monitors the resource web health. 


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
    
    * ### [CodePipeline](#aws-codepipeline-screenshots)

    * ### [Unit Test Pytest](#unit-test-pytest-screenshots)

    * ### [API Tests Docker Pyresttest](#api-functional-pyresttest-with-docker-screenshots)

 * ### [References](#references-1)
 * ### [Useful Commands](#useful-commands-1)
 * ### [Author Contact](#author-contact-1)

<br />


>  ## Overview
 <br />

I have developed this project in order to build a cdk application to implement **Docker** containerization for **API Functional Tests** using **Pyresttest** library and Publish the built images to Elastic Container Registry (**ECR**), so that i can run unit and API functional tests in CI/CD Pipeline on the web crawler’s CRUD endpoint built in **Sprint 4**.
To implement this Project i am building a docker image for the **Pyresttest** library in the **AWS CodePipeline**. The image is built using **AWS CodeBuild** and published to the **ECR** (Elastic Container Repository). The **Pytest** library is utilised to perform **Unit** test in the **Beta Pre Build Stage**. The **API Functional Tests** are performed in the **Beta Post Deploy Stage** using the built **Docker Image** from **ECR** which is initilized in a **Docker Container**. The API tests using **Pyresttest** tests check the functionality of the **CRUD** endpoint for **GET**, **POST**, **PUT** and **DELETE** methods. On passing the Beta Testing stage the **CI/CD** pipeline moves to the **Production Stage** which requires Manual Approval to proceed further.

 * The Unit and Functional tests logs can be seen in **AWS CodeBuild** service.
 
<br />
<br />

>  ## Design Diagram
<br />

![sprint6design](https://user-images.githubusercontent.com/117926781/209358452-e519b307-7264-4a78-844c-3b43943d27d5.jpg)

<br />
<br />


> ## Objective
 <br />

 Main objective of this CDK application is to get a clear understanding of **How to implement Docker containerization for Functional Tests using Pyresttest library and Publish the built images to Elastic Container Registry (ECR), to run unit and API tests in CI/CD Pipeline on the web crawler’s CRUD endpoint built in Sprint 4**. 
 
A Docker image is a file used to execute code in a Docker container. Docker images act as a set of instructions to build a Docker container, like a template. Docker images also act as the starting point when using Docker. An image is comparable to a snapshot in virtual machine (VM) environments.

* **Base image**: The user can build this first layer entirely from scratch with the build command.

* **Parent image**: As an alternative to a base image, a parent image can be the first layer in a Docker image. It is a reused image that serves as a foundation for all other layers.

* **Layers**: Layers are added to the base image, using code that will enable it to run in a container. Each layer of a Docker image is viewable under /var/lib/docker/aufs/diff, or via the Docker history command in the command-line interface (CLI).

<br />


> ## AWS-Services
 <br />

 Below is the list of AWS Services that i have used while deploying my application on AWS:

 * **AWS API Gateway**
 * **AWS CodePipeline**
 * **AWS CloudFormation**
 * **AWS Lambda**
 * **AWS ECR**
 * **AWS CDK**
 * **AWS IAM**
 

<br />
 <br />

> ## Non AWS Services
 <br />

Below is the list of the Non AWS Services that i have used while deploying my application on AWS:

 * **Python Boto3 SDK**
 * **Pytest**
 * **Pyresttest**
 
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

    The **git add .** command adds the current changes to the staging layer, we can revert back if needed from this stage. The **git commit -m ""** command adds the changes from staging to history. The **git push** command pushes the changes from history to github and once the changes are deployed, the **AWS  CodePipeline** will fetch the changes from the **source** and starts to update the entire pipeline automatically.
<br />
<br />


>## Results
In order to display the GUI screenshots of the multiple services that i have used in my project, with my final results and detailed information about the project and end results, please check below-pasted screenshots:


<br />

* #### AWS CodePipeline Screenshots
<br />

![image](https://user-images.githubusercontent.com/117926781/209361454-aac781da-a511-4ef0-b094-dcdd1e99032f.png)

![image](https://user-images.githubusercontent.com/117926781/209361677-82acc3af-8d4a-4be9-a7c4-5c57a4dbc789.png)

![image](https://user-images.githubusercontent.com/117926781/209362220-108e44da-8ca7-43f6-89fe-a66a82214abb.png)

![image](https://user-images.githubusercontent.com/117926781/209362525-dc42d0e2-c627-4df0-af4f-e7922adf0688.png)

<br/>


* #### Unit Test (Pytest) Screenshots
<br />

![image](https://user-images.githubusercontent.com/117926781/209362747-cb609561-6c70-48c6-b0c3-b296972a5c4a.png)
<br/>
<br/>

* #### API Functional (Pyresttest) with Docker Screenshots
<br />

![image](https://user-images.githubusercontent.com/117926781/209363215-ef9aed77-3a61-4673-af0f-506a911496c0.png)
<br/>

![image](https://user-images.githubusercontent.com/117926781/209363726-efeb0bea-1a73-4491-9190-2787c11e9b71.png)
<br/>

![image](https://user-images.githubusercontent.com/117926781/209364169-49e8abfb-000e-4f67-add5-580fc12544e8.png)
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

* [Docker](https://docker-curriculum.com/)

* [Pytest](https://docs.pytest.org/en/6.2.x/fixture.html)

* [Pyresttest](https://github.com/svanoort/pyresttest)

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
