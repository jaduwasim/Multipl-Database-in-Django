class LoanDBRouters():
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'car_loan':
            return 'car_loan'
        elif model._meta.app_label == 'home_loan':
            return 'home_loan'
        
        return 'default'
    
    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'car_loan':
            return 'car_loan'
        elif model._meta.app_label == 'home_loan':
            return 'home_loan'
        
        return 'default'
    
    def allow_relation(self, obj1, obj2, **hints):
        if obj1._state.db == obj2._state.db:
            return True
        return None
    
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'home_loan':
            return db == 'home_loan'
        elif app_label == 'car_loan':
            return db == 'car_loan'
        return db == 'default'