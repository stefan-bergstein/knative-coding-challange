

```

podman build -t sender:latest -f Containerfile .


podman run -it --rm --name sender --network host  sender:latest  send-cloudevents.py --broker http://192.168.2.221:8080

```