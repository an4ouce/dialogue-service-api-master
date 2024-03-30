# Fastapi gateway for dialogue service

Quick access to the open api specification of the service - [here](./openapi.yaml)

Visualize - [here](https://editor.swagger.io)

## Начало работы

```console
git clone https://github.com/an4ouce/dialogue-service-api-master
```
### Необходимое для запуска

- Убедитесь, что у вас установлен Docker и Docker Compose
  - Windows или macOS:
    [Установить Docker Desktop](https://www.docker.com/get-started)
  - Linux: [Установить Docker](https://www.docker.com/get-started) и затем
    [Docker Compose](https://github.com/docker/compose)

### Запуск

Приложение может быть запущено на локальном компьютере с помощью команд:

```console
sudo docker-compose run --rm "dialog-api" make migrate
```
```console
sudo docker-compose up --build -d
```
## Enjoy! 
