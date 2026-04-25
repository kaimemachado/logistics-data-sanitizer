Logistics Data Sanitizer | ETL Pipeline

O Problema (Contexto de Negócios)
No setor de logística e e-commerce, arquivos brutos enviados por fornecedores frequentemente chegam com dados não padronizados (SKUs em formatos inconsistentes) e ausência de informações vitais, como o preço final de venda. O processamento manual dessas planilhas consome horas de analistas, atrasa a entrada de produtos no catálogo e gera um alto risco de erros de precificação por falha humana.

A Solução
Para eliminar o trabalho manual e garantir segurança na operação, desenvolvi um Pipeline de ETL (Extract, Transform, Load) automatizado. O sistema atua como um saneador de dados que:

Extract: Faz a ingestão massiva de dados brutos via arquivos .csv.

Transform: Padroniza as chaves de identificação (SKUs para UPPERCASE) e aplica regras de negócio dinâmicas (cálculo de 30% de margem de lucro convertendo strings para floats).

Load: Exporta um novo dataset limpo, validado e estruturado, pronto para ser consumido pelo banco de dados da empresa ou ERP.

Tecnologias Utilizadas
Linguagem: Python 3

Bibliotecas: csv (Manipulação nativa para ganho de performance sem dependências externas)

Conceitos Aplicados: Estruturas de Dados (Listas de Dicionários), Loops de processamento em lote, Manipulação de File System (mode='r' e mode='w').

Como Executar o Projeto
Clone este repositório.

Certifique-se de ter o Python 3 instalado.

Coloque o seu arquivo de dados brutos na mesma pasta do script com o nome product_catalog.csv.

Rode o script principal:

Bash
python main.py
O sistema gerará automaticamente um arquivo priced_inventory.csv com os dados sanitizados e prontos para uso.

------------------------------------------------------------------------------------------------------------------

Logistics Data Sanitizer | ETL Pipeline

The Problem (Business Context)
In the logistics and e-commerce sector, raw files sent by suppliers often arrive with unstandardized data (SKUs in inconsistent formats) and a lack of vital information, such as the final selling price. Manual processing of these spreadsheets consumes hours of analysts' time, delays the entry of products into the catalog, and generates a high risk of pricing errors due to human error.

The Solution
To eliminate manual work and ensure operational accuracy, I developed an automated ETL (Extract, Transform, Load) Pipeline. The system acts as a data sanitizer that:

Extract: Performs massive ingestion of raw data via .csv files.

Transform: Standardizes identification keys (SKUs to UPPERCASE) and applies dynamic business rules (calculating a 30% profit margin by converting strings to floats).

Load: Exports a new clean, validated, and structured dataset, ready to be consumed by the company's database or ERP.

Technologies Used

Language: Python 3

Libraries: csv (Native manipulation for performance gains without external dependencies)

Concepts Applied: Data Structures (Lists of Dictionaries), Batch processing loops, File System Manipulation (mode='r' and mode='w').

How to Run the Project

Clone this repository.

Make sure you have Python 3 installed.

Place your raw data file in the same folder as the script, named product_catalog.csv.

Run the main script:

Bash
python main.py
The system will automatically generate a priced_inventory.csv file with the sanitized data, ready for use.