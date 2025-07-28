# Overengineered backend
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
![Python](https://img.shields.io/badge/python-3.13+-blue?logo=python&style=flat-square)


## Goal of this project
- Understand all the things I want to use in a project but failed to since i get overwhelmed easily

## Endgoal
> [!Note]
> This infra sys design will not include info on postgres/redis etc unless I find something interesting that warrants mentioning them here

- [X] For code quality
    - [X] I intend to add a pre commit hook that uses ruff and pyright

- [ ] Deploy to Container Apps/ ECS/ Cloud Run, will prolly use container apps due to some free creds i have
    - [ ] To do that i intend to push to Container/image registry of sorts from whichever cloud provider of choice or might even be docker hub. This process should be done through a gh action not manually

- [ ] File uploads to S3 attached to a cdn.
    - [ ] S3 file upload setup
    - [ ] CDN setup

- [ ] Observability
    - [ ] Since we will use gunicorn and the beginning we need its logs send to alloy as well along with nginx maybe
    - [ ] Since I will be using docker compose I want to set it up in such a way that it has alloy in it 
    - [ ] It will be attacked to Loki and graphana which will be from the companies own free tier

- [ ] Deploy to bare metal VM
    - This is to have some exposure to absolute control in some sense
        - There wont be any auto scaling
        - It will have nginx and I will have to handle certificates too
        - This will need some cheap domain name as well to ensure its https
    - Use cloudflare rev proxy or check for alternatives as well

- [ ] Local dev setup 
    - Docker compose
        - Will have nginx contaner routing traffic instead of say cloudflare

- [ ] Over the top dev setup
    - Use docker swarm to have some level of auto scaling

- [ ] As for django specific goal 
    - [ ] Have swagger ui things under proper auth, preferrably google OAuth
    - [ ] Support async and not sync

- [ ] Prolly a bit more advanced things
    - [ ] have canary deploment
    - [ ] try out certbot for and lets encrypt for auto certs renewal for https
    - [ ] Add dependabot scanning
    - [ ] Traces and metrics 
    - [ ] Perf test maybe k6
    - [ ] IaC
    - [ ] Feature Flags(but no idea how to implement yet)
    - [ ] Chaos monkey in CI CD but will it be useful here need to read more about it
