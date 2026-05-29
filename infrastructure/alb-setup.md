# Application Load Balancer Setup

## Load Balancer
- Name: autoscaling-alb
- Type: Application Load Balancer
- Scheme: Internet-facing
- VPC: autoscaling-vpc
- Subnets: both public subnets

## Target Group
- Name: autoscaling-target-group
- Protocol: HTTP:80
- Target type: Instance
- Health check path: /
- Health check interval: 10 seconds
- Healthy threshold: 2
- Unhealthy threshold: 2
