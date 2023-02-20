---
# User change
title: "Deploy Lambda functions on AArch64 (ARM64) using Python"

weight: 3 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

##  Deploy Lambda functions on AArch64 (ARM64) using Python 

## Prerequisites

* An [AWS account](https://portal.aws.amazon.com/billing/signup?nc2=h_ct&src=default&redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation#/start)
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
* [Terraform](/content/install-tools/terraform.md)

## Deploy Lambda function via Terraform

To generate an **access key** and **secret key**, follow the instructions mentioned in this [document](/content/learning-paths/server-and-cloud/lambda_function/nodejs_deployment.md).
To deploy AWS Lambda functions, we need the **main.tf**, **output.tf** and **lambda_function (python_lambda.py)** files.

Here is the **python_lambda.py** file

```console

def lambda_handler(event, context):
    message = 'Hello {} {}!'.format(event['first_name'], event['last_name'])
    return {
        'message' : message
    }

```
The above Lambda function will simply print `event.name` value as an output.

Here is the complete **main.tf** file

```console
provider "aws" {
  region = "us-east-2"
  access_key  = "Axxxxxxxxxxxxxxxxxxxx"
  secret_key   = "Rxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
}

provider "archive" {}

data "archive_file" "lambda_zip_dir" {
  type        = "zip"
  output_path = "hello_lambda.zip"
  source_file  = "hello_lambda.py"
}
data "aws_iam_policy_document" "policy" {
  statement {
    sid    = ""
    effect = "Allow"

    principals {
      identifiers = ["lambda.amazonaws.com"]
      type        = "Service"
    }

    actions = ["sts:AssumeRole"]
  }
}

resource "aws_iam_role" "iam_for_lambda" {
  name               = "iam_for_lambda"
  assume_role_policy = "${data.aws_iam_policy_document.policy.json}"
}

resource "aws_lambda_function" "lambda" {
  function_name = "python_lambda"
  filename         = "${data.archive_file.lambda_zip_dir.output_path}"
  source_code_hash = "${data.archive_file.lambda_zip_dir.output_base64sha256}"
  role    = "${aws_iam_role.iam_for_lambda.arn}"
  handler = "hello_lambda.lambda_handler"
  runtime = "python3.8"
  architectures = ["arm64"]
}

data "aws_lambda_invocation" "example" {
  function_name = aws_lambda_function.lambda.function_name

  input = <<JSON
{
  "first_name": "Arm-",
  "last_name": "user"
}
JSON
}

output "result" {
  value = "${data.aws_lambda_invocation.example.result}"
}


```
**NOTE:-** Replace `access_key` and `secret_key` with your values.

In the **main.tf** file mentioned above, a Lambda function is being created. Additionally, we are creating a Lambda function specific IAM role. Lambda functions use the **ZIP** file of code for uploading, so we are using the resource `Archive` for this purpose.
We are using `lambda invoke` resource in our **main.tf** file for invoking our Lambda function.

Here is the **output.tf** file

```console
output "lambda" {
  value = "${aws_lambda_function.lambda.qualified_arn}"
}

```
We are printing the **ARN** (Amazon Resource Names) of the Lambda resource in the above **output.tf** file.

Now, use the Terraform commands below to deploy **main.tf** file.


### Terraform Commands

**Initialize Terraform**

Run `terraform init` to initialize the Terraform deployment. This command is responsible for downloading all dependencies which are required for the AWS provider.

```console
terraform init
```
    
![Screenshot (255)](https://user-images.githubusercontent.com/92315883/209255228-8c8b1b17-ce55-4c7d-9916-6c15918fc82e.png)

**Create a Terraform execution plan**

Run `terraform plan` to create an execution plan.

```console
terraform plan
```

**NOTE:** The **terraform plan** command is optional. You can directly run **terraform apply** command. But it is always better to check the resources about to be created.

**Apply a Terraform execution plan**

Run `terraform apply` to apply the execution plan to your cloud infrastructure. The below command creates all required infrastructure.

```console
terraform apply
```      
![Screenshot (351)](https://user-images.githubusercontent.com/92315883/216279981-a46e3cd0-50a0-4c93-b9e5-2c77ea84f865.png)

### Verify the Lambda function

To verify the deployment of Lambda functions on AWS console, go to **Lambda » Functions**. We will see our Lambda function as below:

![Screenshot (354)](https://user-images.githubusercontent.com/92315883/216284315-dec9b16c-bc34-4752-8408-e5af819ea030.png)

![Screenshot (357)](https://user-images.githubusercontent.com/92315883/216515003-78546861-9d21-4d79-995c-0c2b5073feec.png)

**NOTE:**- To execute Lambda functions on the Graviton processor, we set "architectures = ["arm64"]".
