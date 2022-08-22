CREATE TABLE IF NOT EXISTS products(
    id INTEGER NOT NULL PRIMARY KEY,
    name TEXT NOT NULL,
    price INTEGER NOT NULL,
    accentColor TEXT,
    image TEXT NOT NULL,
    slug TEXT NOT NULL UNIQUE,
    quantityAvailable INTEGER NOT NULL,
    quantitySold INTEGER NOT NULL,
    description TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS customers(
    id INTEGER NOT NULL PRIMARY KEY,
    email TEXT NOT NULL UNIQUE,
    phone INTEGER NOT NULL UNIQUE,
    country TEXT NOT NULL,
    firstName TEXT NOT NULL,
    lastName TEXT NOT NULL,
    street TEXT NOT NULL,
    appartment INTEGER NOT NULL,
    postalCode TEXT NOT NULL,
    city TEXT NOT NULL,
    province TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS orders(
    id TEXT NOT NULL PRIMARY KEY,
    price INTEGER,
    stripePaymentIntent TEXT,
    shippingMode TEXT NOT NULL,
    additionalNotes TEXT,
    shippedAt TEXT,
    quantity INTEGER,
    customerId INTEGER REFERENCES customers
);

CREATE TABLE IF NOT EXISTS productOptions(
    id INTEGER NOT NULL PRIMARY KEY,
    option TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    productId INTEGER REFERENCES products
);

CREATE TABLE IF NOT EXISTS orderDetails(
    id TEXT NOT NULL PRIMARY KEY,
    quantity INTEGER,
    productId INTEGER REFERENCES productOptions,
    orderId INTEGER REFERENCES orders
);

CREATE TABLE IF NOT EXISTS coupons(
    id INTEGER NOT NULL PRIMARY KEY,
    coupon TEXT NOT NULL,
    discount INTEGER NOT NULL
);

PRAGMA foreign_keys = ON;

INSERT INTO
    products (
        name,
        price,
        accentColor,
        image,
        slug,
        quantityAvailable,
        quantitySold,
        description
    )
VALUES
    (
        "T-Shirt Pietre White",
        "25",
        "red-500",
        "pietre-tee-white.png",
        "pietre-tee-white",
        100,
        0,
        "La tua prima maglietta di Pietre.  
Imprescindibile per sentirsi un vero fan.  
Lasciati avvolgere dal pattern pietroso e indossala 24/7.  
Versione bianca, perfetta per quando c'è troppo sole ai Lagos de Covadonga. 

+  Base **Gildan Heavy Cotton**
+  100% cotone
+  185 gr.
+  Vestibilità regular"
    );

INSERT INTO
    products (
        name,
        price,
        accentColor,
        image,
        slug,
        quantityAvailable,
        quantitySold,
        description
    )
VALUES
    (
        "T-Shirt Pietre Black",
        "25",
        "pink-500",
        "pietre-tee-black.png",
        "pietre-tee-black",
        90,
        0,
        "La tua prima maglietta di Pietre.  
Imprescindibile per sentirsi un vero fan.  
Lasciati avvolgere dal pattern pietroso e indossala 24/7.  
Versione nera, va bene con tutto, particolarmente consigliata per fare serata con il Simone.

*  Base **Gildan Heavy Cotton**
*  100% cotone
*  185 gr.
*  Vestibilità regular"
    );

INSERT INTO
    products (
        name,
        price,
        accentColor,
        image,
        slug,
        quantityAvailable,
        quantitySold,
        description
    )
VALUES
    (
        "T-Shirt Pietre Grey",
        "25",
        "yellow-400",
        "pietre-tee-grey.png",
        "pietre-tee-grey",
        80,
        9,
        "La tua prima maglietta di Pietre.  
Imprescindibile per sentirsi un vero fan.  
Lasciati avvolgere dal pattern pietroso e indossala 24/7.  
Versione grigia, la più fangosa, la più Roubaix, la più cool.

*  Base **Gildan Heavy Cotton**
*  100% cotone
*  185 gr.
*  Vestibilità regular"
    );

INSERT INTO
    products (
        name,
        price,
        accentColor,
        image,
        slug,
        quantityAvailable,
        quantitySold,
        description
    )
VALUES
    (
        "Sticker",
        "5",
        "zinc-900",
        "sticker.png",
        "sticker",
        400,
        21,
        "Sticker d'appartenenza alla community.
Lo attacchi dove ti pare e in un attimo è brandizzata Pietre.
Bicicletta, borraccia, astuccio, pc, frigorifero, letto...lascia sfogare la tua fantasia!
Trovi gli sticker senza spese di spedizione fra le opzioni di acquisto di ogni t-shirt abbinata.  
6x6cm. 10 pezzi."
    );

INSERT INTO
    products (
        name,
        price,
        image,
        accentColor,
        slug,
        quantityAvailable,
        quantitySold,
        description
    )
VALUES
    (
        "Guerrilla Sticker",
        "5",
        "guerrilla-sticker.png",
        "zinc-900",
        "guerrilla-sticker",
        400,
        32,
        "Sei un fan duro e puro?
Vuoi diffondere la voce sul canale e la community?
Con questo pacchetto potrai tappezzare di pietrosità tutto il mondo facendo del vero e proprio guerrilla marketing.

Dai banchi di scuola alle arene sportive, dai pali della luce alle grandi salite del ciclismo.  

Grazie al simbolo di Youtube chiunque lo veda saprà dove cercarci.

Trovi gli sticker senza spese di spedizione fra le opzioni di acquisto di ogni t-shirt abbinata.  
6x6cm. 10 pezzi."
    );

INSERT INTO
    productOptions (option, quantity, productId)
VALUES
    ("s", 50, 1);

INSERT INTO
    productOptions (option, quantity, productId)
VALUES
    ("m", 50, 1);

INSERT INTO
    productOptions (option, quantity, productId)
VALUES
    ("l", 50, 1);

INSERT INTO
    productOptions (option, quantity, productId)
VALUES
    ("xl", 0, 1);

INSERT INTO
    productOptions (option, quantity, productId)
VALUES
    ("s", 50, 2);

INSERT INTO
    productOptions (option, quantity, productId)
VALUES
    ("m", 50, 2);

INSERT INTO
    productOptions (option, quantity, productId)
VALUES
    ("l", 50, 2);

INSERT INTO
    productOptions (option, quantity, productId)
VALUES
    ("xl", 0, 2);

INSERT INTO
    productOptions (option, quantity, productId)
VALUES
    ("s", 50, 3);

INSERT INTO
    productOptions (option, quantity, productId)
VALUES
    ("m", 50, 3);

INSERT INTO
    productOptions (option, quantity, productId)
VALUES
    ("l", 50, 3);

INSERT INTO
    productOptions (option, quantity, productId)
VALUES
    ("xl", 0, 3);

INSERT INTO
    productOptions (option, quantity, productId)
VALUES
    ("-", 50, 4);

INSERT INTO
    productOptions (option, quantity, productId)
VALUES
    ("-", 50, 5);