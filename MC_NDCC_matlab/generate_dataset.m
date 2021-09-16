function M = generate_dataset(centers_matrix, ss,class_locations, n_features)
    %{
    
        *** This function returns the generated dataset matrix with
        coresponding labels 
        
        *** Samples of each center generated using normal distribution 
        function with mu as the center location and sigma as 5 

        *** Size of the samples are given from sample spliter funtion
        
    %}

    [r, c] = size(class_locations);
    %Intialize the matrix as an empty matrix
    M = zeros(0, n_features);
    l = zeros(0, 1);
    for i = 1:r
        for j = 1:c
            %Generate samples in specific center point(mu) and (sigma = 5,
            %and) in size of ss by n_features
            tmp = normrnd(centers_matrix(int32(class_locations(i,j))), 5,[int32(ss(i,j)), n_features]);
            label_tmp = ones(int32(ss(i,j)), 1)*(i);
         
            l = [l; label_tmp];
            M = [M; tmp];
        end
    end
    M = [M, l];
end