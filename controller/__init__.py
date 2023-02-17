from controller.home_controller import home
from controller.users_controller import user
from controller.pets_controller import pet
from controller.rentals_controller import rental


registerable_controllers = [
    home,
    user,
    pet,
    rental
]
