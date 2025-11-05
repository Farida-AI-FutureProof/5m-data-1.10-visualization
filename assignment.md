# Assignment

## Brief

Write the Python codes for the following questions.
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

## Instructions

Paste the answer as Python in the answer code section below each question.

### Question 1

Question: How do you create a 2x2 subplot grid in matplotlib and select the first subplot?

Answer:

```python
import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 2)  # 2x2 grid
ax = axes[0, 0]                 # first subplot (top-left)

```

### Question 2

Question: How to plot a line and set the color to red and style to dash in a matplotlib plot?

```python
x = [1, 2, 3, 4]
y = [1, 4, 9, 16]
```

Answer:

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [1, 4, 9, 16]

plt.plot(x, y, color="red", linestyle="--")
plt.show()

```

### Question 3

Question: How to plot a histogram with 30 bins for `data` in matplotlib?

```python
data = np.random.randn(1000)
```

Answer:

```python
import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(1000)

plt.hist(data, bins=30)
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Histogram of data")
plt.show()

```

### Question 4

Question: How can you set the x-axis and y-axis labels in a matplotlib plot?

Answer:

```python
import matplotlib.pyplot as plt

plt.plot([1, 2, 3], [1, 4, 9])
plt.xlabel("X axis label")
plt.ylabel("Y axis label")
plt.title("Example Plot")
plt.show()

```

### Question 5

Question: How do you create a bar plot in seaborn using the `tips` dataset to show the average tip amount per day?

```python
import seaborn as sns
tips = sns.load_dataset('tips')
```

Answer:

```python
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.barplot(data=tips, x="day", y="tip")  # default estimator is mean
plt.xlabel("Day")
plt.ylabel("Average Tip")
plt.title("Average Tip Amount per Day")
plt.show()

```

### Question 6

Question: How to create a box plot for total_bill categorized by day in the `tips` dataset using seaborn?

Answer:

```python
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.boxplot(data=tips, x="day", y="total_bill")
plt.xlabel("Day")
plt.ylabel("Total Bill")
plt.title("Total Bill by Day")
plt.show()

```
Guidance, explanations, and sample code were developed with the assistance of ChatGPT (GPT-5) by OpenAI, used for learning support, concept clarification, and code formatting.

All analysis and visualisation outputs were independently reviewed and verified by me to ensure understanding and correctness.
## Submission

- Submit the URL of the GitHub Repository that contains your work to NTU black board.
- Should you reference the work of your classmate(s) or online resources, give them credit by adding either the name of your classmate or URL.
