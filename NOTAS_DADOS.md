# Notas sobre qualidade e completude dos dados — SIH-SUS

## Lacunas de publicação identificadas

Durante a validação da extração (Fase 2), identificamos meses sem arquivo
`RD` (AIH Reduzida) disponível no FTP do DataSUS, mesmo solicitando o
período completo. Isso é uma característica conhecida da fonte — atraso
de repasse hospitalar ou correção retroativa — e não um erro do pipeline
de extração.

### Amazonas (AM) — 2019 a 2023

| Ano  | Meses ausentes         |
|------|--------------------------|
| 2019 | nenhum                   |
| 2020 | nenhum                   |
| 2021 | julho, novembro          |
| 2022 | maio, dezembro           |
| 2023 | março                    |

Total: 55 de 60 meses esperados (91,7% de completude).

## Decisão de modelagem

Meses sem dado publicado **não são preenchidos com zero** na camada Gold.
Preencher com zero implicaria afirmar "zero internações naquele mês", o
que é estatisticamente falso — a informação correta é "dado indisponível
na fonte para este período". O dashboard final deve indicar essa ausência
explicitamente (ex: gap no gráfico de série temporal, não um vale a zero).

## Dimensão CNES (capacidade hospitalar)

O CNES é um cadastro (não um histórico de eventos como o SIH), então não
faz sentido extrair todos os 60 meses. Optamos por **um snapshot anual**
(dezembro de cada ano, 2019-2023), capturando mudanças reais na rede
hospitalar ao longo do tempo sem redundância — um padrão equivalente a
uma Slowly Changing Dimension.

Grupo extraído: `ST` (Estabelecimentos). Outros grupos do CNES (leitos,
profissionais, equipamentos, serviços especializados) existem na fonte
mas não fazem parte do escopo deste projeto.