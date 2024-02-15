from faker import Faker

faker = Faker(locale='es_AR')

print("Sobrenome", faker.last_name())
print("Email", faker.email())
print("Senha", faker.password())
print("URL", faker.url())
print("Placa de carro", faker.license_plate())
