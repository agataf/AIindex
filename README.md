# AIindex

Structure of the repo:

`imagenet_table.csv` is the dataset copied manually from the Papers with Code [ImageNet Classification section](https://paperswithcode.com/sota/image-classification-on-imagenet).

`generate_frames.py` is a script which takes in the `imagenet_table` and generates the following files:
- `top_results_at_time_t.csv`: a file containing a subset of `imagenet_table.csv`, containing only the results that were the state of the art (on 1% accuracy) at the _time they were published_. I copied its results to the [Top Results at Time t](https://docs.google.com/spreadsheets/d/14_2OYPJ2DASIAXYEj9YUTyBlUWQVrJaLJ_bvvx2hWZU/) sheet in the Drive.
- `imagenet_table.csv`: a file containing three columns:
  - date: all dates from earliest one present in `imagenet_table.csv` to 2019-11-25
  - No extra training data: a result from `top_results_at_time_t.csv` published on that date on empty
  - Extra training data: a result from `top_results_at_time_t.csv` published on that date on empty
  
  I copied its results to the [Accuracy to Plot](https://docs.google.com/spreadsheets/d/14_2OYPJ2DASIAXYEj9YUTyBlUWQVrJaLJ_bvvx2hWZU/) sheet in the Drive.

-------------

## CIFAR-100 Image Classification [link](https://docs.google.com/spreadsheets/d/1SKlcJIwTkHf3lJyvhf-hXrq4KsfIbyKQYFWg3b-AunE/edit#gid=667587078)
1. Double check [current results](https://paperswithcode.com/sota/image-classification-on-cifar-100) on Papers with Code 
2. Download sheet "Data with Paper Links" as csv
3. Run `generate_frames.py`
4. Upload/copy `top_results_at_time_t_CIFAR.csv` to [CIFAR-100 - Top results at time t](https://docs.google.com/spreadsheets/d/1SKlcJIwTkHf3lJyvhf-hXrq4KsfIbyKQYFWg3b-AunE/edit#gid=1013954913) sheet on drive
5. Upload/copy `accuracy_to_plot_CIFAR.csv` to [CIFAR-100 - Percentage Correct data](https://docs.google.com/spreadsheets/d/1SKlcJIwTkHf3lJyvhf-hXrq4KsfIbyKQYFWg3b-AunE/edit#gid=1414781210) sheet on drive
--> [CIFAR-100 - Top results at time t + details](https://docs.google.com/spreadsheets/d/1SKlcJIwTkHf3lJyvhf-hXrq4KsfIbyKQYFWg3b-AunE/edit#gid=830827910) automatically updates
