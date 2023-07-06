> SkipQ Sirius: Sprint 5
# Welcome to Design Problem #3!
### Design Problem - 3: 

1) **How would you automate deployment (e-g on AWS) for a system that has:**

* a. Source code in a repo.<br/>
* b. How do we generate an artifact from the repo that gets published and later is used in some services? <br/>
* c. Are there more than one solutions? <br/>

2) **Deploy, maintain and rollback pipeline for an artifact deployment e-g lambda package, docker image etc.**
* a. If the latest deployment is failing, why do you think that is? <br/>
* b. How will you rollback? <br/>
* c. How do you reduce such failures so there is less need to rollback? <br/>
##### [Back-to-Top](#back-to-top)
---

## Answers:
<br/>

> ## Question 1:
<br/>

**1):** AWS Code pipeline is a fully managed serverless CI/CD service that helps in automating the entire software delivery release. It is a pipeline wherein we can call all other services like Codebuild, CodeCommit, manual approvals, testing, deployment, etc., in any order and any number of times. Additionally, it is entirely serverless, works on a pay-as-you-go cost model with a fully secured & configurable workflow, and enables one place monitoring and rapid software delivery.

Services and tools:
Source Control repository: Github

Build: AWS CodeBuild

Deployment: AWS CodeDeploy

CI/CD Pipeline: AWS Codepipeline

Reference: https://www.xavor.com/blog/how-to-automate-deployments-on-aws/

The AWS CodePipeline integration with GitHub is relatively simple as well. After selecting GitHub as the source provider, click on the “Connect to GitHub” button.
To connect to GitHub, you’ll need to authenticate to your GitHub account. Your GitHub credentials should be entered here, not your AWS credentials.
Once you’ve authenticated to GitHub, you’ll need to review and authorize permissions for AWS to have admin access to Repository webhooks and services and all public and private repositories. Clicking on the “Authorize application” button will direct you to the AWS CodePipeline process to complete the integration.
Reviewing and Authorizing AWS Access to your GitHub Account
Finally, you’ll need to select the repository and branch to use as your source. Fortunately, the integration allows AWS to auto-populate the text boxes, so you don’t have to do too much additional typing.

Reference: https://www.sumologic.com/glossary/aws-codepipeline/

The pipeline downloads the code from the CodeCommit/Github repository, initiates the Build and Test action using CodeBuild, and securely saves the built artifact on the S3 bucket, which can used later by other services.

Reference: https://aws.amazon.com/blogs/devops/complete-ci-cd-with-aws-codecommit-aws-codebuild-aws-codedeploy-and-aws-codepipeline/


There are multiple solutions to implement CI/CD pipeline by using sources like, CodeCommit, Github, Gitlab, Bitbucket etc.
For Build we can use services like CodeBuild, Jenkins, Github Actions etc.
For Deploy we can use services like CodeDeploy, Terraform, Prometheus etc.

Reference: https://www.nclouds.com/blog/accelerate-cicd-pipeline-aws-codepipeline-codebuild/
https://spot.io/resources/aws-ci-cd-the-basics-and-a-quick-tutorial/

<br/>

> ## Question 2:
<br/>

![image](https://user-images.githubusercontent.com/117926781/207034830-9d051b52-ecc3-448d-9982-698bc59a5707.png)
**2):** In AWS CodePipeline, an action is a task performed on an artifact in a stage. A failure is an action in a stage that is not completed successfully. You can use the CLI to manually retry the failed action before the stage completes (while other actions are still in progress). If a stage completes with one or more failed actions, the stage fails, and the pipeline execution does not transition to the next stage in the pipeline.

You can retry the latest failed actions in a stage without having to run a pipeline again from the beginning. You do this by retrying the stage that contains the actions. You can retry a stage immediately after any of actions fail. All actions that are still in progress continue their work, and failed actions are triggered once again.

Reference: https://docs.aws.amazon.com/codepipeline/latest/userguide/actions-retry.html

CodeDeploy rolls back deployments by redeploying a previously deployed revision of an application as a new deployment. These rolled-back deployments are technically new deployments, with new deployment IDs, rather than restored versions of a previous deployment.

Deployments can be rolled back automatically or manually.

Topics: <br/>
* Automatic rollbacks<br/>
* Manual rollbacks <br/>
* Rollback and redeployment workflow<br/>
* Rollback behavior with existing content<br/>

Reference: https://docs.aws.amazon.com/codedeploy/latest/userguide/deployments-rollback-and-redeploy.html

Amazon didn’t start out practicing continuous delivery, and developers here used to spend hours and days managing deployments of their code to production. We adopted continuous delivery across the company as a way to automate and standardize how we deployed software and to reduce the time it took for changes to reach production. Improvements to our release process built up incrementally over time. We identified deployment risks and found ways to mitigate those risks through new safety automation in pipelines. We continue to iterate on the release process by identifying new risks and new ways of improving deployment safety. To learn more about our journey to continuous delivery and how we continue to improve, see the Builders’ Library article Going faster with continuous delivery.

Reference: https://aws.amazon.com/builders-library/automating-safe-hands-off-deployments/

<br />

> ## Author Contact
* Name :: Ali Saeed
* Email :: ali.saeed.sirius@gmail.com
* GitHub :: https://github.com/alisaeed2022skipq
* Phone :: +92-344-5512351

 <br />

Thanks for Reading 👍
##### [Back-to-Top](#back-to-top)
