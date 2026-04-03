# 💼 Salary vs Experience Predictor

A Python-based machine learning project that predicts salary based on years of experience using **Simple Linear Regression** — a classic regression problem, great for demonstrating ML fundamentals.

---

## 📌 Overview

This project demonstrates the end-to-end pipeline of a supervised machine learning project:

- Generating and exploring a dataset
- Training a Simple Linear Regression model
- Evaluating model performance
- Deploying an interactive web app using **Streamlit**

---

## 🚀 Features

- 📊 Predict salary based on years of experience
- 📈 Visualize the dataset and the regression line interactively
- 🌐 Simple and clean Streamlit web interface
- 🔁 Modular structure: data generation, training, testing, and deployment are all separate

---

## 🗂️ Project Structure

```
Salary-vs-Experience-Predictor-Using-ML/
│
├── app.py              # Streamlit web application
├── train.py            # Model training script
├── test.py             # Model testing/evaluation script
├── datagenerate.py     # Script to generate synthetic salary data
├── salary_data.csv     # Dataset (Years Experience vs Salary)
├── Model.pkl           # Serialized trained model
└── requirements.txt    # Python dependencies
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core programming language |
| scikit-learn | Machine learning (Linear Regression) |
| pandas | Data manipulation |
| numpy | Numerical operations |
| matplotlib | Data visualization |
| Streamlit | Web app deployment |

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/parth-visualize/Salary-vs-Experience-Predictor-Using-ML.git
cd Salary-vs-Experience-Predictor-Using-ML
```

### 2. Create a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate        # On macOS/Linux
venv\Scripts\activate           # On Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🏃 Usage

### Generate Data (optional — `salary_data.csv` is already included)

```bash
python datagenerate.py
```

### Train the Model

```bash
python train.py
```

This will train the Linear Regression model and save it as `Model.pkl`.

### Test the Model

```bash
python test.py
```

### Run the Web App

```bash
streamlit run app.py
```

Open your browser and go to `http://localhost:8501` to interact with the app.

---

## 🖥️ App Preview

- Enter **years of experience** using the input slider
- The app instantly displays the **predicted salary**
- Toggle the checkbox to view the **dataset scatter plot** overlaid with the **regression line**

---

## 📐 How It Works

1. **Data**: A CSV dataset with two columns — `Years Experience` and `Salary`
2. **Model**: Simple Linear Regression (`y = mx + b`) trained using scikit-learn
3. **Serialization**: The trained model is saved using `pickle` (`Model.pkl`)
4. **App**: Streamlit loads the model and provides a UI for real-time prediction

---

## 📦 Dependencies

```
numpy
pandas
streamlit
matplotlib
scikit-learn
```

Install all at once with:

```bash
pip install -r requirements.txt
```

---

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add your feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👤 Author

**parth-visualize**  
GitHub: [@parth-visualize](https://github.com/parth-visualize)
