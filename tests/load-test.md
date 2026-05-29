# Load Test

## Tool
stress — CPU load generator for Linux

## Steps
```bash
# Connect to EC2 via Instance Connect
# Then run:

sudo yum install stress -y
sudo stress --cpu 4 --timeout 300
```

## Results
- CPU spiked to ~100%
- CloudWatch AlarmHigh fired after 3 datapoints
- ASG launched 3rd EC2 instance automatically
- Instance count: 2 → 3 during test
- Instance count: 3 → 2 after test ended
- Total scale-out time: ~3 minutes
