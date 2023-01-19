from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self, db_data):
        self.id = db_data['id']
        self.first_name = db_data['first_name']
        self.last_name = db_data['last_name']
        self.age = db_data['age']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']

    @classmethod
    def save_ninja(cls, data):
        query = "INSERT INTO ninjas (dojo_id, first_name, last_name, age) VALUES (%(dojo_id)s, %(fn)s, %(ln)s, %(age)s);"
        # not sure if i have to specify created and updated at here if it's automatically functioned to now() in mysql
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
    
    @classmethod
    def get_one_ninja(cls, data):
        query = "SELECT * FROM ninjas WHERE id = %(id)s;"
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        return result[0]
    
    @classmethod
    def process_update(cls, data):
        query = "UPDATE ninjas SET dojo_id = %(dojo_id)s, first_name = %(fn)s, last_name = %(ln)s, age = %(age)s, updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

    @classmethod
    def delete_ninja(cls,data):
        query = "DELETE FROM ninjas WHERE id = %(id)s;"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

    # @classmethod
    # def get_dojo_of_ninja(cls,data):
    #     query = "SELECT name FROM dojos WHERE id = %(dojo_id)s;"
    #     name = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
    #     print(name)
    #     return name