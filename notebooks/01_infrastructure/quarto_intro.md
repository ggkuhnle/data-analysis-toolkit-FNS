# 📝 What is Quarto?

**Quarto** is an open-source scientific and technical publishing system that allows you to create fully reproducible documents that combine **code, narrative text, and visuals**. It's designed for **researchers, analysts, and data scientists** who need to communicate their findings in a clear, flexible, and transparent way.

---

<details>
<summary><strong>🔍 Why use Quarto?</strong></summary>

#### ✅ **Key Features of Quarto**:

- **Integrates code and text**: You can mix code chunks (e.g., Python, R) with Markdown-formatted narrative.
- **Supports multiple languages**: Python, R, Julia, and Observable JavaScript.
- **Reproducible**: When rendered, Quarto re-runs the code and embeds the updated results in the document.
- **Flexible output formats**: HTML, PDF, MS Word, slides, and even books or websites.
- **Version control-friendly**: Plain text `.qmd` files play well with Git and GitHub.
- **Interactive**: Can be extended with Shiny apps, interactive widgets, or even interactive Python plots via Plotly or Bokeh.

</details>

---

## 📊 What Can You Use Quarto For?

| Use Case | Description |
|----------|-------------|
| **Data Reports** | Generate clean, consistent research reports that combine code, figures, and analysis. |
| **Lab Notebooks** | Create digital, reproducible records of your work—great for MSc projects or collaborations. |
| **Teaching Materials** | Prepare slides, handouts, and web-based tutorials from a single source. |
| **Websites** | Build research or teaching websites with integrated data and results. |
| **Dashboards** | With extensions, you can even build interactive dashboards. |

---

<details>
<summary><strong>💡 Example: Nutrition Study Report</strong></summary>

Imagine you've analysed data on polyphenol intake from the NDNS dataset. Using Quarto, you could:

- Load your dataset with Python
- Run statistical models
- Generate plots and tables
- Write up your interpretation
- Render a beautiful, standalone report in HTML or PDF format  
—all from a single `.qmd` file!

</details>

---

## 💾 How Does It Work?

A Quarto file uses the `.qmd` extension and typically includes:

\`\`\`yaml
---
title: "Example Analysis"
format: html
---

## Results

\`\`\`{python}
import pandas as pd
df = pd.read_csv("data.csv")
df.describe()
\`\`\`
\`\`\`

When you run `quarto render myfile.qmd`, it executes the code and creates a final document with the output embedded. This ensures your analysis and documentation are always in sync.

---

📚 [Quarto Documentation →](https://quarto.org)  
🎓 Great for MSc nutrition, food science, and sensory analysis students who need reliable, readable, and shareable outputs.
