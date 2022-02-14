# Scripts to check if you are able to login or not

## How to build

- `sudo docker build . -t logintest`
- `sudo docker run -d --name logintest -p 8501:8501 -v $(pwd):/app -e TZ='Asia/Kolkata' -e host=<HOST> -e port=<PORT> -e username=<USERNAME> -e password=<PASSWORD> -e mode=<MODE> logintest`
