# Setup da máquina para rodar o projeto

## Usando WSL2 com o Windows

Assumindo que o WSL2 já esteja rodando com um Ubuntu configurado e nele já tenho o Python 3.12, Pyenv e Poetry instalados e configurados no mesmo, passamos para a parte da instalação do Docker:

Segui os 2 documentos que a Microsoft disponibiliza para instalação e configuraçào do mesmo. 

- https://learn.microsoft.com/pt-br/windows/wsl/tutorials/wsl-containers

- https://docs.docker.com/desktop/features/wsl/#download

## Espaço livre e em uso no WSL2

Caso queira consultar e gerenciar o espaço em disco do WSL2, basta seguir o comando desta doc:

https://learn.microsoft.com/pt-br/windows/wsl/disk-space

`wsl.exe --system -d <distribution-name> df -h /mnt/wslg/distro`
