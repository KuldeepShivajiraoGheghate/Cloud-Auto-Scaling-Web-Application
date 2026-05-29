# Launch Template

## Settings
- Name: autoscaling-launch-template
- AMI: Amazon Linux 2023
- Instance type: t3.micro
- Key pair: autoscaling-keypair
- Security group: ec2-security-group

## User Data Script
Runs automatically on every new EC2 instance at launch.

```bash
#!/bin/bash
yum update -y
yum install python3 -y
python3 /home/ec2-user/server.py &
```
