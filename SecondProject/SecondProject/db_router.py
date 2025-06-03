class BlogDBRouter:
    app_names = ['blog']
    models_to_route = ['Post', 'Category']

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.app_names and model.__name__ in self.models_to_route:
            return 'blog_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.app_names and model.__name__ in self.models_to_route:
            return 'blog_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        db_set = {'blog_db', 'default'}
        if obj1._state.db in db_set and obj2._state.db in db_set:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.app_names and model_name in [model.lower() for model in self.models_to_route]:
            return db == 'blog_db'
        return db == 'default'
