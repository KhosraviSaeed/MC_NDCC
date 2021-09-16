function n_each_c = sample_spliter(n_samples, n_classes, n_centers)
    %{

        *** This function generates the number of samples belongs 
        to each class

        *** Centers approximately have n_centers/n_classes samples with a small variance 
 
    %} 
    count = 0;
    n_cen_fe_cls = int32(floor(n_centers/n_classes));
    n_each_c = zeros(n_classes, n_cen_fe_cls);
    while n_samples > count
        r = randi(n_classes);
        r2 = randi(n_cen_fe_cls);
        n_each_c(r, r2) = n_each_c(r, r2) + 1;
        count = count + 1;
    end
end