from App_03__Category import models


def category_list():

    """

        return category list

    """

    sub_category_list = models.CategorySubRoot.objects.filter(visualize_status=True)

    category_data = {}
    for dt in sub_category_list:

        # get category root name
        category_name = dt.category_root.title

        # append category sub root to category list
        if category_name in category_data.keys():
            category_data[category_name].append(dt.title)
        else:
            category_data[category_name] = [dt.title]

    return {'category_list': category_data}

