\# AI-Based Fraud Detection on Blockchain (Algorand)



\## Problem Statement



Campus systems such as voting, attendance tracking, certification, and payments rely on centralized trust.

These systems are vulnerable to fraud, manual verification delays, data tampering, and lack transparency.



\## Proposed Solution



This project introduces a hybrid \*\*AI + Blockchain trust framework\*\* that validates transactions using Machine Learning before committing them to an immutable ledger.



Only verified and safe transactions are written to the Algorand blockchain.



\##  Tech Stack



\- Python  

\- FastAPI (Backend API)  

\- Scikit-learn (Fraud Detection Model)  

\- NumPy  

\- Algorand Python SDK  

\- Algorand TestNet  





\##  System Workflow

User Request

↓

AI Fraud Detection Model

↓

Risk Rule Engine

↓

If SAFE → Send to Algorand Blockchain

If FRAUD → Block Immediately



\## 🧠 Key Features



\- Detects suspicious transaction patterns using Machine Learning  

\- Hard-rule validation for high-risk activities  

\- Prevents fraudulent data from reaching blockchain  

\- Stores only verified actions immutably on Algorand TestNet  

\- Transparent, auditable, and tamper-proof workflow  



\## 📁 Project Structure

AI-Fraud-Detection-Algorand/

│

├── backend/

│ ├── app.py

│ ├── algorand\_tx.py

│ └── algorand\_config.py

│

├── ml/

│ ├── dataset\_generator.py

│ └── train\_model.py

│

├── data/

│ └── transactions.csv

│

├── fraud\_model.pkl

├── requirements.txt

└── README.md



\## ▶️ Run Locally



\### 1)  Clone the Repository

git clone https://github.com/rathorearpita241/AI-Fraud-Detection-Algorand.git



cd AI-Fraud-Detection-Algorand



\### 2)  Create Virtual Environment



python -m venv env





Activate (Windows):env\\Scripts\\activate



If someone is using Mac/Linux:

source env/bin/activate



\### 3) Install Dependencies

pip install -r requirements.txt



\### 4) Run the Backend API

python -m uvicorn backend.app:app --reload



\### 5) Open API Documentation

After running the backend server, open the interactive API documentation at:



http://127.0.0.1:8000/docs



This Swagger UI allows you to test fraud detection and blockchain submission directly from the browser.



\## Testing the System



\### Fraudulent Transaction Example (Blocked)



tx\_amount: 5000

tx\_frequency: 9

account\_age\_days: 2





\### Legitimate Transaction Example (Approved)

tx\_amount: 100

tx\_frequency: 1

account\_age\_days: 200



\##  Blockchain Integration



Approved transactions are submitted to \*\*Algorand TestNet\*\*, ensuring:



\- Tamper-proof records  

\- Transparent verification  

\- Decentralized trust model 



\## Use Cases



\- Secure student voting systems  

\- Attendance verification  

\- Certificate authenticity validation  

\- Transparent fund tracking  

\- Fraud-resistant campus workflows  



\## Future Enhancements



\- Smart contract automation  

\- Real-time fraud dashboards  

\- Integration with university ERP systems  

\- Identity-linked verification (DID)





\##Author



\*\*Arpita Rathore\*\*  

GitHub: https://github.com/rathorearpita241



https://www.linkedin.com/in/arpita-rathore-1a1b9231a/



\## License



This project is developed for academic and research demonstration purposes.



