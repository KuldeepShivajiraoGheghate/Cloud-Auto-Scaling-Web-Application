# VPC Setup

## Configuration
- VPC Name: autoscaling-vpc
- CIDR: 10.0.0.0/16
- Region: us-east-1

## Subnets
| Subnet | CIDR | Availability Zone |
|---|---|---|
| autoscaling-subnet-public1 | 10.0.0.0/20 | us-east-1a |
| autoscaling-subnet-public2 | 10.0.16.0/20 | us-east-1b |

## Internet Gateway
- Name: autoscaling-igw
- State: Attached to autoscaling-vpc

## Settings
- DNS hostnames: Enabled
- DNS resolution: Enabled
- Auto-assign public IPv4: Enabled on both subnets
