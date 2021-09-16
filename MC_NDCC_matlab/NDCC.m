%{
NORMALLY DISTRIBUTED CLUSTERS is a data generator. 
It generates a series of random centers for multivariate
normal distributions. NDC randomly generates a fraction
of data for each center, i.e. what fraction of data points
will come from this center. NDC randomly generates a 
separating plane. Based on this plane, classes for are 
chosen for each center. NDC then randomly generates the 
points from the distributions. NDC can increase 
inseparability by increasng variances of distributions.
A measure of "true" separability is obtained by looking 
at how many points end up on the wrong side of the 
separating plane. All values are taken as integers 
for simplicity.
%}


centers_list = [100, 300, 500];
n_samples  = input('Enter the number of samples:\n');
n_features = input('Enter the number of features:\n');
n_classes  = input('Enter the number of classes:\n');


% Generating center matrix based on centers_list and number of features
centers_matrix = get_centers_mat(centers_list, n_features);
n_centers = 2*length(centers_list)*n_features;

% The same number of randomly chosen centers will dedicate to each class
class_locations = class_center_locations(n_classes, n_centers);

% Deciding randomly that how many samples should be in each class_locations
ss = sample_spliter(n_samples, n_classes, n_centers);

%Generating dataset 
ds = generate_dataset(centers_matrix, ss,class_locations, n_features);

%Saving the dataset as a csv file in current directory
writematrix(ds, 'dataset.csv');
    