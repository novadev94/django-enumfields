def import_class(components):
    from importlib import import_module
    from django.utils.module_loading import import_string

    if len(components) > 2:
        raise ValueError('Invalid enum options')
    elif len(components) == 1:
        return import_string(components[0])
    else:
        module_path, full_class_name = components
        module = import_module(module_path)
        current_member = module
        for class_name in full_class_name.split('.'):
            current_member = getattr(current_member, class_name)
        return current_member
