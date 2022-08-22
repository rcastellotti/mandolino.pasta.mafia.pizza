from mpmp import db, Post, User, Category

db.drop_all()
db.create_all()

post = Post(
    text="Lorem ipsum dolor sit amet consectetur adipisicing elit. Eveniet excepturi laboriosam temporibus ad quis atque! Quae, quos. Cumque alias saepe ipsum rerum dolores amet ullam reprehenderit nostrum, exercitationem tenetur eligendi.",
    date="23/01/2019",
    slug="198nsa",
    image="image1   ",
)
db.session.add(post)
db.session.commit()

user = User(
    email="fedfontana@rcastellotti.dev", username="fedfontana", password="fedfontana"
)
db.session.add(user)
db.session.commit()

category = Category(text="coca")
category1 = Category(text="zatla")
db.session.add(category)
db.session.add(category1)
db.session.commit()


post.categories.append(category1)
post.categories.append(category)
post.author=user
db.session.add(post)
db.session.commit()



post1 = Post(
    text="Lorem ipsum dolor sit amet consectetur adipisicing elit. Eveniet excepturi laboriosam temporibus ad quis atque! Quae, quos. Cumque alias saepe ipsum rerum dolores amet ullam reprehenderit nostrum, exercitationem tenetur eligendi.",
    date="23/01/2019",
    slug="35jksx",
    image="image",
)
db.session.add(post1)
db.session.commit()

user1 = User(
    email="roberto@rcastellotti.dev", username="roberto", password="fedfontana"
)
db.session.add(user1)
db.session.commit()

category2 = Category(text="fumo")
category3 = Category(text="zatlasss")
db.session.add(category2)
db.session.add(category3)
db.session.commit()


post1.categories.append(category2)
post1.categories.append(category3)
post1.author=user1
db.session.add(post1)
db.session.commit()