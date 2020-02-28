
## TODO
- Mapeamento de Dependências do projeto (Sistema, Bibliotecas do Projeto "Linguagem")
    - Bibliotecas do Projeto - Python/Django (Desenvolvedor)
    - Sistema (SO, Hardware, etc ) - (Desenvolvedor/DevOps/Infra)
    - Escolher servidor HTTP - (Apache, Nginx, Gunicorn, etc...)
    - Definir o provedor de serviço - (AWS, Google Cloud, Azure, etc...)
    - Mapeamento das conexões a sistemas externos (Banco de Dados, APIs Externas, etc...)
    - Definir o serviço de Logs e Telemetria

- Criar o Dockerfile (Recomendação: Usar imagem Python 3.7 - Alpine, Ubuntu)
    - Criação do arquivo
    - Testar a execução
    - Analizar o desempenho
- Criação do Pipeline
    - Definição das Etapas (Teste, Build, Detecção Vulnerabilidade, Deploy, Merge para outra Branch, etc...)
    - Escrever o Pipeline
    - Testar/Validar (Se todas as etapas estão funcionando)
- Criação do Ambiente (USAR SEMPRE IaC. Exemplo: Ansible, Terraform, Puppet, Vagrant, etc...)
    - Escolha do Sistema Operacional
    - Necessidade de um Orquestrador? (K8S, Docker Swarm, Rancher, Openshit, etc...)
    - Instalação de dependências do SO
    - Criação de Dominio e certificado
    - Regras de Firewall - Inbound, Outbound (Security Groups, Iptables, etc...)
    - Load Balancer
    - Backups

- Logs, Telemetria e Visualização
    - Escolher o serviço (ELK, Prometheus, Grafana, Cloud Watch, Zabbix, Cacti, etc...)
    - Instalação dos agentes, responsáveis pelo envio de métricas e logs para os serviços de coleta (Beats, etc...)
    - Regras de coleta (Periodicidade, Grok Filter, etc...)
