import data
import sender_stand_request

# Funcion que me permite generar el nombre de un kit
def def_name_kit_body(name):
    name_body = data.kit_body.copy()
    name_body["name"] = name
    return name_body

# Funcion para las pruebas positivas de los test
def positive_assert(name):
    user_response = sender_stand_request.post_new_user(data.user_body)
    token = user_response.json()["authToken"] #extraccion token de la creacion de un usuario
    # Nombre del cuerpo del kit
    kit_body = def_name_kit_body(name)
    kit_response = sender_stand_request.post_created_kit(kit_body, token)
    # Verificacion de la respuesta
    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == name

# Funcion para las pruebas negativas de los test que contengan mal el nombre
def negative_assert_code_400_badname(name):
    user_response = sender_stand_request.post_new_user(data.user_body)
    token = user_response.json()["authToken"] #extraccion token de la creacion de un usuario
    # Nombre del cuerpo del kit
    kit_body = def_name_kit_body(name)
    kit_response = sender_stand_request.post_created_kit(kit_body, token)
    # Verificacion de la respuesta
    assert kit_response.status_code == 400

#Pruebas
# Prueba 1: El número permitido de caracteres (1)
def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert("a") #approved

# Prueba 2: El número permitido de caracteres (511)
def test_create_kit_511_letter_in_name_get_success_response():
    positive_assert(data.kit_body_511) #approved

# Prueba 3: El número de caracteres es menor que la cantidad permitida (0)
def test_create_kit_empty_name_get_error_response():
    negative_assert_code_400_badname("") #Failed error 201

# Prueba 4: El número de caracteres es mayor que la cantidad permitida (512)
def test_create_kit_512_letter_in_name_get_error_response():
    negative_assert_code_400_badname(data.kit_body_512) #Failed error 201

# Prueba 5: Se permiten caracteres especiales
def test_create_kit_special_symbol_in_name_get_success_response():
    positive_assert("№%@") #approved

# Prueba 6: Se permiten espacios
def test_create_kit_has_spaces_in_name_get_success_response():
    positive_assert(" A Aaa ") #approved

# Prueba 7: Se permiten números
def test_create_kit_has_number_in_name_get_success_response():
    positive_assert("123") #approved

# Prueba 8: El parámetro 'name' no se pasa en la solicitud
def test_create_kit_no_name_get_error_response():
    user_response = sender_stand_request.post_new_user(data.user_body)
    token = user_response.json()["authToken"]
    kit_body = {"name": None}
    response = sender_stand_request.post_created_kit(kit_body, token)
    assert response.status_code == 400 #Failed error 500

# Prueba 9: Se ha pasado un tipo de parámetro diferente (número en lugar de string)
def test_create_kit_number_type_name_get_error_response():
    negative_assert_code_400_badname(123) #Failed error 201