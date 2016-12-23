import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
import ckanext.aridhia.helpers as _helpers
import logging


log = logging.getLogger(__name__)


class AridhiaPlugin(plugins.SingletonPlugin, toolkit.DefaultDatasetForm):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IPackageController, inherit=True)
    plugins.implements(plugins.IResourceController, inherit=True)
    plugins.implements(plugins.IDatasetForm, inherit=True)
    plugins.implements(plugins.ITemplateHelpers)
    plugins.implements(plugins.IRoutes)
    
    # IPackageController
    
    def after_show(self, context, pkg_dict):
        
        pkg_dict.update({'identifier': pkg_dict.get('id')})
        return pkg_dict
        
    def before_view(self, pkg_dict):
        
        pkg_dict.update({'identifier': pkg_dict.get('id')})
        return pkg_dict

    # IRoutes

    def before_map(self, map):
        map.redirect('/user/register', 'https://portal.rsrch.nl/',
                     _redirect_code='301 Moved Permanently')
        map.redirect('/user/reset', 'https://portal.rsrch.nl/',
                     _redirect_code='301 Moved Permanently')
        return map

    def after_map(self, map):
        return map

    # IDatasetForm
    
    def create_package_schema(self):
        schema = super(AridhiaPlugin, self).create_package_schema()
        defaults = [toolkit.get_validator('ignore_missing'),
                    toolkit.get_converter('convert_to_extras')]
        
        schema.update({
            'restricted': defaults,
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
            'restricted': defaults,
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
            'restricted': defaults,
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
        
    def get_helpers(self):
        return {
            'language_options':
                _helpers.language_options,
            'get_language_by_code':
                _helpers.get_language_by_code,
            'get_package_version':
                _helpers.get_package_version
        }


    def before_search(self, search_params):
        fq = search_params.get("fq", "")
        if not toolkit.c.user:
            # There is no user logged in, hide the restricted datasets
            fq = fq + " -extras_restricted:1"
        search_params["fq"] = fq
        return search_params

    def before_view(self, package):
        if not toolkit.c.user and package.get("restricted", 0) == "1":
            raise toolkit.NotAuthorized
        return package
