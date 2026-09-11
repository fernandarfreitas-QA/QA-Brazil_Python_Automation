import data
import helpers

class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Conectado ao servidor Urban Routes")
        else:
            print("Não foi possível conectar ao Urban Routes. Verifique se o servidor está ligado e ainda em execução.")
    def test_set_route(self):
        # Adicionar em S8
        print("função criada para definir a rota")
        pass

    def test_select_plan(self):
        # Adicionar em S8
        print("função criada para definir a plan")
        pass

    # Adicionar em S8
    def test_fill_phone_number(self):
        # Adicionar em S8
        print("funcao criada para definir a phone number")
        pass

    def test_fill_card(self):
        # Adicionar em S8
        print("funcao criada para definir a card")
        pass

    def test_comment_for_driver(self):
        # Adicionar em S8
        print("funcao criada para definir a comment")
        pass

    def test_order_blanket_and_handkerchiefs(self):
        # Adicionar em S8
        print("funcao criada para definir a blanket")
        pass

    def test_order_2_ice_creams(self):
        numbers_of_ice_creams = 2
        # Adicionar em S8
        for count in range(numbers_of_ice_creams):
            print("funcao criada para adicionar quantidade de ice cream")
        pass

    def test_car_search_model_appears(self):
        # Adicionar em S8
        print("função criada para car search")
        pass
