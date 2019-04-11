# DC Docker logs test

Will be playing around writing code to test docker and logs with EC2

To run Logging correctly use this command

```
    sudo docker run --log-driver=awslogs --log-opt awslogs-region="us-west-2" --log-opt awslogs-group="docker-logs" --log-opt awslogs-stream="docker1" -d docker-image
```
