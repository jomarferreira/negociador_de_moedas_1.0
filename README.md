# 💱 Currency Consultant (Negociador de Moedas)
Application developed in Python for consulting international currencies, using web scraping to collect real data from external sources.

## 🇧🇷 Versão em Português
Aplicação desenvolvida em Python para consulta de moedas internacionais, utilizando web scraping para coleta de dados do site IBAN.

## 🚀 Features
- Web scraping of currency data from IBAN website  
- Data processing and organization using lists and dictionaries  
- Interactive terminal interface for user input  
- Input validation and error handling  

## 🛠️ Technologies Used
- Python 3  
- Requests  
- BeautifulSoup  

## 📊 How It Works
1. The application sends a request to the IBAN website  
2. Extracts currency data using web scraping  
3. Organizes the data into structured format  
4. Displays a list of countries for the user  
5. User selects an option and receives the currency code  

## ▶️ How to Run
```bash
git clone https://github.com/joeywheelersam/negociador_de_moedas_1.0.git
cd negociador_de_moedas_1.0
pip install requests beautifulsoup4
python main.py
