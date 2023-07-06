FROM thoom/pyresttest

COPY ./tests /usr/src/app 

WORKDIR /usr/src/app

ENTRYPOINT [ "pyresttest"]

CMD ["https://siviiizfqg.execute-api.us-east-2.amazonaws.com/","api_tests.yml"]