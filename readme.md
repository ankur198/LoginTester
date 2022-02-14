# Login Tester
Scripts to check if you are able to login or not

## How to run

Replace variables `<VARIABLE>` before running command

- mac/linux
    ```bash
    sudo docker run -d \
        --name logintester \
        -p 8501:8501 \
        -v $(pwd):/app \
        -e TZ='Asia/Kolkata' \
        -e host=<HOST> \
        -e port=<PORT> \
        -e username=<USERNAME> \
        -e password=<PASSWORD> \
        -e mode=<MODE> \
        ankur198/logintester
    ```
- powershell
    ```pwsh
    sudo docker run -d `
        --name logintester `
        -p 8501:8501 `
        -v $(pwd):/app `
        -e TZ='Asia/Kolkata' `
        -e host=<HOST> `
        -e port=<PORT> `
        -e username=<USERNAME> `
        -e password=<PASSWORD> `
        -e mode=<MODE> `
        ankur198/logintester
    ```

`mode` can be either `ldap` or `jira` at the moment

You can now monitor logs at [localhost:8501](https://localhost:8501)