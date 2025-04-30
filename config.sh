#!/bin/bash

# Cores ANSI
RED='\033[0;31m'
GREEN='\033[0;32m'
CYAN='\033[0;36m'
YELLOW='\033[1;33m'
BOLD='\033[1m'
RESET='\033[0m'

# Função com cor para simular digitação
type_effect() {
    text="$1"
    color="${2:-$RESET}"
    delay="${3:-0.03}"
    while IFS= read -r -n1 char; do
        printf "${color}%s${RESET}" "$char"
        sleep "$delay"
    done <<< "$text"
    echo
}

# Arte ASCII com cor ciano
echo -e "${CYAN}"
cat << "EOF"
 _______                             _________                                    
 \      \   ____  __ _________  ____ \_   ___ \  ___________  ____   ____ _____   
 /   |   \_/ __ \|  |  \_  __ \/  _ \/    \  \/ /  _ \_  __ \/  _ \ /    \\__  \  
/    |    \  ___/|  |  /|  | \(  <_> )     \___(  <_> )  | \(  <_> )   |  \/ __ \_
\____|__  /\___  >____/ |__|   \____/ \______  /\____/|__|   \____/|___|  (____  /
        \/     \/                            \/                         \/     \/
EOF
echo -e "${RESET}"

# Detectar sistema operacional
OS_NAME=$(uname -s)
DISTRO=""
BASE=""

if [ -f /etc/os-release ]; then
    . /etc/os-release
    DISTRO=$NAME
    case "$ID_LIKE" in
        *debian*) BASE="Debian/Ubuntu" ;;
        *rhel*|*fedora*) BASE="Red Hat/Fedora" ;;
        *arch*) BASE="Arch Linux" ;;
        *suse*) BASE="SUSE" ;;
        *) BASE="Desconhecida" ;;
    esac
else
    DISTRO=$OS_NAME
    BASE="Desconhecida"
fi

type_effect "Bem-vindo ao instalador do projeto Dashboard COVID-19." "$CYAN"
type_effect "Detectando o sistema operacional..." "$YELLOW"
sleep 1
type_effect "Sistema: $DISTRO" "$GREEN"
type_effect "Base: $BASE" "$GREEN"
echo

# Verificar e instalar Python se necessário
type_effect "Verificando a instalação do Python..." "$YELLOW"
if ! command -v python3 &> /dev/null; then
    type_effect "Python3 não encontrado. Iniciando instalação..." "$RED"
    if [[ "$BASE" == "Debian/Ubuntu" ]]; then
        sudo apt update && sudo apt install -y python3 python3-venv python3-pip
    elif [[ "$BASE" == "Red Hat/Fedora" ]]; then
        sudo dnf install -y python3 python3-venv python3-pip
    elif [[ "$BASE" == "Arch Linux" ]]; then
        sudo pacman -Syu python python-virtualenv python-pip
    else
        type_effect "Base do sistema não reconhecida. Por favor, instale o Python3 manualmente." "$RED"
        exit 1
    fi
else
    type_effect "Python3 já está instalado." "$GREEN"
fi
echo

# Criar e ativar ambiente virtual
type_effect "Criando ambiente virtual 'Configs'..." "$CYAN"
python3 -m venv Configs
source Configs/bin/activate
type_effect "Ambiente virtual ativado." "$GREEN"
echo

# Instalar dependências
type_effect "Instalando bibliotecas necessárias..." "$CYAN"
pip install --upgrade pip
pip install dash dash-bootstrap-components pandas plotly
type_effect "Bibliotecas instaladas com sucesso." "$GREEN"
echo

# Navegar até o diretório correto
type_effect "Navegando até o diretório do projeto..." "$CYAN"
DASHBOARD_PATH="src/Dashboard COVID-19/Dashboard COVID-19"
if cd "$DASHBOARD_PATH" 2>/dev/null; then
    type_effect "Diretório encontrado com sucesso." "$GREEN"
else
    type_effect "Erro: diretório '$DASHBOARD_PATH' não encontrado. Verifique a estrutura do projeto." "$RED"
    exit 1
fi
echo

# Exibir informações sobre a COVID-19 no Brasil
type_effect "Carregando informações atualizadas sobre a COVID-19 no Brasil..." "$YELLOW"
sleep 2
type_effect "Desde o início de 2025, o Brasil registrou mais de 130.000 casos de COVID-19 e 664 mortes. Embora os números sejam menores em comparação com anos anteriores, ainda é essencial manter as medidas de prevenção e vacinação em dia. Fonte: Ministério da Saúde." "$CYAN" 0.02
echo

# Executar o dashboard
type_effect "Iniciando o servidor do dashboard..." "$YELLOW"
if python dashboard.py & then
    sleep 5
    type_effect "Abrindo o dashboard no navegador padrão..." "$YELLOW"
    xdg-open http://127.0.0.1:8050/ 2>/dev/null || open http://127.0.0.1:8050/ 2>/dev/null || start http://127.0.0.1:8050/
    echo
    type_effect "Instalação e execução concluídas com sucesso." "$GREEN"
    type_effect "Acesse o Dashboard COVID-19 em: http://127.0.0.1:8050/" "$CYAN"
else
    type_effect "Erro ao iniciar o dashboard. Verifique se o arquivo 'dashboard.py' está presente no diretório." "$RED"
    exit 1
fi
