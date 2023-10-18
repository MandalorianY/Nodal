import time
from collections import Counter
import pandas as pd
import plotly.express as px

def timer_log(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        return end_time - start_time
    return wrapper

@timer_log
def count_words_dict():
    with open(r"data\t8.shakespeare.txt") as f:
        words = f.read().split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

@timer_log
def count_words_counter():
    with open(r"data\t8.shakespeare.txt") as f:
        words = f.read().split()
    return Counter(words)

print("Count word function ",count_words_counter())
print("Count word with a dict",count_words_dict())

# make a function to run this experiment 100 times and plot the two distributions of
# execution times. This allows us to have more robust information (e.g: mean and
# variance) using pandas and plotly.
def experiment():
    dict_times = []
    counter_times = []
    for i in range(100):
        dict_times.append(count_words_dict())
        counter_times.append(count_words_counter())
    return dict_times, counter_times

dict_times, counter_times = experiment()
df = pd.DataFrame(dict_times, columns=["dict"])
df["counter"] = counter_times
df = df.melt(var_name="implementation", value_name="seconds")
fig = px.box(df, x="implementation", y="seconds")
fig.write_html(r'static\counter_chart.html')
