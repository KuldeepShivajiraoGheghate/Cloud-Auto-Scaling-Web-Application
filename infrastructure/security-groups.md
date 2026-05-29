# Security Groups

## alb-security-group
Allows internet traffic to reach the Load Balancer.

| Rule | Protocol | Port | Source |
|---|---|---|---|
| Inbound | TCP | 80 | 0.0.0.0/0 |
| Inbound | TCP | 443 | 0.0.0.0/0 |
| Outbound | All | All | 0.0.0.0/0 |

## ec2-security-group
EC2 instances only accept traffic FROM the ALB — never directly from internet.

| Rule | Protocol | Port | Source |
|---|---|---|---|
| Inbound | TCP | 80 | alb-security-group |
| Inbound | TCP | 22 | 0.0.0.0/0 |
| Outbound | All | All | 0.0.0.0/0 |
