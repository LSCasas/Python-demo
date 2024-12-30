import entities

# Create instances of User
user1 = entities.User("alfraedo", 30, "Alfreado", "Altamairano", "password123", "alfredo@example.com")
# Save user
user1.save()

post1 = entities.Post("Primaer Post", "Estae es el contenido del primer post", "activo", "alfredo")
post1.save()

article1 = entities.Article("Primaer Artículo", "Contenido adel primer artículo", "publicado", "imagen1.jpg", "alfredo")
article1.save()

