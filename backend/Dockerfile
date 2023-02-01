FROM python:3.10-alpine
ENV PYTHONUNBUFFERED 1
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install --upgrade pip pipenv
WORKDIR /backend
COPY ./Pipfile* ./
COPY . .
RUN pipenv sync
ENV PORT ${PORT}
COPY ./entrypoint.sh /entrypoint.sh
RUN chmod o+x /entrypoint.sh
ENTRYPOINT ["sh", "-c", "/entrypoint.sh"]
EXPOSE 8080