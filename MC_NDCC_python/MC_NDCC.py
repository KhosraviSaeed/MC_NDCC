# TITLE: Multi-Class Normal Distribution Cubic Clusters Dataset Generator
# AUTHOR: Dr. Hossein Moosaei, Saeed Khosravi
# Date: 10/09/2020

# NORMALLY DISTRIBUTED CLUSTERS is a data generator. 
# It generates a series of random centers for multivariate
#normal distributions. NDC randomly generates a fraction
# of data for each center, i.e. what fraction of data points
# will come from this center. NDC randomly generates a 
# separating plane. Based on this plane, classes for are 
# chosen for each center. NDC then randomly generates the 
# points from the distributions. NDC can increase 
# inseparability by increasng variances of distributions.
# A measure of "true" separability is obtained by looking 
# at how many points end up on the wrong side of the 
# separating plane. All values are taken as integers 
# for simplicity.

import numpy as np
import pandas as pd
class MC_NDCC:
    
    def __init__(self):
        self.n_samples  = int(input("Enter number of samples: \n"))
        self.n_features = int(input("Enter number of features: \n"))
        self.n_classes  = int(input("Enter number of classes: \n"))
        
        self.centers_list    = [100, 300, 500]
        self.center_points   = self.centers_matrix(self.centers_list, self.n_features)
        self.n_centers       = 2*len(self.centers_list)*self.n_features
        self.class_locations = self.class_center_locations(self.n_classes, self.n_centers)
        self.ss = self.sample_spliter(self.n_samples, self.n_classes, self.n_centers)
        r, c    = self.class_locations.shape
        self.M  = np.zeros((0, self.n_features))
        self.l  = np.zeros((0, 1))
        for i in range(r):
            for j in range(c):
                self.temp = np.random.normal(loc = self.center_points[int(self.class_locations[i, j])],size = (int(self.ss[i,j]), self.n_features),scale = 5)
                self.label_temp = np.ones((int(self.ss[i,j]), 1))*(i+1)
                self.l = np.concatenate((self.l, self.label_temp), axis = 0)
                self.M = np.concatenate((self.M, self.temp) , axis = 0)
        self.M = np.concatenate((self.M, self.l), axis = 1).astype('int32')
        np.random.shuffle(self.M)
    def sample_spliter(self, n_samples, n_classes, n_centers):
        # This function generates the number of samples belongs to each class
        # Centers approximately have n_centers/n_classes samples with a small variance 
        count = 0
        n_cen_fe_cls = int(np.floor(n_centers/n_classes))
        n_each_c = np.zeros((n_classes, n_cen_fe_cls))
        while(n_samples > count):
            r = np.random.randint(n_classes)
            r2 = np.random.randint(n_cen_fe_cls)
            n_each_c[r, r2] += 1
            count += 1
        return n_each_c

    def class_center_locations(self, n_classes, n_centers):
        
        # This function specifies which center 
        # points belong to which classes
    
        # It returns a matrix in size of n_classess by 
        # n_centers_for_each_class that means a row for each class
        
        rng = np.random.default_rng()
        # Generate list of random non-repeatative numbers from 1 to n_center
        locs = rng.choice(n_centers, n_centers, replace=False)
        # number of centers for each class
        n_cen_fe_cls = int(np.floor(n_centers/n_classes))
        cls_locs = np.zeros((n_classes,n_cen_fe_cls))
        k = 0
        for i in range(n_classes):
            for j in range(n_cen_fe_cls):
                cls_locs[i,j] = locs[k]
                k += 1 
        return cls_locs

    def centers_matrix(self, centers_list, n_features):
        # This function returns the matrix of center locations 
        # based on centers_list in n_features space
        n_centers = 2*len(centers_list)*n_features
        centers_matrix = np.zeros((n_centers, n_features))
        for i in range(len(centers_list)):
            for j in range(n_features):
                centers_matrix[i*2*n_features + 2*j  , j] =  centers_list[i]
                centers_matrix[i*2*n_features + 2*j+1, j] = -centers_list[i]
        return centers_matrix
    
        
    def get_matrix(self):
        # Get the dataset as a numpy matrix
        return self.M
    
    def get_csv(self, filename):
        # Save the dataset as csv file
        df = pd.DataFrame(self.M)
        df.to_csv(filename, header = False, index = False)
        print(f'Dataset saved as {filename} in current directory. ')
