from models import db, Cupcake

def create_cupcakes():
    c1 = Cupcake(
        flavor="cherry",
        size="large",
        rating=5,
    )
    c2 = Cupcake(
        flavor="chocolate",
        size="small",
        rating=9,
        image="https://www.bakedbyrachel.com/wp-content/uploads/2018/01/chocolatecupcakesccfrosting1_bakedbyrachel.jpg"
    )
    c3 = Cupcake(
        flavor="tiramisu",
        size="medium",
        rating=10,
        image="https://www.rainbownourishments.com/wp-content/uploads/2021/05/vegan-tiramisu-cupcakes-1.jpg"
    )
    db.session.add_all([c1, c2, c3])
    db.session.commit()