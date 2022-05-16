def order_create(request):  # When user clicks on create order this fuciton will trigger
    form = OrderItemForm()  # first render empty form || return render(request, 'order_create.html', context) || this code will take the form variable from here and it will render the empty form
    # when user clicks the submit button after filling the order details this line will get execute, if this IF condition stisfies we will enter in to the loop.
    if request.method == 'POST':
        # This line of code will get all the data and files that are added in the form by user.
        form = OrderItemForm(request.POST, request.FILES)
        # Now the request is containing all the data that is entered by the user, out of that data we need only category. this line of code will bring what is the category that user selected.
        get_category = request.POST.get('category_name')
        get_product = request.POST.get('product_name')
        # if the data entered in the form by user is a valid data, then enter in to the loop.
        if form.is_valid():
            # From the existing orders we have to filter the orders which are incomplete and the category that user selected. this is being done just to get the chef's who are still working on the pirticular category, so that we can assign this order to the chef who is still preparing that category order.
            geting_prepared = OrderItem.objects.filter(
                status='incomplete', product_name=get_product)
            #print('+++++++++++++',geting_prepared)
            chef_dict = {}  # define an empty dict, this dict will have the {chef:orders_completed}
            # if you get the list of chefs who are working on the same category, then enter in to the loop.
            if geting_prepared:
                # breakpoint()
                # iterate over the list of chefs(Querysets).
                for i in geting_prepared:
                    # get the chef names who are preparing the incomplete orders.
                    chef_name_q = i.prepared_by
                    if chef_name_q== None:
                        get_chef = Chef.objects.filter(category_name=get_category).first()
                       
                        obj = form.save(commit=False)
                        obj.prepared_by = get_chef
                        obj.save()
                    # print('----------------------',chef_name_q)
                    # out of chefs who are preparing the incomplete orders, get their completed_orders number.
                    else:
                        get_chef = Chef.objects.filter(chef_name=chef_name_q).values_list(
                            'orders_completed', flat=True)
                        for i in get_chef:  # get the filtered list of chefs orders that are completed
                            # create a dict || dict['sravan'] = 2, dict['ravan'] = 3, chef_dict[sushanth]:1
                            chef_dict[chef_name_q] = i
                    # print('DICT',chef_dict)
                    # Get the chefs orders who had prepared the less orders in a day.#get the key where the value is minimum#https://www.codegrepper.com/code-examples/python/how+to+find+the+minimum+value+in+a+dictionary+python
                            chef_final = min(chef_dict, key=chef_dict.get)
                            get_chef = Chef.objects.get(chef_name=chef_final)
                            obj = form.save(commit=False)
                            obj.prepared_by = get_chef
                            obj.save()
            else:  # if the chef's are idle and not preparing any orders in line. all the existing orders are completed, if new order is comming up then assign the order to any available chef.                breakpoint()
                #print('+++++++++++ELSE+++++++')
                #breakpoint()
                geting_prepared = OrderItem.objects.filter(status='incomplete', category_name=get_category,)
                list_chefs = []
                final_list = []
                for i in geting_prepared:
                    list_chefs.append(i.prepared_by)
                #print(list_chefs)
                for i in list_chefs:
                    final_list.append(i.chef_name)
                #chef_cat = Category.objects.get(category_name = get_category)
                #print(chef_cat)
                get_chef = Chef.objects.filter(category_name=get_category).exclude(chef_name__in = final_list).first()


                if get_chef is None:
                    carteg_filt = Chef.objects.filter(category_name=get_category)
                    #print(carteg_filt, '!!!!!!!!!!!!!!!!!!')
                    for i in carteg_filt:
                        chef_dict[i.chef_name] = i.orders_completed
                        #print(chef_dict,'@@@@@@@@@@@@@@@@')
                chef_final = min(chef_dict, key=chef_dict.get)
                print(chef_final, '1111111111111111')

                if get_chef is None:
                    carteg_filt = Chef.objects.filter(category_name=get_category)
                    for i in carteg_filt:
                        chef_dict[i.chef_name] = i.orders_completed
                chef_final = min(chef_dict, key=chef_dict.get)

                get_chef = Chef.objects.get(chef_name=chef_final)
                obj = form.save(commit=False)  # instace: hold before you save.
                # before you save the customer order in database, assign a chef who is idle.
                obj.prepared_by = get_chef
                obj.save()  # save to DB

        return redirect('order_view')
    context = {'form': form}
    return render(request, 'order_create.html', context)
