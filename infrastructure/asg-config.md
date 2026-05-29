# Auto Scaling Group Configuration

## ASG Settings
- Name: autoscaling-asg
- Launch template: autoscaling-launch-template
- Min capacity: 1
- Desired capacity: 2
- Max capacity: 4

## Scaling Policy
- Type: Target Tracking
- Metric: Average CPU Utilization
- Target: 50%
- Scale-out: CPU > 50% for 3 datapoints
- Scale-in: CPU < 35% for 15 datapoints
- Warmup period: 120 seconds

## Health Check
- Type: ELB
- Grace period: 120 seconds
