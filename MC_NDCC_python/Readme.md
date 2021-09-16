# Multi-Class Normal Distribution Cubic Clusters Dataset Generator
**NORMALLY DISTRIBUTED CUBIC CLUSTERS** is a data generator. 
It generates a series of random centers for multivariate
normal distributions. NDC randomly generates a fraction
of data for each center, i.e. what fraction of data points
will come from this center. NDC randomly generates a 
separating plane. Based on this plane, classes for are 
chosen for each center. NDC then randomly generates the 
points from the distributions. NDC can increase 
inseparability by increasing variances of distributions.
A measure of "true" separability is obtained by looking 
at how many points end up on the wrong side of the 
separating plane. All values are taken as integers 
for simplicity.



### Python: How to use it
<hr>
1. Put `MC_NDCC.py` file in a directory you want to make the dataset
2. Make a `Test.py` file in the directory and drop the code below in it

```python
Import MC_NDCC

# Initialize an instance 
ndcc = MC_NDCC.MC_NDCC()
# Get the dataset as a Numpy matrix
ds_mat  = ndcc.get_matrix()
# Save the dataset as a csv file
ndcc.get_csv('file_name.csv')
```
3. Run `Test.py`

### Matlab: How to use it
<hr>
1. Run `NDCC.m` file.  
2. Get the generated dataset as a file `dataset.csv` in the current directory

