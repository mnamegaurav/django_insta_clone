JAZZMIN_SETTINGS = {
    'show_ui_builder': True
}
# JAZZMIN_SETTINGS = {
#     # title of the window (Will default to current_admin_site.site_title if absent or None)
#     "site_title": "Insta Clone",

#     # Title on the brand, and login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
#     "site_header": "Insta Clone",

#     # square logo to use for your site, must be present in static files, used for favicon and brand on top left
#     "site_logo": "books/img/logo.png",

#     # Welcome text on the login screen
#     "welcome_sign": "Welcome to the library",

#     # Copyright on the footer
#     "copyright": "Acme Library Ltd",

#     # The model admin to search from the search bar, search bar omitted if excluded
#     "search_model": "auth.User",

#     # Field name on user model that contains avatar image
#     "user_avatar": None,

#     ############
#     # Top Menu #
#     ############

#     # Links to put along the top menu
#     "topmenu_links": [

#         # Url that gets reversed (Permissions can be added)
#         {"name": "Home",  "url": "admin:index", "permissions": ["auth.view_user"]},

#         # external url that opens in a new window (Permissions can be added)
#         {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},

#         # model admin to link to (Permissions checked against model)
#         {"model": "auth.User"},

#         # App with dropdown menu to all its models pages (Permissions checked against models)
#         {"app": "books"},
#     ],

#     #############
#     # User Menu #
#     #############

#     # Additional links to include in the user menu on the top right ("app" url type is not allowed)
#     "usermenu_links": [
#         {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
#         {"model": "auth.user"}
#     ],

#     #############
#     # Side Menu #
#     #############

#     # Whether to display the side menu
#     "show_sidebar": True,

#     # Whether to aut expand the menu
#     "navigation_expanded": True,

#     # Hide these apps when generating side menu e.g (auth)
#     "hide_apps": [],

#     # Hide these models when generating side menu (e.g auth.user)
#     "hide_models": [],

#     # List of apps (and/or models) to base side menu ordering off of (does not need to contain all apps/models)
#     "order_with_respect_to": ["auth", "books", "books.author", "books.book"],

#     # Custom links to append to app groups, keyed on app name
#     "custom_links": {
#         "books": [{
#             "name": "Make Messages", 
#             "url": "make_messages", 
#             "icon": "fas fa-comments",
#             "permissions": ["books.view_book"]
#         }]
#     },
#     # Icons that are used when one is not manually specified
#     "default_icon_parents": "fas fa-chevron-circle-right",
#     "default_icon_children": "fas fa-circle",

#     #################
#     # Related Modal #
#     #################
#     # Use modals instead of popups
#     "related_modal_active": False,

#     #############
#     # UI Tweaks #
#     #############
#     # Relative paths to custom CSS/JS scripts (must be present in static files)
#     "custom_css": None,
#     "custom_js": None,
#     # Whether to show the UI customizer on the sidebar
#     "show_ui_builder": False,

#     ###############
#     # Change view #
#     ###############
#     # Render out the change view as a single form, or in tabs, current options are
#     # - single
#     # - horizontal_tabs (default)
#     # - vertical_tabs
#     # - collapsible
#     # - carousel
#     "changeform_format": "horizontal_tabs",
#     # override change forms on a per modeladmin basis
#     "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs"},
#     # Add a language dropdown into the admin
#     "language_chooser": True,
# }