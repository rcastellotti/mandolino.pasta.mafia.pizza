from mpmp import db, Post, User, Category

db.drop_all()
db.create_all()
user = User(username="rcastellotti")
user.set_password("test")
db.session.add(user)
db.session.commit()

post = Post(
    text="lorem ipsum dolor sit amet consectetur adipisicing elit. Eveniet excepturi laboriosam temporibus ad quis atque! Quae, quos. Cumque alias saepe ipsum rerum dolores amet ullam reprehenderit nostrum, exercitationem tenetur eligendi.",
    date="23/01/2019",
    slug="198nsa",
    image="/static/test.png",
    rating=5
)
db.session.add(post)
category = Category(text="lorem")
category1 = Category(text="ipsum")
category2 = Category(text="dolor")
db.session.add(category)
db.session.add(category1)
db.session.add(category2)
post.categories.append(category)
post.categories.append(category1)
post.categories.append(category2)
post.author = user
db.session.commit()
