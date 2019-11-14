# mv "/Users/agataforyciarz/Downloads/ImageNet\ -\ Total\ Data.csv" imagenet_table.csv
import pandas as pd
df = pd.read_csv("imagenet_table.csv", header=0, sep=",")
df = df.iloc[:,:8]

df = df.sort_values(by=["date"], ascending=False).reset_index()
df[["Rank", "Top 1 Accuracy", "date"]]

acc = 0
keep_indices = set()
acc_list = []
for i in reversed(range(df.shape[0])):
 	new_acc = float(df.loc[i,"Top 1 Accuracy"].split('%')[0])
 	if float(new_acc) > acc:
	 	keep_indices.add(i)
	 	acc_list.append(new_acc)
	 	acc = new_acc
	 	idx = i

top_df = df.iloc[list(keep_indices)].sort_values(by="date", ascending=False)
del top_df["index"]
top_df[["Rank", "Top 1 Accuracy", "date"]]


top_df.to_csv("top_results_at_time_t.csv", index=False)

top_df.date = top_df.date.astype(str)
top_df["Top 1 Accuracy"] = top_df["Top 1 Accuracy"].apply(lambda x: x.split("%")[0])
dates_dict = dict(zip(top_df.date, top_df["Top 1 Accuracy"]))

extra_label_dates = top_df[~top_df["Extra Training Data Label"].isna()].date.values

dates = pd.Series(pd.date_range(start="2012-12-01", end="2020-11-03", freq=None)).astype(str)
top1 = [dates_dict[el] if (el in dates_dict.keys() and el not in extra_label_dates) else None for el in dates]
extra_data_top1 = [dates_dict[el] if el in extra_label_dates else None for el in dates]

df1 = pd.DataFrame({"date": dates, "No extra training data": top1, "Extra training data": extra_data_top1})
df1 = df1[["date", 'No extra training data', 'Extra training data']]
df1.to_csv("accuracy_to_plot.csv", index=False)
