function cls_locs = class_center_locations(n_classes, n_centers);
    %{
        
        *** This function specifies which center points belong 
        to which classes
    
        *** It returns a matrix in size of n_classess by
        n_centers_for_each_class that means a row for each class

    %}

    % Generate list of random non-repeatative numbers from 1 to n_center 
    locs = datasample(1:n_centers,n_centers,'Replace',false);
    
    % number of centers for each class
    n_cen_fe_cls = int32(floor(n_centers/n_classes));
    
    cls_locs = zeros(n_classes,n_cen_fe_cls);
    k = 1;
    for i = 1:n_classes
        for j = 1:n_cen_fe_cls
            cls_locs(i,j) = locs(k);
            k = k+1;
        end
    end

end