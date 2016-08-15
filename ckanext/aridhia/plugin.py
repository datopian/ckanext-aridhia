import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class AridhiaPlugin(plugins.SingletonPlugin, toolkit.DefaultDatasetForm):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IPackageController, inherit=True)
    plugins.implements(plugins.IDatasetForm, inherit=True)
    
    # IPackageController
    
    def after_show(self, context, pkg_dict):
        
        pkg_dict.update({'identifier': pkg_dict.get('id')})
        return pkg_dict
        
    def before_view(self, pkg_dict):
        
        pkg_dict.update({'identifier': pkg_dict.get('id')})
        return pkg_dict
    

    # IDatasetForm
    
    def create_package_schema(self):
        schema = super(AridhiaPlugin, self).create_package_schema()
        defaults = [toolkit.get_validator('ignore_missing'),
                    toolkit.get_converter('convert_to_extras')]
        
        schema.update({
            'number_of_participants':defaults,
            'human_research':defaults,
            'number_of_records': defaults,
            'spatial_coverage': defaults,
            'language': defaults,
            'tc_start': defaults,
            'tc_end': defaults,
            'logo': defaults
        })
        return schema

    def update_package_schema(self):
        schema = super(AridhiaPlugin, self).update_package_schema()
        defaults = [toolkit.get_validator('ignore_missing'),
                    toolkit.get_converter('convert_to_extras')]
        
        schema.update({
            'number_of_participants':defaults,
            'human_research':defaults,
            'number_of_records': defaults,
            'spatial_coverage': defaults,
            'language': defaults,
            'tc_start': defaults,
            'tc_end': defaults,
            'logo': defaults
        })
        return schema

    def show_package_schema(self):
        
        schema = super(AridhiaPlugin, self).show_package_schema()
        defaults = [toolkit.get_converter('convert_from_extras'),
                    toolkit.get_validator('ignore_missing')]
        
        schema.update({
            'number_of_participants':defaults,
            'human_research':defaults,
            'number_of_records': defaults,
            'spatial_coverage': defaults,
            'language': defaults,
            'tc_start': defaults,
            'tc_end': defaults,
            'logo': defaults
        })
        
        return schema

    def is_fallback(self):
        # Return True to register this plugin as the default handler for
        # package types not handled by any other IDatasetForm plugin.
        return True

    def package_types(self):
        # This plugin doesn't handle any special package types, it just
        # registers itself as the default (above).
        return []

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'aridhia')