```
 _______                             _________                                    
 \      \   ____  __ _________  ____ \_   ___ \  ___________  ____   ____ _____   
 /   |   \_/ __ \|  |  \_  __ \/  _ \/    \  \/ /  _ \_  __ \/  _ \ /    \\__  \  
/    |    \  ___/|  |  /|  | \(  <_> )     \___(  <_> )  | \(  <_> )   |  \/ __ \_
\____|__  /\___  >____/ |__|   \____/ \______  /\____/|__|   \____/|___|  (____  /
        \/     \/                            \/                         \/     \/ 
```

---
Este projeto tem como objetivo oferecer uma ferramenta interativa para visualização e análise de dados da COVID-19 no Brasil. Construído em Python com as bibliotecas Dash, Plotly e Pandas, o **NeuroCorona** utiliza dados oficiais do Ministério da Saúde para apresentar informações confiáveis sobre casos, óbitos e tendências epidemiológicas. A visualização facilita a interpretação pública e técnica, sendo ideal para pesquisadores, estudantes e cidadãos interessados.

---

## 📚 Índice

1. [Introdução](#1-introdução)  
2. [Objetivos](#2-objetivos)  
3. [Arquitetura do Projeto](#3-arquitetura-do-projeto)  
4. [Tecnologias Utilizadas](#4-tecnologias-utilizadas)  
5. [Instalação e Execução](#5-instalação-e-execução)  
6. [Funcionalidades do Dashboard](#6-funcionalidades-do-dashboard)  
7. [Fonte de Dados](#7-fonte-de-dados)  
8. [Resultados Esperados](#8-resultados-esperados)  
9. [Considerações Finais](#9-considerações-finais)  
10. [Referências](#10-referências)  

---

## 1. Introdução

Desde o início da pandemia de COVID-19, tornou-se evidente a importância da visualização de dados como ferramenta de monitoramento e conscientização. O **NeuroCorona** surgiu como um projeto educacional e científico para apresentar os dados da pandemia no Brasil de forma clara, acessível e interativa.

---

## 2. Objetivos

### Objetivo Geral

- Criar um dashboard dinâmico e informativo sobre a pandemia da COVID-19 no Brasil.

### Objetivos Específicos

- Permitir a análise temporal dos dados por estado e por data.
- Utilizar dados oficiais e confiáveis.
- Facilitar o acesso à informação para o público geral e comunidade científica.
- Automatizar todo o processo de instalação e execução do dashboard.

---

## 3. Arquitetura do Projeto

```
NeuroCorona/
├── Configs/                  # Ambiente virtual Python
├── src/
│   └── Dashboard COVID-19/
│       ├── dashboard.py      # Script principal do dashboard
│       ├── df_brasil.csv     # Dados nacionais
│       ├── df_states.csv     # Dados por estado
│       ├── geojson/          # Arquivos geográficos
│       └── assets/           # Estilo do dashboard
├── config.sh                 # Script de configuração, instalações e execução 
└── README.md                 # Documentação do projeto
```

---

## 4. Tecnologias Utilizadas

- **Python 3.11+**
- **Dash** (`dash`, `dash-bootstrap-components`)
- **Plotly**
- **Pandas**
- **JSON & GeoJSON**

O script `config.sh` automatiza a instalação de dependências, criação de ambiente virtual e execução do projeto.

---

## 5. Instalação e Execução

### Pré-requisitos

- Linux (Debian, Fedora, Arch ou derivados)
- Python 3.11+
- Acesso a terminal com `bash` e `sudo`

### Instruções

```bash
# Clone o repositório
git clone https://github.com/sh1ftx/NeuroCorona.git
cd NeuroCorona

# Dar permissão e executar o script de instalação
chmod +x config.sh
./config.sh
```

O script detecta seu sistema, instala o Python se necessário, configura o ambiente virtual e executa o dashboard.

---

## 6. Funcionalidades do Dashboard

- Exibição dos **casos confirmados e óbitos** por estado e por data.
- Visualização por **mapa interativo (geojson)**.
- Gráficos de linha e barras interativos.
- Interface responsiva e com **visual moderno**.
- Atualização contínua com os dados mais recentes do Ministério da Saúde.

---

## 7. Fonte de Dados

Os dados utilizados no projeto são públicos e obtidos do **Portal de Dados Oficiais da COVID-19 no Brasil**, mantido pelo Ministério da Saúde:

🔗 [https://covid.saude.gov.br/](https://covid.saude.gov.br/)

Os arquivos CSV são pré-processados e armazenados localmente para melhor desempenho.

---

## 8. Resultados Esperados

O projeto busca:

- Democratizar o acesso à informação confiável sobre a COVID-19.
- Auxiliar pesquisadores e estudantes no entendimento dos impactos regionais da pandemia.
- Estimular o uso de dados abertos em projetos educacionais e sociais.

---

## 9. Considerações Finais

O **NeuroCorona** é um projeto open-source em desenvolvimento contínuo. Futuras atualizações incluirão:

- Integração com banco de dados.
- Filtros por faixa etária e sexo.
- Comparativo internacional.
- Exportação de gráficos e relatórios PDF.

Contribuições são bem-vindas!

---

## 10. Referências

- Ministério da Saúde. **Painel Coronavírus – Brasil**. Disponível em:  
  [https://covid.saude.gov.br](https://covid.saude.gov.br). Acesso em: abril de 2025.

- GitHub – Projeto NeuroCorona:  
  [https://github.com/sh1ftx/NeuroCorona.git](https://github.com/sh1ftx/NeuroCorona.git)

- Plotly Dash: [https://dash.plotly.com](https://dash.plotly.com)

- Pandas Documentation: [https://pandas.pydata.org/docs](https://pandas.pydata.org/docs)

---

> Desenvolvido com 💡 por [Kayki Ivan (sh1ft)](https://github.com/sh1ftx)
