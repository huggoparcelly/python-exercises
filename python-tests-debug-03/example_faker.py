from faker import Faker

faker = Faker(locale='pt_BR')
Faker.seed(0)

print("Name:", faker.name())
print("Email:", faker.email())
print("Phone Number:", faker.phone_number())
print("CPF:", faker.cpf())
print("CNPJ:", faker.cnpj())