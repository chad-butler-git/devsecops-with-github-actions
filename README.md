# devsecops-with-github-actions
Resource files for DevSecops with GitHub Actions Course

## Source Files
* /aws - contains scripts for AWS infra, such as the cloudformation script
  * cf-ec2.yaml - generates ec2 instance, the security group, and an IAM policy that will be attached to a user.
* /git - contains scripts for github
  * /git/workflows - contains origin copies of workflow action scripts.
    * deploy.yaml - deploys Pygoat to an EC2 instance
    * 

## GitHub Secrets
The following GitHub secrets are needed to run workflows

* HOST (public dns name)
* USERNAME (ec2-user)
* KEY (SSH private key used to access EC2 instance)
* AWS_ACCESS_KEY_ID (from IAM user)
* AWS_SECRET_ACCESS_KEY (from IAM user)
* PORT (SSH port of EC2 instance - 22)

## Troubleshooting
### CloudFormation Stack
Check the following for errors:
* /var/log/cloud-init-output.log - look at the end of the file for errors.
* /var/log/cfn-init.log
* /var/log/cfn-init-cmd.log
