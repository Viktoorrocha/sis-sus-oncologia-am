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

### São Paulo (SP) — 2019 a 2023

Nenhuma lacuna identificada: 60 de 60 meses (100% de completude).

## Decisão de modelagem

Meses sem dado publicado **não são preenchidos com zero** na camada Gold.
Preencher com zero implicaria afirmar "zero internações naquele mês", o
que é estatisticamente falso — a informação correta é "dado indisponível
na fonte para este período". O dashboard final deve indicar essa ausência
explicitamente (ex: gap no gráfico de série temporal, não um vale a zero).

## Metodologia de verificação

Para cada UF/ano extraído, contamos os arquivos `RD*.parquet` recebidos
e comparamos com os 12 meses esperados. Divergências são registradas
nesta tabela conforme a extração nacional avança.