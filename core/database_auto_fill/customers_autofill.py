from customer.models import Customer
import random
import string


def lower_string(length):
    result = ''.join(
        (random.choice(string.ascii_lowercase) for x in range(length)))
    return result


e_domains = ['@gmail.com', '@hotmail.com', '@mail.ru']
random_emails = [lower_string(5) + i for i in e_domains]
print(random_emails)
names = [
    'Oliver',
    'Mike',
    'Joe',
    'Stive',
    'Mark',
    'Adam',
    'Joy',
    'Ken'
]


def fill_db():
    for i in range(10):
        w = Customer.objects.create(
            name=random.choice(names),
            email=random.choice(random_emails),
            balance=random.randint(500, 6000),
            country='AG',
            age=random.randint(18, 64),
            sex='male',
            driver_licence=True
        )
        # w.save(force_insert=True)

fill_db()
