# 🚀 Automação de Formulários com Python, Selenium e Excel  

Este projeto é uma solução de **automação de preenchimento de formulários online** utilizando **Python**, **Selenium** e **OpenPyXL**.  

A aplicação lê os dados de uma planilha Excel (`DadosFormulario.xlsx`) e, de forma automática, preenche e envia um formulário no **SurveyMonkey**.  

---

## 🔧 Tecnologias Utilizadas  
- **Python** – linguagem principal para orquestrar toda a automação  
- **Selenium WebDriver** – automação do navegador para interação com os campos e botões  
- **OpenPyXL** – leitura e manipulação dos dados da planilha Excel  
- **Excel** – armazenamento dos dados de entrada (nome, e-mail, telefone, sexo, descrição)  

---

## ⚙️ Como Funciona  
1. Os dados são organizados em uma planilha, separados por colunas (nome, e-mail, telefone, sexo e sobre).  
2. O script percorre cada linha da planilha, abrindo o formulário no navegador.  
3. Cada campo é preenchido automaticamente com os dados correspondentes.  
4. O formulário é enviado, repetindo o processo para todos os registros da planilha.  
 
